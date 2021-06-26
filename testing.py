import discord
import asyncio
import os
#import search_site
from dotenv import load_dotenv
load_dotenv()

# instantiate discord client
client = discord.Client()

# discord event to check when bot is online
@client.event
async def on_ready():
    print(f'{client.user} is now online!')

@client.event
async def on_message(message): 
  # so bot dosen't respond to itself
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  
  
  if message.content.startswith(f'$hello'):
    await message.channel.send('''Hello there i'm the Seeking Alpha Scraping Bot. I was made by ReZa to scrape fast and eat ass!''')


client.run(os.getenv('TOKEN'))