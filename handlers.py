import service
import keyboards
from service import (
    CRITERIA_INPUT, VALUE_INPUT,
    get_characters, display_characters, clear_pressed_button,
    CRITERIA_FILTER, VALUE_FILTER, REPEAT_CRITERIA_FILTER, END
)
from keyboards import dynamic_main_keyboard, value_keyboards_list
from static_text import (
    welcome_text, success_message, first_criteria_text, second_criteria_text, value_choice_text, help_text
)


async def start(update, context):
    text = welcome_text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def start_filter(update, context):
    keyboards.possible_main_kb_buttons_in_list = list(keyboards.possible_main_kb_buttons_tuple)[:]
    service.list_to_filter = service.all_chars_list[:]
    await update.message.reply_text(text=first_criteria_text, reply_markup=dynamic_main_keyboard())
    return CRITERIA_FILTER


async def criteria_filter(update, context):
    await hide_previous_keyboard(update, context)
    pointer = int(update.callback_query["data"].split(".")[-1])
    CRITERIA_INPUT[0] = pointer
    reply_text = value_choice_text[pointer]
    reply_keyboard = value_keyboards_list[pointer]
    clear_pressed_button(keyboards.possible_main_kb_buttons_in_list, pointer)
    await update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_keyboard)
    return VALUE_FILTER


async def value_filter(update, context):
    VALUE_INPUT[0] = update.callback_query["data"].split(".")[-1]
    filtered_list = get_characters(service.list_to_filter, CRITERIA_INPUT[0] + 1, VALUE_INPUT[0])
    display_list = display_characters(filtered_list)
    service.list_to_filter = filtered_list
    await update.callback_query.message.edit_text(display_list)
    if len(keyboards.possible_main_kb_buttons_in_list) > 2:
        await update.callback_query.message.reply_text(text=second_criteria_text, reply_markup=dynamic_main_keyboard())
        return REPEAT_CRITERIA_FILTER
    return END


async def hide_previous_keyboard(update, context):
    await update.callback_query.message.edit_text(success_message)


async def helper(update, context):
    text = help_text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
