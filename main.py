import logging
import os
import sys

from env_data import TOKEN

import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

from handlers import start, menu, filter_by_element, filter_by_weapon, filter_by_rarity, filter_by_region, value_filter
from manage_data import (
    TWO_TWO, NEW, ELEMENT_CHOICE, WEAPON_CHOICE, RARITY_CHOICE, REGION_CHOICE,
    ELEMENT_VALUE, WEAPON_VALUE, RARITY_VALUE, REGION_VALUE, FILTER_VALUE,
)

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TELEGRAM_TOKEN = TOKEN

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# common handlers, TODO replace the start one with menu functionality
start_handler = CommandHandler("start", start)
menu_handler = CommandHandler("menu", menu)

# main menu handlers
element_handler = CallbackQueryHandler(filter_by_element, pattern=f"^{ELEMENT_CHOICE}")
weapon_handler = CallbackQueryHandler(filter_by_weapon, pattern=f"^{WEAPON_CHOICE}")
rarity_handler = CallbackQueryHandler(filter_by_rarity, pattern=f"^{RARITY_CHOICE}")
region_handler = CallbackQueryHandler(filter_by_region, pattern=f"^{REGION_CHOICE}")

value_handler = CallbackQueryHandler(value_filter, pattern=f"^{FILTER_VALUE}")

application.add_handler(start_handler)
application.add_handler(menu_handler)

application.add_handler(element_handler)
application.add_handler(weapon_handler)
application.add_handler(rarity_handler)
application.add_handler(region_handler)

application.add_handler(value_handler)

application.run_polling()
