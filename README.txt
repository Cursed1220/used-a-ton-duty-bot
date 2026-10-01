USED-A-TON DUTY BOT — WINDOWS SETUP

WHAT IT DOES
- Green Clock In / red Clock Out buttons.
- Adds the existing On Duty role at clock-in and removes it at clock-out.
- Posts ONE completed-shift message to duty-logs, containing both clock-in and clock-out times plus shift duration.
- Saves completed shifts and active sessions in duty.db.
- Tracks total, peak (18:00-23:00), and off-peak time.
- /hours lets staff see their own totals; management can inspect another member.
- /force-clockout lets management end a forgotten active shift.

1. INSTALL PYTHON
Install Python 3.11 or newer from python.org. During installation tick "Add Python to PATH".

2. CREATE THE DISCORD BOT
Go to Discord Developer Portal > Applications > New Application.
Name it Used-A-Ton Duty Bot.
Open Bot and create/reset the bot token. NEVER send this token to anyone.
Enable SERVER MEMBERS INTENT.

3. INVITE IT
In OAuth2 / URL Generator select bot and applications.commands.
Bot permissions needed: View Channels, Send Messages, Embed Links, Read Message History, Manage Roles.
It does NOT need Administrator.
Invite it to Used-A-Ton.

4. ROLE ORDER
In Server Settings > Roles, place the actual Used-A-Ton Duty Bot role ABOVE the green On Duty role. The bot cannot add/remove a role above itself.
Set the On Duty role to "Display role members separately from online members" if you want the right-hand member list to show an On Duty group.

5. GET DISCORD IDS
Discord Settings > Advanced > Developer Mode ON.
Right-click the server, channels and roles and choose Copy ID.
You need: Server ID, On Duty role ID, duty-logs channel ID, clock-in-out channel ID, Manager role ID.

6. CONFIGURE
Make a copy of .env.example and rename the copy to .env.
Open .env in Notepad and replace the placeholders with your IDs and bot token.
Do not put quotes around the numbers/token.

7. START
Double-click start.bat. First launch installs the required Python packages and starts the bot.
Keep that window open while you want the bot online.

8. POST THE PANEL
In Discord, type /post-clock once. A manager (or someone with Manage Server) can run it. The bot posts the panel in your configured clock-in-out channel.

TEST
Click Clock In: you should receive On Duty and appear in the On Duty group.
Click Clock Out: On Duty is removed and ONE completed-shift entry is posted to duty-logs.
Run /hours to see saved totals.

IMPORTANT
- Never share your .env or Discord bot token.
- duty.db contains the saved duty records; keep it if moving the bot to another computer.
- If the bot says it cannot manage roles, move its Discord bot role above On Duty and make sure Manage Roles is enabled.
