from nicegrill import utils
from weather import Weather as wtr
from database import settingsdb as settings
import logging


class Weather:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    async def weatherxxx(message):
        """Shows the weather of specified city"""
        if not settings.check_city() and not utils.get_arg(message):
            await message.edit("<b>Enter a city name first</b>")
            return
        city = settings.check_city() if not utils.get_arg(
            message) else utils.get_arg(message)
        weather = wtr.find(city)
        await message.edit(
            f"<b>City:</b> <i>{weather['weather']['city']}</i>\n"
            f"<b>Temperature:</b> <i>{round(weather['weather']['temp'])}°C</i>\n"
            f"<b>Pressure:</b> <i>{weather['weather']['pressure']} hPa</i>\n"
            f"<b>Humidity:</b> <i>{weather['weather']['humidity']}%</i>\n"
            f"<b>Latency:</b> <i>{weather['weather']['lat']}</i>\n"
            f"<b>Status:</b> <i>{weather['main']}</i>\n"
            f"<b>Description:</b> <i>{weather['description'].capitalize()}</i>\n"
            f"<b>Wind Speed:</b> <i>{weather['wind']['speed']} m/s</i>\n")

    async def setcityxxx(message):
        """Sets a default city so that you don't have to type it everytime"""
        if not utils.get_arg(message):
            settings.delete("City")
            await message.edit("<b>Saved city name removed</b>")
            return
        settings.delete("City")
        settings.set_city(utils.get_arg(message))
        await message.edit("<b>Successfully saved</b>")
