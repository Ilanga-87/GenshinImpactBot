import logging
import os
import sys

from env_data import TOKEN

import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

from handlers import start, two, filter_by_element, filter_by_weapon, filter_by_rarity, filter_by_region
from manage_data import TWO_TWO, NEW, ELEMENT_CHOICE, WEAPON_CHOICE, RARITY_CHOICE, REGION_CHOICE

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TELEGRAM_TOKEN = TOKEN

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
start_handler = CommandHandler("start", start)
two_handler = CommandHandler("two", two)

# main menu handlers
element_handler = CallbackQueryHandler(filter_by_element, pattern=f"^{ELEMENT_CHOICE}")
weapon_handler = CallbackQueryHandler(filter_by_weapon, pattern=f"^{WEAPON_CHOICE}")
rarity_handler = CallbackQueryHandler(filter_by_rarity, pattern=f"^{RARITY_CHOICE}")
region_handler = CallbackQueryHandler(filter_by_region, pattern=f"^{REGION_CHOICE}")

application.add_handler(start_handler)
application.add_handler(two_handler)

application.add_handler(element_handler)
application.add_handler(weapon_handler)
application.add_handler(rarity_handler)
application.add_handler(region_handler)

application.run_polling()
