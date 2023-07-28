import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!bc ", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command()
async def ben(ctx):
    await ctx.send('Theres children in the basement of this server, contact michael for more informaition')


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


@bot.command(name='8ball')
async def magic_ball(ctx, *, question : str = None):

    if not question:
        await ctx.send("You did not send a message. Try again!")
        
    responses = [
        "absolutely not.",
        "it is certan",
        "no way jose.",
        "Yes!",
        "Not even a little bit",
    ]
    response = random.choice(responses)
    await ctx.send(f'Question {question}\n:8Ball: Answer: {response}')

bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')

