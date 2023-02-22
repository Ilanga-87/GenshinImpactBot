about_bot = """
The bot that will help you to filter Genshin Impact characters by Element, Weapon, Rarity and Region.
"""

description = """
Simple bot that can filter Genshin Impact characters by Element, Weapon, Rarity and Region. 
Has only control command /filter.
Have fun!
"""

welcome_text = """
Hi! I will filter for you Genshin Impact characters. Every filtration can have 2 criterion. E.g., Element and Weapon.
Of course, when the amount of characters will be more then 100, I will add more filter steps :)
My main command is /filter. Also you can look at /help.
"""

first_criteria_text = """
Here you can choose the first option to filter all Genshin Impact characters by:
"""

second_criteria_text = """
Here you can choose the second option to filter all Genshin Impact characters by:
"""

# TODO Instead of change the whole phrase find an approach to change only variables with words
value_choice_text = [
    "Select the element you want to filter characters by:",
    "Select the weapon you want to filter characters by:",
    "Select the rarity you want to filter characters by:",
    "Select the region want to filter characters by:",
]

success_message = """
Ok, let's go farther
"""

criteria_choice_message = "Your {} criteria is {}."
value_choice_message = "You selected {}"

amount_of_chars = "You want to see filter by {} {} {} {}. I found {} characters: "

empty_list_message = """
Characters not found
"""

help_text = """
You can control me by /filter command.
"""

undefined_command_text = """
Sorry, I didn't understand that command. May be /help can be useful for you.
"""
