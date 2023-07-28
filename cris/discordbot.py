import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!cm ", intents=intents)

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user.name}')

@bot.command()
async def cris_m(ctx):
    await ctx.send('Testing testing, Cristiano > Messi')

@bot.command(name='8ball')
async def magic_ball(ctx, *, question: str = None):
    if not question:
        await ctx.send("you did not send a message! try again")
        return
    responses = {
        "Absolutely not.",
         "it is certain.",
        "no way, jose.",
        "yes!",
        "death!",
        "Nope! not even a little bit"
    }
    response = random.choice(responses)
    await ctx.send(f' Question: {question}\n:8ball: answer: {response}')


snipes = {}

@bot.event
async def on_message_delelte(message):
    global snipes
    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'message' : message.content,
        'snipee_id' : message.author.id
    }
    print(f'{message.author} just sent {messsge.content} and it was saved to the snipes dict.')


bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')