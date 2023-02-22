import os
from dotenv import load_dotenv
import logging

from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ConversationHandler, \
    MessageHandler, filters

from handlers import start, start_filter, value_filter, criteria_filter, helper, undefined_commands
from manage_data import FILTER_VALUE, FILTER_CRITERIA

from service import CRITERIA_FILTER, REPEAT_CRITERIA_FILTER, VALUE_FILTER

load_dotenv()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", helper)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("filter", start_filter)],
    states={
        CRITERIA_FILTER: [CallbackQueryHandler(criteria_filter, pattern=f"^{FILTER_CRITERIA}")],
        VALUE_FILTER: [CallbackQueryHandler(value_filter, pattern=f"^{FILTER_VALUE}")],
        REPEAT_CRITERIA_FILTER: [CallbackQueryHandler(criteria_filter, pattern=f"^{FILTER_CRITERIA}")],
    },
    fallbacks=[CommandHandler("filter", start_filter)],
)

unknown_handler = MessageHandler(filters.COMMAND, undefined_commands)

application.add_handler(start_handler)
application.add_handler(help_handler)
application.add_handler(conv_handler)
application.add_handler(unknown_handler)

application.run_polling()
