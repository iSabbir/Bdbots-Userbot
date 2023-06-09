# modules/weather.py

import requests
from pyrogram import filters, InlineKeyboardMarkup, InlineKeyboardButton
from main import Userbot

API_KEY = 'your_openweathermap_api_key'

@Userbot.on_message(filters.command("weather", prefixes="/"))
async def weather(client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a city name.")
        return

    city = " ".join(message.command[1:])
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        await message.reply("An error occurred. Please check your city name and try again.")
    else:
        weather_data = data["weather"][0]
        main_data = data["main"]
        description = weather_data["description"].capitalize()
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_message = f"Weather in {city}:\n\n{description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"

        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Website", url="https://bdbots.blogspot.com"),
                    InlineKeyboardButton("Channel", url="https://t.me/bdbots"),
                ]
            ]
        )

        await message.reply(weather_message + "\n\nDone by BDBOTS", reply_markup=reply_markup)
