import discord
from discord.ext import commands
import random

intents =discord .intents.all()

bot = commands.bot(comands_prefix="&", intents=intents)

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user.name})
          
bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')