import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!ar" , intents=intents)

@bot.event 
async def on_ready():
    print(f'We have logged in as {bot.user.name}') 

@bot.command()
async def addie(ctx):
    
    await ctx.send('Im running from Addies computer, hello')

@bot.command(name='8ball')
async def magic_ball(ctx, *, question: str = None):
    if not question:
        await ctx.send(" You didn't send a message! Try again!")
        return 
    responses = [
        "Absolutely not",
        "It will happen", 
        "Yes!",
        "There is a possiblity that it will happen",
        "You are delusional"
    ]
    response = random.choice(responses)
    await ctx.send(f'Question: {question}\n:8ball: Answer: {response}')

snipes = {}

@bot.event
async def on_message_delete(message):
    global snipes 
    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'message' : message.content,
        'snipee_id' : message.author.id
    }
    print(f'{message.author} just sent {message.content} and it was sent to the snipees dictionary')
    print(f'{snipes}')


bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')