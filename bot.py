import asyncio
import discord
import logging
from rq import Queue

from commands import COMMANDS


logger = logging.getLogger('logger.json')

TOKEN = 'MzQ3MzA3NTU5NTQ1NDcwOTc3.DHWtnQ.VPnwsznaHhlKx2g8URs4VgEAWCw'


TEST_DICT = {'help': help_bot}

# TODO - add time event for lunch and tea
# TODO - send klala every hour

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

        arguments = message.content.split()[1:]

        if no arguments:
            bot_help()
            return

        command = arguments[0]

        if command in TEST_DICT:
            TEST_DICT[command]()
        else:
            bot_help()
            return

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(TOKEN)

logger.info('Bot is starting...')
