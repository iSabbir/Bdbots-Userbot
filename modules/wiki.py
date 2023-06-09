# modules/wiki.py

import wikipedia
from pyrogram import filters, InlineKeyboardMarkup, InlineKeyboardButton
from main import Userbot

@Userbot.on_message(filters.command("wiki", prefixes="/"))
async def wiki(client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a search term.")
        return

    search_query = " ".join(message.command[1:])
    try:
        summary = wikipedia.summary(search_query, sentences=5)
    except wikipedia.exceptions.PageError:
        await message.reply("No matching page found. Please check your search term and try again.")
        return
    except wikipedia.exceptions.DisambiguationError as e:
        summary = f"Multiple pages match the search term. Here are some suggestions:\n\n{', '.join(e.options[:5])}"

    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Website", url="https://bdbots.blogspot.com"),
                InlineKeyboardButton("Channel", url="https://t.me/bdbots"),
            ]
        ]
    )

    await message.reply(summary + "\n\nDone by BDBOTS", reply_markup=reply_markup)
