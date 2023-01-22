from keyboards import main_keyboard, elements_keyboard, weapon_keyboard, rarity_keyboard, region_keyboard
from static_text import welcome_text, element_text


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, world!")


async def two(update, context):
    await update.message.reply_text(text=welcome_text, reply_markup=main_keyboard())


async def filter_by_element(update, context):
    await update.callback_query.message.reply_text(text=element_text, reply_markup=elements_keyboard())


async def filter_by_weapon(update, context):
    await update.callback_query.message.reply_text(text=element_text, reply_markup=weapon_keyboard())


async def filter_by_rarity(update, context):
    await update.callback_query.message.reply_text(text=element_text, reply_markup=rarity_keyboard())


async def filter_by_region(update, context):
    await update.callback_query.message.reply_text(text=element_text, reply_markup=region_keyboard())
