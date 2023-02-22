import service
import keyboards
from service import (
    CRITERIA_INPUT, VALUE_INPUT,
    get_characters, clear_pressed_button, display_characters_with_emoji, tpl_to_dict,
    CRITERIA_FILTER, VALUE_FILTER, REPEAT_CRITERIA_FILTER, END
)
from keyboards import dynamic_main_keyboard, value_keyboards_list
from static_text import (
    welcome_text, first_criteria_text, second_criteria_text,
    value_choice_text, help_text, undefined_command_text,
    criteria_choice_message, amount_of_chars, value_choice_message
)


async def start(update, context):
    text = welcome_text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def start_filter(update, context):
    service.first_criteria_holder, service.second_criteria_holder, service.first_value_holder, service.second_value_holder = "", "", "", ""
    keyboards.possible_main_kb_buttons_dict = tpl_to_dict(keyboards.possible_main_kb_buttons_tuple)
    service.list_to_filter = service.all_chars_list[:]
    await update.message.reply_text(text=first_criteria_text, reply_markup=dynamic_main_keyboard())
    return CRITERIA_FILTER


async def criteria_filter(update, context):
    pointer = int(update.callback_query["data"].split(".")[-1])
    await hide_previous_keyboard(update, context, pointer)

    CRITERIA_INPUT[0] = pointer
    reply_text = value_choice_text[pointer]
    reply_keyboard = value_keyboards_list[pointer]
    clear_pressed_button(keyboards.possible_main_kb_buttons_dict, pointer)
    await update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_keyboard)
    return VALUE_FILTER


async def value_filter(update, context):
    VALUE_INPUT[0] = update.callback_query["data"].split(".")[-1]
    if len(service.list_to_filter) < len(service.all_chars_list):
        service.second_value_holder = VALUE_INPUT[0]
    else:
        service.first_value_holder = VALUE_INPUT[0]

    filtered_list = get_characters(service.list_to_filter, CRITERIA_INPUT[0] + 1, VALUE_INPUT[0])
    display_list = display_characters_with_emoji(filtered_list)
    service.list_to_filter = filtered_list

    await update.callback_query.message.edit_text(value_choice_message.format(VALUE_INPUT[0].title()))
    await update.callback_query.message.reply_text(
        amount_of_chars.format(service.first_criteria_holder, service.first_value_holder.title(),
                               service.second_criteria_holder, service.second_value_holder.title(),
                               len(filtered_list)).replace("  ", "")
    )
    await update.callback_query.message.reply_text(display_list)
    if len(keyboards.possible_main_kb_buttons_dict) > 2:
        await update.callback_query.message.reply_text(text=second_criteria_text, reply_markup=dynamic_main_keyboard())
        return REPEAT_CRITERIA_FILTER
    return END


async def hide_previous_keyboard(update, context, pointer):
    headers = ["Element", "Weapon", "Rarity", "Region"]
    if len(service.list_to_filter) < len(service.all_chars_list):
        display_message = criteria_choice_message.format("second", headers[pointer])
        service.second_criteria_holder = headers[pointer]
    else:
        display_message = criteria_choice_message.format("first", headers[pointer])
        service.first_criteria_holder = headers[pointer]
    await update.callback_query.message.edit_text(display_message)


async def helper(update, context):
    text = help_text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


async def undefined_commands(update, context):
    text = undefined_command_text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
