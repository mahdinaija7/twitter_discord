import tweepy as tp
import discord
from time import sleep
import asyncio

dicord_token="your token"

consumer_key= 'yourkeyhere'
consumer_secret= 'yourkeyhere'
access_token= 'yourkeyhere'
access_token_secret= 'yourkeyhere'

auth=tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tp.API(auth)

client=discord.Client()
discord_channel_id='channel id '
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    sleep(0.5)
    print('BOt is Ready!')

@client.event
async def on_message(message):
    if message.author != client.user and str(message.channel.id) ==discord_channel_id :
        api.update_status(status=message.content)


async def main_func():
    await client.start(dicord_token, bot=False)


asyncio.get_event_loop().run_until_complete(main_func())