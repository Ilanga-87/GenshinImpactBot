import static_text

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


def get_characters(char_list, criteria, value):
    result_list = []
    if len(char_list) > 0:
        for tpl in char_list:
            if str(tpl[criteria]).lower() == str(value).lower():
                result_list.append(tpl)
    return result_list


# Variables to filter characters
CRITERIA_INPUT = [""]
VALUE_INPUT = [""]


def display_characters(chars_list):
    if len(chars_list) < 1:
        return static_text.empty_list_message

    chars_in_strings = ""
    for char in chars_list:
        chars_in_strings += f"{char[0]} - {char[1]} - {char[2]} - {char[3]} - {char[4]} \n"
    return chars_in_strings