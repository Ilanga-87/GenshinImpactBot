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
    ELEMENT_VALUE, WEAPON_VALUE, RARITY_VALUE, REGION_VALUE, FILTER_VALUE,
    CRYO, PYRO, GEO, ANEMO, HYDRO, DENDRO, ELECTRO,
    SWORD, CATALYST, CLAYMORE, BOW, POLEARM,
    RARITY_4, RARITY_5,
    MONDSTADT, LI_YUE, INAZUMA, SUMERU,
    RESET
)

reset_button = InlineKeyboardButton(reset, callback_data=f"{RESET}")


def main_keyboard():
    buttons = [
        [InlineKeyboardButton(element, callback_data=f"{ELEMENT_CHOICE}"),
         InlineKeyboardButton(weapon, callback_data=f"{WEAPON_CHOICE}")],
        [InlineKeyboardButton(rarity, callback_data=f"{RARITY_CHOICE}"),
         InlineKeyboardButton(region, callback_data=f"{REGION_CHOICE}")
         ]]
    return InlineKeyboardMarkup(buttons)


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
