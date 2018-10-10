"""This Module contains basic functions that I use in various programs"""

# Variable Definitions

__version__ = "Alpha"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
__email__ = "rodrigo.mcuadrada@gmail.com"
__license__ = "MIT"
__date__ = "9th of August 2017"

# functions


def cls():
    """This function clears the shell screen"""
    print("\n" * 50)


def pause():
    """This function pauses the program until the user presses enter key"""
    input("PRESS ENTER TO CONTINUE...")


def confirm():
    """This Function asks user for confirmation"""
    confirmation = input("Do you wish to confirm? Y-N: ")
    if confirmation[0].lower() == "y":
        return True
    print("Confirmation Failed!")
    return False


def int_input(prompt="Text for prompt"):
    """This function prompts for an integer, and loops until it gets one"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input not a valid integer, please try again...")
