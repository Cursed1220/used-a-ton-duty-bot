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
    # Home Assistant add-on options are stored here when configured in config.yaml.
    options_path = "/data/options.json"
    try:
        with open(options_path, "r", encoding="utf-8") as options_file:
            options = json.load(options_file)
        value = options.get("daily_roster_webhook_url", "")
        if value:
            return str(value).strip()
    except (OSError, json.JSONDecodeError):
        pass

    # Environment-variable fallback for other hosting setups.
    return os.getenv("DAILY_ROSTER_WEBHOOK_URL", "").strip()


DAILY_ROSTER_WEBHOOK_URL = load_daily_roster_webhook_url()

# ==============================
# LOA SETTINGS
# ==============================

LOA_ROLE_ID = 1553335212723802122
LOA_CHANNEL_ID = 1553340731089752074

TZ = ZoneInfo(os.getenv("TIMEZONE", "Africa/Johannesburg"))

DB = "/data/duty.db"


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
