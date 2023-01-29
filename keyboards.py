from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from button_text import (
    element, weapon, rarity, region,
    cryo, pyro, hydro, electro, geo, anemo, dendro,
    bow, sword, polearm, catalyst, claymore,
    rarity_4, rarity_5,
    mondstadt, li_yue, inazuma, sumeru,
    reset
)
from manage_data import (
    TWO_TWO, NEW, ELEMENT_CHOICE, WEAPON_CHOICE, RARITY_CHOICE, REGION_CHOICE,
    ELEMENT_VALUE, WEAPON_VALUE, RARITY_VALUE, REGION_VALUE, FILTER_VALUE, FILTER_CRITERIA,
    CRYO, PYRO, GEO, ANEMO, HYDRO, DENDRO, ELECTRO,
    SWORD, CATALYST, CLAYMORE, BOW, POLEARM,
    RARITY_4, RARITY_5,
    MONDSTADT, LI_YUE, INAZUMA, SUMERU,
    RESET
)

reset_button = InlineKeyboardButton(reset, callback_data=f"{RESET}")

main_menu_buttons_dict = {
    "element": ELEMENT_CHOICE,
    "weapon": WEAPON_CHOICE,
    "rarity": RARITY_CHOICE,
    "region": REGION_CHOICE,
    "reset": RESET,
}

main_menu_buttons_list = (
    ELEMENT_CHOICE,
    WEAPON_CHOICE,
    RARITY_CHOICE,
    REGION_CHOICE,
    RESET,
)

possible_main_kb_buttons = [
    InlineKeyboardButton(element, callback_data=f"{FILTER_CRITERIA}.{ELEMENT_CHOICE}"),
    InlineKeyboardButton(weapon, callback_data=f"{FILTER_CRITERIA}.{WEAPON_CHOICE}"),
    InlineKeyboardButton(rarity, callback_data=f"{FILTER_CRITERIA}.{RARITY_CHOICE}"),
    InlineKeyboardButton(region, callback_data=f"{FILTER_CRITERIA}.{REGION_CHOICE}"),
    InlineKeyboardButton(reset, callback_data=f"{RESET}")
]


def dynamic_main_keyboard():
    actual_main_kb_buttons = possible_main_kb_buttons[:4]
    return InlineKeyboardMarkup.from_column(actual_main_kb_buttons)


def elements_keyboard():
    buttons = [
        [
            InlineKeyboardButton(anemo, callback_data=f"{FILTER_VALUE}.{ANEMO}"),
            InlineKeyboardButton(electro, callback_data=f"{FILTER_VALUE}.{ELECTRO}"),
        ],
        [ 
            InlineKeyboardButton(cryo, callback_data=f"{FILTER_VALUE}.{CRYO}"),
            InlineKeyboardButton(pyro, callback_data=f"{FILTER_VALUE}.{PYRO}"),
        ],
        [
            InlineKeyboardButton(geo, callback_data=f"{FILTER_VALUE}.{GEO}"),
            InlineKeyboardButton(dendro, callback_data=f"{FILTER_VALUE}.{DENDRO}"),
        ],
        [
            InlineKeyboardButton(hydro, callback_data=f"{FILTER_VALUE}.{HYDRO}"),
        ],
        [
            reset_button
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def weapon_keyboard():
    buttons = [
        [
            InlineKeyboardButton(bow, callback_data=f"{FILTER_VALUE}.{BOW}"),
            InlineKeyboardButton(polearm, callback_data=f"{FILTER_VALUE}.{POLEARM}")
        ],
        [
            InlineKeyboardButton(claymore, callback_data=f"{FILTER_VALUE}.{CLAYMORE}"),
            InlineKeyboardButton(catalyst, callback_data=f"{FILTER_VALUE}.{CATALYST}")
        ],
        [
            InlineKeyboardButton(sword, callback_data=f"{FILTER_VALUE}.{SWORD}"),
        ],
        [
            reset_button
        ]
    ]
    return InlineKeyboardMarkup(buttons)


def rarity_keyboard():
    buttons = [
        [
            InlineKeyboardButton(rarity_4, callback_data=f"{FILTER_VALUE}.{RARITY_4}"),
            InlineKeyboardButton(rarity_5, callback_data=f"{FILTER_VALUE}.{RARITY_5}")
        ],
        [
            reset_button
        ]
    ]
    return InlineKeyboardMarkup(buttons)


def region_keyboard():
    buttons = [
        [
            InlineKeyboardButton(mondstadt, callback_data=f"{FILTER_VALUE}.{MONDSTADT}"),
            InlineKeyboardButton(li_yue, callback_data=f"{FILTER_VALUE}.{LI_YUE}")
        ],
        [
            InlineKeyboardButton(inazuma, callback_data=f"{FILTER_VALUE}.{INAZUMA}"),
            InlineKeyboardButton(sumeru, callback_data=f"{FILTER_VALUE}.{SUMERU}")
        ],
        [
            reset_button
        ]
    ]
    return InlineKeyboardMarkup(buttons)


value_keyboards_list = [elements_keyboard(), weapon_keyboard(), rarity_keyboard(), region_keyboard()]
