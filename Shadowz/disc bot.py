import discord 
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!jg ", intents=intents)

@bot.event 
async def on_ready():
    print(f'we have logged in as {bot.user.name}')

@bot.command()
async def jake(ctx):
    await ctx.send('I am running from Jakes commuter')

@bot.command( name='8ball')
async def magik_ball(ctx, *, question: str = None):
    if not question:
        await ctx.send("you did not send a message! TrY aGaIn")
        return 
    responses = [
        "absolutly not.",
        "no way, hose",
        "It is not certain",
        "Yes!",
        "kiss yourself goodbye",
        "not even a little bit"
    ]
    response = random.choice(responses)
    await ctx.send(f'question: {question}\n :8Ball: Answer: {response}')

snipes = {}

@bot.event
async def on_message_delete(message):
    global snipes
    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'message' : message.content,
        'snipee' : message.author.id
    }
    print (f'{message.author}xjust sent {message.content} and it was was save to the snipes dict.')

bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')