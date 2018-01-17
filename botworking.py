import discord
import asyncio
import feedparser
import unidecode
from pypubg import core
from time import sleep
client = discord.Client()
channel = discord.Object(id='')
async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='')
    rss = 'https://www.reddit.com/r/funny/new/.rss?limit=1'
    temp=''
    feed = feedparser.parse(rss)
    for key2 in feed["entries"]:
        temp = unidecode.unidecode(key2["link"])
    while not client.is_closed:
        counter += 1
        feed = feedparser.parse(rss)
        for key1 in feed["entries"]:
            main=unidecode.unidecode(key1["link"])
            if(not temp==main):
                await client.send_message(channel, ':alien:'+ '`New post from reddit-`'+'\n'+'**'+unidecode.unidecode(key1["title"]+'**'+'\n'+unidecode.unidecode(key1["link"])))
                temp=main
            else:
                print("No new feed-")
        await asyncio.sleep(30) # task runs every 30 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Reddit feed'))
@client.event
async def on_message(message):
    if message.content.startswith('!pubg'):
        msg=message.content[6:]
        for x in range(0,len(msg)):
            if msg[x]==' ':
                name=msg[:x]
                region=msg[x+1:len(msg)]
client.loop.create_task(my_background_task())
client.run('')
