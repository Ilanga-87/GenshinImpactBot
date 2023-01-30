#TODO write text for descriptions; ru version; add all chars

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
    "Select the element you need. If you want to back to start choice, press BACK button",
    "Select the weapon you need. If you want to back to start choice, press BACK button",
    "Select the rarity you need. If you want to back to start choice, press BACK button",
    "Select the region you need. If you want to back to start choice, press BACK button",
]
"""
Select the element you need. If you want to back to start choice, press BACK button
"""
success_message = """
Ok, let's go farther
"""
empty_list_message = """
Characters not found
"""

help_text = """
You can control me by /filter command.
"""

undefined_command_text = """
Sorry, I didn't understand that command. May be /help can be useful for you.
"""