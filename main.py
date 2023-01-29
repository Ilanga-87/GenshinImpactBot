import logging
import os
import sys

from env_data import TOKEN

import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, ConversationHandler

from handlers import start, menu, value_filter, filter_by
from manage_data import (
    TWO_TWO, NEW, ELEMENT_CHOICE, WEAPON_CHOICE, RARITY_CHOICE, REGION_CHOICE,
    ELEMENT_VALUE, WEAPON_VALUE, RARITY_VALUE, REGION_VALUE, FILTER_VALUE, FILTER_CRITERIA
)

from service import REPEAT_MAIN_KB, CRITERIA_FILTER, REPEAT_CRITERIA_FILTER, VALUE_FILTER, REPEAT_VALUE_FILTER, RESET

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TELEGRAM_TOKEN = TOKEN

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("menu", menu)],
    states={
        CRITERIA_FILTER: [CallbackQueryHandler(filter_by, pattern=f"^{FILTER_CRITERIA}")],
        VALUE_FILTER: [CallbackQueryHandler(value_filter, pattern=f"^{FILTER_VALUE}")],
        REPEAT_CRITERIA_FILTER: [CallbackQueryHandler(filter_by, pattern=f"^{FILTER_CRITERIA}")],
        REPEAT_VALUE_FILTER: [CallbackQueryHandler(value_filter, pattern=f"^{FILTER_VALUE}")],
    },
    fallbacks=[CallbackQueryHandler(menu, pattern=f"^{RESET}")]
)


# common handlers, TODO replace the start one with menu functionality
start_handler = CommandHandler("start", start)
# menu_handler = CommandHandler("menu", menu)
#
# # main menu handler
# criteria_handler = CallbackQueryHandler(filter_by, pattern=f"^{FILTER_CRITERIA}")
#
# # inner keyboards handler
# value_handler = CallbackQueryHandler(value_filter, pattern=f"^{FILTER_VALUE}")
#
#
application.add_handler(start_handler)
# application.add_handler(menu_handler)
#
# application.add_handler(criteria_handler)
# application.add_handler(value_handler)

application.add_handler(conv_handler)

application.run_polling()
