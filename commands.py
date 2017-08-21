"""
    TODO - add time event for lunch and tea
    TODO - send klala every hour
    TODO - something with havura shel batlanim
"""

import inspect
import random
import sys

from data import DICKPICKS, OSSAS


def add_emoji(emoji_name, img_path):
    """
    This function adds an emoji.

    :param emoji_name: emoji's name.
    :param img_path: image's path, isn't local.
    """

    pass


def search(query):
    """This function googles by query. """
    pass


def cookie_clicker():
    """This function increases cookie clicker by 1."""
    pass


def gal_quote():
    """This function sends a random quote by Gal."""
    pass


def gal_add_quote(quote):
    """This function adds a quote, allowed only to Gal."""
    pass


def ossas():
    """This function sends the name of ossas."""
    return OSSAS


def dickpick():
    """This function returns a random ascii dickpick."""
    return random.choice(DICKPICKS)


def bot_help(*args):
    """This function sends commands' docs."""

    if args:  # more specific command
        pass

    else:  # general command

        curr_module = sys.modules[__name__]
        functions = inspect.getmembers(curr_module, inspect.isfunction)

        manual = ""
        for name, func in functions:
            manual += "\n\n"
            manual += repr(name)
            manual += '\t' + func.__doc__

        return manual
