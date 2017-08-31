"""
    TODO - add time event for lunch and tea
    TODO - send klala every hour
    TODO - urban dictionary
    TODO - something with havura shel batlanim
    TODO - voice : OSSAS, SAX GUY, OK-OK-OK
"""

import inspect
import random
import sys
import requests
import json

from foaas import fuck

from db import setup_connection, add_row, get_random_row


connection = setup_connection()
cur = connection.cursor()


def add_emoji(emoji_name, img_path):
    """
    This function adds an emoji.

    :param emoji_name: emoji's name.
    :param img_path: image's path, isn't local.
    """

    pass


def commands():
    """This function returns the bot's commands."""
    curr_module = sys.modules[__name__]
    return [command[0] for command in inspect.getmembers(curr_module, inspect.isfunction)]


def search(query, long_param=True):
    """This function googles by query. """
    pass


def cookie_clicker():
    """This function increases cookie clicker by 1."""
    pass


def gal_quote():
    """This function sends a random quote by Gal."""
    row = get_random_row(cur, 'quotes')
    if row:
        return row.quote
    return "No QUOTE FROM GAL"


def add_quote(user, quote, long_param=True):
    """This function adds a quote, allowed only to Gal."""
    if "GAL" not in [role.name for role in user.roles]:
        return "You are not GAL!"

    add_row(cur, 'quotes', {'quote': quote})
    return "Quote added :)"


def ossas():
    """This function sends the name of ossas."""
    return "uvuvwevwevweonyetenyevwUgwemubwenOSSAS."


def urban(query, long_param=True):
    """
    This function returns the first search result from Urban Dictionary
    by the query.
    The search result includes definition and example.
    :param query:
    :return:
    """
    try:
        url = "http://api.urbandictionary.com/v0/define?term={}".format(query)
        request = requests.get(url)
        data = json.loads(request.text)
        if data['result_type'] == "exact":
            raw_output = "Definition:\n" + data['list'][0]['definition'] + "\nExample:\n" + data['list'][0]['example']
            return raw_output
        else:
            return "There is no definition for {} in Urban Dictionary".format(query)
    except ConnectionError as e:
        print(e.message)


def fuck_you(user, person):
    """
    This function returns a random fuck off message to a name
    from the called user.
    :param user:
    :param person:
    :return:
    """
    return fuck.random(name=person, from_=user.name).text


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
            manual += "__**{0}**__".format(name)
            manual += func.__doc__

        return manual
