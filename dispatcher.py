import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from handlers import start, two

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TELEGRAM_TOKEN = "5611962231:AAFpuoddWx5SKc_aOXv1wX3P3Ta9P2p-8GY"

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
start_handler = CommandHandler("start", start)
two_handler = CommandHandler("two", two)
application.add_handler(start_handler)
application.add_handler(two_handler)
application.run_polling()
