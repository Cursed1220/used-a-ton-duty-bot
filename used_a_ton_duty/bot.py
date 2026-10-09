    if active:
        start = datetime.fromisoformat(active["clock_in"]).astimezone(TZ)
        intervals.append((start, datetime.now(TZ)))

    for start, end in intervals:
        overlap_start = max(start, day_start)
        overlap_end = min(end, day_end)
        if overlap_end > overlap_start:
            total += int((overlap_end - overlap_start).total_seconds())
    return total


@tasks.loop(time=time(20, 0, tzinfo=TZ))
async def daily_roster_report():
    if not DAILY_ROSTER_WEBHOOK_URL:
        print("Daily roster skipped: DAILY_ROSTER_WEBHOOK_URL is not configured.")
        return

    now = datetime.now(TZ)
    day_start = datetime.combine(now.date(), time.min, TZ)
    day_end = day_start + timedelta(days=1)

    # Use the configured guild, or the first available guild if no ID is set.
    guild = bot.get_guild(GUILD_ID) if GUILD_ID else (bot.guilds[0] if bot.guilds else None)
    if guild is None:
        print("Daily roster skipped: bot could not find the Discord server.")
        return

    with db() as c:
        ids = set(row[0] for row in c.execute(
            "SELECT DISTINCT user_id FROM shifts WHERE clock_in < ? AND clock_out > ?",
            (day_end.isoformat(), day_start.isoformat())
        ).fetchall())
        ids.update(row[0] for row in c.execute("SELECT user_id FROM active").fetchall())

    lines = []
    for user_id in ids:
        seconds = daily_seconds_for_user(user_id, day_start, day_end)
        if seconds <= 0:
            continue
        member = guild.get_member(user_id)
        if member is None:
            try:
                member = await guild.fetch_member(user_id)
            except (discord.NotFound, discord.Forbidden, discord.HTTPException):
                member = None
        name = member.display_name if member else f"Discord user {user_id}"
        lines.append((name.casefold(), f"**{discord.utils.escape_markdown(name)}**\nTotal: {fmt_duration(seconds)}"))

    lines.sort(key=lambda item: item[0])
    content = "\n\n".join(line for _, line in lines)
    if not content:
        content = "No staff hours recorded today."

    try:
        webhook = discord.Webhook.from_url(DAILY_ROSTER_WEBHOOK_URL, client=bot)
        await webhook.send(content=content, username="Used-A-Ton Daily Roster", allowed_mentions=discord.AllowedMentions.none())
        print(f"Daily roster posted for {now:%Y-%m-%d}.")
    except Exception as e:
        print(f"Daily roster webhook error: {e}")


@daily_roster_report.before_loop
async def before_daily_roster_report():
    await bot.wait_until_ready()


# ============================================================
# BOT READY
# ============================================================

@bot.event
async def on_ready():

    bot.add_view(
        DutyView()
    )

    try:

        if GUILD_ID:

            guild = discord.Object(
                id=GUILD_ID
            )

            bot.tree.copy_global_to(
                guild=guild
            )

            await bot.tree.sync(
                guild=guild
            )

        else:

            await bot.tree.sync()

    except Exception as e:

        print(
            "Command sync error:",
            e
        )

    print(
        f"Logged in as {bot.user}"
    )

    print(
        f"LOA monitoring enabled | "
        f"Role: {LOA_ROLE_ID} | "
        f"Channel: {LOA_CHANNEL_ID}"
    )

    if not daily_roster_report.is_running():
        daily_roster_report.start()


# ============================================================
# START
# ============================================================

init_db()

if not TOKEN:

    raise RuntimeError(
        "DISCORD_TOKEN is missing. "
        "Copy .env.example to .env and add your token."
    )

bot.run(TOKEN)
