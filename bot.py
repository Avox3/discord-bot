import asyncio
import discord
import inspect
import logging

import commands


TOKEN = open('settings/tokens.txt', 'r').read().split('\n')[0]

logger = logging.getLogger('logger.json')
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    logger.info('Bot is ready...')


@client.event
async def on_message(message):

    logger.info('Bot is working...')

    if message.content.startswith('!bot'):

        arguments = message.content.split()[1:]  # get arguments

        if not arguments:  # no command
            return

        command_name = arguments[0]
        func = getattr(commands, command_name)

        # not a valid command, function doesn't exist
        if not func:
            return

        arguments = arguments[1:]  # function arguments
        required_args = inspect.getargspec(func)[0]

        if 'long_param' in required_args:
            arguments = [" ".join(arguments)]

        # add user as argument
        if 'user' in required_args:
            arguments = [message.author] + arguments

        response = func(*arguments)
        await client.send_message(message.channel, response)  # send response

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)

client.run(TOKEN)
logger.info('Bot is starting...')
