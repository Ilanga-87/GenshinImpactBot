import logging

from env_data import TOKEN

from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ConversationHandler

from handlers import start, menu, value_filter, filter_by
from manage_data import FILTER_VALUE, FILTER_CRITERIA

from service import CRITERIA_FILTER, REPEAT_CRITERIA_FILTER, VALUE_FILTER, RESET

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TELEGRAM_TOKEN = TOKEN

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

start_handler = CommandHandler("start", start)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("menu", menu)],
    states={
        CRITERIA_FILTER: [CallbackQueryHandler(filter_by, pattern=f"^{FILTER_CRITERIA}")],
        VALUE_FILTER: [CallbackQueryHandler(value_filter, pattern=f"^{FILTER_VALUE}")],
        REPEAT_CRITERIA_FILTER: [CallbackQueryHandler(filter_by, pattern=f"^{FILTER_CRITERIA}")],
    },
    fallbacks=[CommandHandler("menu", menu)],
)

application.add_handler(start_handler)
application.add_handler(conv_handler)

application.run_polling()
