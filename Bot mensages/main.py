import os
import discord
from discord.ext import commands
from credentials import secrets

intents = discord.Intents.default()
intents.message_content = True

api_key = secrets.get('API_KEY')

bot = commands.Bot(command_prefix='/', intents=intents)

 
@bot.command()   
async def oi(ctx):
    await ctx.send('eai')
        
bot.run(api_key)