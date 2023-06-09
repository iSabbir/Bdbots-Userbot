# modules/commands.py

from pyrogram import filters
from main import Userbot

@Userbot.on_message(filters.command("start", prefixes="/"))
async def start(client, message):
    await message.reply("Hello! I'm BDBOTS, a super powerful userbot. Check out our website: [BDBOTS](https://bdbots.blogspot.com) and our Telegram channel: [T.me/bdbots](https://t.me/bdbots)", parse_mode="markdown")
```

2. `modules/autoupdate.py` - Automatic updates:

````python
# modules/autoupdate.py

import os
import subprocess
import sys
from pyrogram import filters
from main import Userbot

@Userbot.on_message(filters.command("update", prefixes="/") & filters.me)
async def autoupdate(client, message):
    await message.edit("Updating...")

    try:
        output = subprocess.check_output(["git", "pull"])
    except subprocess.CalledProcessError as error:
        await message.edit(f"Update failed\nError: {error.output.decode()}")
        return

    if "Already up to date" not in output.decode():
        await message.edit("Update successful. Restarting...")
        os.execv(sys.executable, [sys.executable] + sys.argv)
    else:
        await message.edit("Already up to date.")
```
