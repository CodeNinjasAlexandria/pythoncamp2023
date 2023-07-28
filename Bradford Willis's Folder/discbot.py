import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!nk ", intents=intents) 

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user.name}')

@bot.command()
async def bradford(ctx):
    await ctx.send("Hi")

@bot.command(name='8ball')
async def magic_ball(ctx, *, question: str = None):
    if not question:
        await ctx.send("You did not send a message! Try again!")
        return
    responses =[
        "Not",
        "It Is certain.",
        "No Way, jose."
        "Yes!",
        "Death",
        "Nope! Not Even a litte bit"
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
    print(f'{message.author} just sent {message.content} and it was saved to the snipes dict.')

    
bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')