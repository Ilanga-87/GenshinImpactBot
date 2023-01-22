from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from button_text import (
    element, weapon, rarity, region,
    cryo, pyro, hydro, electro, geo, anemo, dendro,
    bow, sword, polearm, catalyst, claymore,
    rarity_4, rarity_5,
    mondstadt, li_yue, inazuma, sumeru,
    reset
)
from manage_data import TWO_TWO, NEW, ELEMENT_CHOICE, WEAPON_CHOICE, RARITY_CHOICE, REGION_CHOICE

reset_button = InlineKeyboardButton(reset, callback_data=f"{TWO_TWO}")


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
            InlineKeyboardButton(anemo, callback_data=f"{TWO_TWO}"),
            InlineKeyboardButton(electro, callback_data=f"{TWO_TWO}"),
        ],
        [
            InlineKeyboardButton(cryo, callback_data=f"{TWO_TWO}"),
            InlineKeyboardButton(pyro, callback_data=f"{TWO_TWO}"),
        ],
        [
            InlineKeyboardButton(geo, callback_data=f"{TWO_TWO}"),
            InlineKeyboardButton(dendro, callback_data=f"{TWO_TWO}"),
        ],
        [
            InlineKeyboardButton(hydro, callback_data=f"{TWO_TWO}"),
        ],
        [
            reset_button
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def weapon_keyboard():
    buttons = [
        [
            InlineKeyboardButton(bow, callback_data=f"{TWO_TWO}"),
            InlineKeyboardButton(polearm, callback_data=f"{TWO_TWO}")
        ],
        [
            InlineKeyboardButton(claymore, callback_data=f"{TWO_TWO}"),
            InlineKeyboardButton(catalyst, callback_data=f"{TWO_TWO}")
        ],
        [
            InlineKeyboardButton(sword, callback_data=f"{TWO_TWO}"),
        ],
        [
            reset_button
        ]
    ]
    return InlineKeyboardMarkup(buttons)


def rarity_keyboard():
    buttons = [
        [
            InlineKeyboardButton(rarity_4, callback_data=f"{TWO_TWO}"),
            InlineKeyboardButton(rarity_5, callback_data=f"{TWO_TWO}")
        ],
        [
            reset_button
        ]
    ]
    return InlineKeyboardMarkup(buttons)


def region_keyboard():
    buttons = [
        [
            InlineKeyboardButton(mondstadt, callback_data=f"{TWO_TWO}"),
            InlineKeyboardButton(li_yue, callback_data=f"{TWO_TWO}")
        ],
        [
            InlineKeyboardButton(inazuma, callback_data=f"{TWO_TWO}"),
            InlineKeyboardButton(sumeru, callback_data=f"{TWO_TWO}")
        ],
        [
            reset_button
        ]
    ]
    return InlineKeyboardMarkup(buttons)
