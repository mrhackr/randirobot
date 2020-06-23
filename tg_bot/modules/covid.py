import requests
import datetime
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async
from prettytable import PrettyTable

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

@run_async
def covid(bot: Bot, update: Update):
    message = update.effective_message
    text = message.text.split(' ', 1)
    if len(text) == 1:
        r = requests.get(f"https://corona.lmao.ninja/v2/all").json()
        reply_text = f"🦠 *Global Totals* 🦠\n😷 Total Cases : {r['cases']:,}\n🤧 Cases Today : {r['todayCases']:,}\n💀 Total Deaths : {r['deaths']:,}\n⚰ Deaths Today : {r['todayDeaths']:,}\n😇 Recovered : {r['recovered']:,}\n🤒 Active : {r['active']:,}\n🤕 Critical : {r['critical']:,}\nℹ Cases/Mil : {r['casesPerOneMillion']}\nℹ Deaths/Mil : {r['deathsPerOneMillion']}"
    else:
        variabla = text[1]
        r = requests.get(f"https://corona.lmao.ninja/v2/countries/{variabla}").json()
        reply_text = f"🦠 *Cases For* *{r['country']}* 🦠: \n😷 Total Cases : {r['cases']:,}\n🤧 Cases Today : {r['todayCases']:,}\n💀 Total Deaths : {r['deaths']:,}\n⚰ Deaths Today : {r['todayDeaths']:,}\n😇 Recovered: {r['recovered']:,}\n🤒 Active: {r['active']:,}\n🤕 Critical : {r['critical']:,}\nℹ Cases/Mil : {r['casesPerOneMillion']}\nℹ Deaths/Mil : {r['deathsPerOneMillion']}"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)

__help__ = """
 - /covid To Get Global Data
 - /covid <country> To Get Data Of A Country
"""

COVID_HANDLER = DisableAbleCommandHandler(["covid", "corona"], covid)

dispatcher.add_handler(COVID_HANDLER)

__mod_name__ = "Corona Info"
