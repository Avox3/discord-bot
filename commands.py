
COMMANDS = ['dickpick', 'add-emoji',
            'search', 'cookie-clicker',
            'klala', 'gal-quote', 'gal-add-quote',
            '']


def bot_help(*args):
    """

    """

    if args:
        pass
    else:
        for command in COMMANDS.items():
            func = locals[command]
            print(func.__doc__)
