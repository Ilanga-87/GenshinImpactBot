from service import CRITERIA_INPUT, VALUE_INPUT, get_characters, all_chars_list, display_characters
from keyboards import main_keyboard, elements_keyboard, weapon_keyboard, rarity_keyboard, region_keyboard
from static_text import welcome_text, element_text, success_message


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, world!")


async def menu(update, context):
    await update.message.reply_text(text=welcome_text, reply_markup=main_keyboard())


async def filter_by_element(update, context):
    CRITERIA_INPUT[0] = int(update.callback_query["data"])
    print(CRITERIA_INPUT)
    await hide_previous_keyboard(update, context)
    await update.callback_query.message.reply_text(text=element_text, reply_markup=elements_keyboard())


async def filter_by_weapon(update, context):
    await hide_previous_keyboard(update, context)
    await update.callback_query.message.reply_text(text=element_text, reply_markup=weapon_keyboard())


async def filter_by_rarity(update, context):
    await hide_previous_keyboard(update, context)
    await update.callback_query.message.reply_text(text=element_text, reply_markup=rarity_keyboard())


async def filter_by_region(update, context):
    await hide_previous_keyboard(update, context)
    await update.callback_query.message.reply_text(text=element_text, reply_markup=region_keyboard())


async def value_filter(update, context):
    VALUE_INPUT[0] = update.callback_query["data"].split(".")[-1]
    filtered_list = get_characters(all_chars_list, CRITERIA_INPUT[0], VALUE_INPUT[0])
    print(CRITERIA_INPUT)
    print(VALUE_INPUT)
    print(filtered_list)
    display_list = display_characters(filtered_list)
    print(display_list)
    await update.callback_query.message.edit_text(display_list)


async def hide_previous_keyboard(update, context):
    await update.callback_query.message.edit_text(success_message)
