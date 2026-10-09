import os
import json
import sqlite3
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo

import discord
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID", "0"))

ON_DUTY_ROLE_ID = int(os.getenv("ON_DUTY_ROLE_ID", "0"))
DUTY_LOG_CHANNEL_ID = int(os.getenv("DUTY_LOG_CHANNEL_ID", "0"))
CLOCK_CHANNEL_ID = int(os.getenv("CLOCK_CHANNEL_ID", "0"))
MANAGER_ROLE_ID = int(os.getenv("MANAGER_ROLE_ID", "0"))
def load_daily_roster_webhook_url():
    """Read the webhook from Home Assistant add-on options, with env fallback."""
    options_path = "/data/options.json"
    try:
        with open(options_path, "r", encoding="utf-8") as options_file:
            options = json.load(options_file)
        value = options.get("daily_roster_webhook_url", "")
        if value:
            return str(value).strip()
    except (OSError, json.JSONDecodeError):
        pass
    return os.getenv("DAILY_ROSTER_WEBHOOK_URL", "").strip()


DAILY_ROSTER_WEBHOOK_URL = load_daily_roster_webhook_url()

# ==============================
# LOA SETTINGS
# ==============================

LOA_ROLE_ID = 1553335212723802122
LOA_CHANNEL_ID = 1553340731089752074

TZ = ZoneInfo(os.getenv("TIMEZONE", "Africa/Johannesburg"))

DB = "duty.db"


# ==============================
# DISCORD SETUP
# ==============================

intents = discord.Intents.default()

intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# ==============================
# DATABASE
# ==============================

def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c


def init_db():
    with db() as c:

        c.execute("""
            CREATE TABLE IF NOT EXISTS active (
                user_id INTEGER PRIMARY KEY,
                clock_in TEXT NOT NULL
            )
        """)

        c.execute("""
            CREATE TABLE IF NOT EXISTS shifts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                clock_in TEXT,
                clock_out TEXT,
                seconds INTEGER,
                peak_seconds INTEGER,
                offpeak_seconds INTEGER
            )
        """)


# ==============================
# TIME FUNCTIONS
# ==============================

def fmt_duration(sec):
    mins = max(0, int(sec)) // 60
    h, m = divmod(mins, 60)

    return f"{h}h {m:02d}m"


def peak_seconds(start, end):

    total = 0.0
    day = start.date()

    while day <= end.date():

        p1 = datetime.combine(
            day,
            time(18, 0),
            TZ
        )

        p2 = datetime.combine(
            day,
            time(23, 0),
            TZ
        )

        a = max(start, p1)
        b = min(end, p2)

        if b > a:
            total += (b - a).total_seconds()

        day += timedelta(days=1)

    return int(total)


# ==============================
# MANAGEMENT CHECK
# ==============================

def manager(interaction):

    return (
        interaction.user.guild_permissions.manage_guild
        or (
            MANAGER_ROLE_ID
            and any(
                r.id == MANAGER_ROLE_ID
                for r in interaction.user.roles
            )
        )
    )


# ============================================================
# LOA ROLE MONITOR
# ============================================================

@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):

    before_has_loa = any(
        role.id == LOA_ROLE_ID
        for role in before.roles
    )

    after_has_loa = any(
        role.id == LOA_ROLE_ID
        for role in after.roles
    )

    # Nothing changed regarding LOA
    if before_has_loa == after_has_loa:
        return

    channel = after.guild.get_channel(LOA_CHANNEL_ID)

    if not channel:
        print(
            f"LOA channel {LOA_CHANNEL_ID} could not be found."
        )
        return

    now = datetime.now(TZ)

    # ==========================================
    # LOA ROLE ADDED
    # ==========================================

    if not before_has_loa and after_has_loa:

        embed = discord.Embed(
            title="🟠 STAFF MEMBER ON LOA",
            description=(
                f"**{after.display_name}** has gone on "
                f"**Leave of Absence**.\n\n"
                f"🔴 **Status:** On Leave\n"
                f"🕐 **Time:** {now:%H:%M}\n"
                f"📅 **Date:** {now:%d %B %Y}"
            ),
            color=discord.Color.orange(),
            timestamp=now
        )

        embed.set_footer(
            text="Used-A-Ton Management"
        )

        try:
            await channel.send(embed=embed)

            print(
                f"LOA: {after.display_name} went on LOA."
            )

        except discord.Forbidden:
            print(
                "ERROR: I don't have permission to send "
                "messages in the LOA channel."
            )

        except Exception as e:
            print(
                f"LOA announcement error: {e}"
            )

    # ==========================================
    # LOA ROLE REMOVED
    # ==========================================

    elif before_has_loa and not after_has_loa:

        embed = discord.Embed(
            title="🟢 STAFF MEMBER BACK AT WORK",
            description=(
                f"**{after.display_name}** has returned "
                f"from **Leave of Absence**.\n\n"
                f"🟢 **Status:** Back at Work\n"
                f"🕐 **Time:** {now:%H:%M}\n"
                f"📅 **Date:** {now:%d %B %Y}"
            ),
            color=discord.Color.green(),
            timestamp=now
        )

        embed.set_footer(
            text="Used-A-Ton Management"
        )

        try:
            await channel.send(embed=embed)

            print(
                f"LOA: {after.display_name} returned to work."
            )

        except discord.Forbidden:
            print(
                "ERROR: I don't have permission to send "
                "messages in the LOA channel."
            )

        except Exception as e:
            print(
                f"LOA announcement error: {e}"
            )


# ============================================================
# DUTY BUTTONS
# ============================================================

class DutyView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=None
        )


    @discord.ui.button(
        label="Clock In",
        emoji="🟢",
        style=discord.ButtonStyle.success,
        custom_id="uat_clock_in"
    )
    async def clock_in(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        now = datetime.now(TZ)

        with db() as c:

            row = c.execute(
                "SELECT clock_in FROM active WHERE user_id=?",
                (interaction.user.id,)
            ).fetchone()

            if row:

                return await interaction.response.send_message(
                    "You are already clocked in.",
                    ephemeral=True
                )

            c.execute(
                """
                INSERT INTO active(user_id,clock_in)
                VALUES (?,?)
                """,
                (
                    interaction.user.id,
                    now.isoformat()
                )
            )

        role = interaction.guild.get_role(
            ON_DUTY_ROLE_ID
        )

        if role:

            try:

                await interaction.user.add_roles(
                    role,
                    reason="Clocked in"
                )

            except discord.Forbidden as e:

                print(
                    f"ROLE ERROR: {e}"
                )

        await interaction.response.send_message(
            f"🟢 Clocked in at **{now:%H:%M}**.",
            ephemeral=True
        )


    @discord.ui.button(
        label="Clock Out",
        emoji="🔴",
        style=discord.ButtonStyle.danger,
        custom_id="uat_clock_out"
    )
    async def clock_out(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        now = datetime.now(TZ)

        with db() as c:

            row = c.execute(
                "SELECT clock_in FROM active WHERE user_id=?",
                (interaction.user.id,)
            ).fetchone()

            if not row:

                return await interaction.response.send_message(
                    "You are not currently clocked in.",
                    ephemeral=True
                )

            start = datetime.fromisoformat(
                row["clock_in"]
            ).astimezone(TZ)

            seconds = max(
                0,
                int(
                    (now - start).total_seconds()
                )
            )

            peak = peak_seconds(
                start,
                now
            )

            off = seconds - peak

            c.execute(
                "DELETE FROM active WHERE user_id=?",
                (interaction.user.id,)
            )

            c.execute(
                """
                INSERT INTO shifts(
                    user_id,
                    clock_in,
                    clock_out,
                    seconds,
                    peak_seconds,
                    offpeak_seconds
                )
                VALUES (?,?,?,?,?,?)
                """,
                (
                    interaction.user.id,
                    start.isoformat(),
                    now.isoformat(),
                    seconds,
                    peak,
                    off
                )
            )

        role = interaction.guild.get_role(
            ON_DUTY_ROLE_ID
        )

        if role:

            try:

                await interaction.user.remove_roles(
                    role,
                    reason="Clocked out"
                )

            except discord.Forbidden:

                pass

        ch = interaction.guild.get_channel(
            DUTY_LOG_CHANNEL_ID
        )

        name = interaction.user.display_name

        if ch:

            embed = discord.Embed(
                title="Used-A-Ton Duty Log",
                description=(
                    f"🟢 **{name} — ON DUTY**\n"
                    f"Clocked in: **{start:%H:%M}**\n\n"
                    f"🔴 **{name} — OFF DUTY**\n"
                    f"Clocked out: **{now:%H:%M}**\n\n"
                    f"**Shift worked: "
                    f"{fmt_duration(seconds)}**"
                ),
                color=discord.Color.from_rgb(255, 105, 180)
            )

            embed.set_footer(
                text=f"{start:%d %b %Y} • Africa/Johannesburg"
            )

            await ch.send(
                embed=embed
            )

        await interaction.response.send_message(
            f"🔴 Clocked out. Shift worked: "
            f"**{fmt_duration(seconds)}**.",
            ephemeral=True
        )


# ============================================================
# POST CLOCK PANEL
# ============================================================

@bot.tree.command(
    name="post-clock",
    description="Post the Used-A-Ton clock-in/out panel"
)
async def post_clock(
    interaction: discord.Interaction
):

    if not manager(interaction):

        return await interaction.response.send_message(
            "Management only.",
            ephemeral=True
        )

    ch = (
        interaction.guild.get_channel(
            CLOCK_CHANNEL_ID
        )
        or interaction.channel
    )

    e = discord.Embed(
        title="USED-A-TON DUTY CLOCK",
        description=(
            "Use the buttons below when starting "
            "and finishing your shift.\n\n"
            "🟢 **Clock In** — starts your shift "
            "and gives the On Duty role.\n"
            "🔴 **Clock Out** — ends your shift, "
            "removes the role and records your hours."
        )
    )

    await ch.send(
        embed=e,
        view=DutyView()
    )

    await interaction.response.send_message(
        "Clock panel posted.",
        ephemeral=True
    )


# ============================================================
# HOURS
# ============================================================

@bot.tree.command(
    name="hours",
    description="View saved duty hours"
)
@app_commands.describe(
    member="Staff member (leave blank for yourself)"
)
async def hours(
    interaction: discord.Interaction,
    member: discord.Member | None = None
):

    target = member or interaction.user

    if (
        member
        and member.id != interaction.user.id
        and not manager(interaction)
    ):

        return await interaction.response.send_message(
            "Management only.",
            ephemeral=True
        )

    with db() as c:

        r = c.execute(
            """
            SELECT
                COALESCE(SUM(seconds),0) s,
                COALESCE(SUM(peak_seconds),0) p,
                COALESCE(SUM(offpeak_seconds),0) o
            FROM shifts
            WHERE user_id=?
            """,
            (target.id,)
        ).fetchone()

    await interaction.response.send_message(
        f"**{target.display_name}**\n"
        f"Total: **{fmt_duration(r['s'])}**\n"
        f"Peak (18:00–23:00): **{fmt_duration(r['p'])}**\n"
        f"Off-peak: **{fmt_duration(r['o'])}**",
        ephemeral=True
    )


# ============================================================
# FORCE CLOCK OUT
# ============================================================

@bot.tree.command(
    name="force-clockout",
    description="Management: clock out a staff member now"
)
async def force_clockout(
    interaction: discord.Interaction,
    member: discord.Member
):

    if not manager(interaction):

        return await interaction.response.send_message(
            "Management only.",
            ephemeral=True
        )

    now = datetime.now(TZ)

    with db() as c:

        row = c.execute(
            "SELECT clock_in FROM active WHERE user_id=?",
            (member.id,)
        ).fetchone()

        if not row:

            return await interaction.response.send_message(
                "That member is not clocked in.",
                ephemeral=True
            )

        start = datetime.fromisoformat(
            row["clock_in"]
        ).astimezone(TZ)

        sec = max(
            0,
            int(
                (now - start).total_seconds()
            )
        )

        peak = peak_seconds(
            start,
            now
        )

        c.execute(
            "DELETE FROM active WHERE user_id=?",
            (member.id,)
        )

        c.execute(
            """
            INSERT INTO shifts(
                user_id,
                clock_in,
                clock_out,
                seconds,
                peak_seconds,
                offpeak_seconds
            )
            VALUES (?,?,?,?,?,?)
            """,
            (
                member.id,
                start.isoformat(),
                now.isoformat(),
                sec,
                peak,
                sec - peak
            )
        )

    role = interaction.guild.get_role(
        ON_DUTY_ROLE_ID
    )

    if role:

        try:

            await member.remove_roles(
                role
            )

        except discord.Forbidden:

            pass

    await interaction.response.send_message(
        f"{member.display_name} clocked out. "
        f"Shift: **{fmt_duration(sec)}**.",
        ephemeral=True
    )


# ============================================================
# DAILY ROSTER REPORT
# ============================================================

def daily_seconds_for_user(user_id: int, day_start: datetime, day_end: datetime) -> int:
    """Total a user's recorded duty time overlapping one local calendar day."""
    total = 0
    with db() as c:
        completed = c.execute(
            "SELECT clock_in, clock_out FROM shifts WHERE user_id=?",
            (user_id,)
        ).fetchall()
        active = c.execute(
            "SELECT clock_in FROM active WHERE user_id=?",
            (user_id,)
        ).fetchone()

    intervals = []
    for row in completed:
        if not row["clock_in"] or not row["clock_out"]:
            continue
        start = datetime.fromisoformat(row["clock_in"]).astimezone(TZ)
        end = datetime.fromisoformat(row["clock_out"]).astimezone(TZ)
        intervals.append((start, end))

    # If still clocked in when the report runs, count the time through the end
    # of this roster day. The active shift will be saved normally when they clock out.
    if active:
        start = datetime.fromisoformat(active["clock_in"]).astimezone(TZ)
        intervals.append((start, datetime.now(TZ)))

    for start, end in intervals:
        overlap_start = max(start, day_start)
        overlap_end = min(end, day_end)
        if overlap_end > overlap_start:
            total += int((overlap_end - overlap_start).total_seconds())
    return total


@tasks.loop(time=time(20, 30, tzinfo=TZ))
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
