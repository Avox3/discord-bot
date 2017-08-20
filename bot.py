import asyncio
import discord

import logging


logger = logging.getLogger('logger.json')

TOKEN = 'MzQ3MzA3NTU5NTQ1NDcwOTc3.DHWtnQ.VPnwsznaHhlKx2g8URs4VgEAWCw'

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    logger.info('Bot is starting...')


@client.event
async def on_message(message):

    logger.info('Bot is working...')

    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

client.run(TOKEN)

logger.info('Bot is starting...')
