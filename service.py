from operator import itemgetter
from telegram.ext import ConversationHandler

import static_text
import button_text
from manage_data import elements_dict, weapon_dict, regions_dict

# Variables to filter characters
CRITERIA_INPUT = ["-100"]
VALUE_INPUT = [""]

# Variables for states in ConversationHandler
CRITERIA_FILTER = 0
REPEAT_MAIN_KB, VALUE_FILTER, REPEAT_CRITERIA_FILTER = range(2, 5)
END = ConversationHandler.END

# Holders
first_criteria_holder = ''
second_criteria_holder = ''
first_value_holder = ''
second_value_holder = ''

with open("data.csv", "r") as file:
    file.readline()
    data = file.readlines()
    all_chars_list = []

    for row in data:
        default_ordered_list = [item for item in row.strip().split(",")]
        default_ordered_list[1] = int(default_ordered_list[1])
        new_order = [0, 2, 3, 1, 4]
        ordered_list = [default_ordered_list[i] for i in new_order]
        all_chars_list.append(tuple(ordered_list))
        list_to_filter = all_chars_list[:]


def get_characters(char_list, criteria, value):
    result_list = []
    if len(char_list) > 0:
        for tpl in char_list:
            if str(tpl[criteria]).lower() == str(value).lower():
                result_list.append(tpl)
    sorted_by_alphabet = sorted(result_list)
    sorted_by_rarity = sorted(sorted_by_alphabet, key=itemgetter(3), reverse=True)
    return sorted_by_rarity


# Unused but possible useful
def display_characters(chars_list):
    if len(chars_list) < 1:
        return static_text.empty_list_message

    chars_in_strings = ""
    for char in chars_list:
        chars_in_strings += f"{char[0]} - {char[1]} - {char[2]} - {char[3]} - {char[4]} \n"
    return chars_in_strings


def display_characters_with_emoji(chars_list):
    if len(chars_list) < 1:
        return static_text.empty_list_message

    chars_in_strings_with_emoji = ""
    for char in chars_list:
        char_element = char[1].lower()
        char_weapon = char[2].lower()
        char_region = char[4].lower()
        chars_in_strings_with_emoji += f"➡️ {char[0]}  |  " \
                                       f"{elements_dict[char_element]}{char[1]}  |  " \
                                       f"{weapon_dict[char_weapon]}{char[2]}  |  {char[3]}  |  " \
                                       f"{regions_dict.get(char_region, '')}{char[4]} \n"
    return chars_in_strings_with_emoji


def clear_pressed_button(dctnary, btn):
    del dctnary[str(btn)]
    return dctnary


def tpl_to_dict(tpl):
    result_dict = {}
    for i, elem in enumerate(tpl):
        result_dict[str(i)] = elem
    return result_dict
