import service
from service import (
    CRITERIA_INPUT, VALUE_INPUT,
    get_characters, display_characters, clear_pressed_button,
    CRITERIA_FILTER, VALUE_FILTER, REPEAT_CRITERIA_FILTER, REPEAT_VALUE_FILTER, REPEAT_MAIN_KB
)
from keyboards import dynamic_main_keyboard, value_keyboards_list
from static_text import welcome_text, success_message, second_criteria_text, value_choice_text


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, world!")


async def menu(update, context):
    await update.message.reply_text(text=welcome_text, reply_markup=dynamic_main_keyboard())
    return CRITERIA_FILTER


async def start_over(update, context):
    query = update.callback_query
    await query.answer()
    await update.message.reply_text(text=welcome_text, reply_markup=dynamic_main_keyboard())


async def filter_by(update, context):
    await hide_previous_keyboard(update, context)
    pointer = int(update.callback_query["data"].split(".")[-1])
    CRITERIA_INPUT[0] = pointer
    # print(CRITERIA_INPUT)
    clear_pressed_button(pointer)
    # btns = clear_pressed_button(pointer)
    # print(btns)
    reply_text = value_choice_text[pointer]
    reply_keyboard = value_keyboards_list[pointer]
    await update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_keyboard)
    return VALUE_FILTER


async def value_filter(update, context):
    VALUE_INPUT[0] = update.callback_query["data"].split(".")[-1]
    print(CRITERIA_INPUT)
    print(VALUE_INPUT)
    filtered_list = get_characters(service.list_to_filter, CRITERIA_INPUT[0] + 1, VALUE_INPUT[0])

    # print(filtered_list)
    display_list = display_characters(filtered_list)
    service.list_to_filter = filtered_list
    # print(display_list)
    await update.callback_query.message.edit_text(display_list)
    await update.callback_query.message.reply_text(text=second_criteria_text, reply_markup=dynamic_main_keyboard())
    return REPEAT_CRITERIA_FILTER


async def hide_previous_keyboard(update, context):
    await update.callback_query.message.edit_text(success_message)
