import discord
from discord.ext import commands
import random

intents = discord.intents.all()

bot = commands.Bot(commands_prefix="!mc ",  intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command()
async def mateo(ctx):
    await ctx.send("I am running on Mateo's computer")

@bot.command(name = 'eightball')
async def magic_ball(ctx, *, question: str = None ):
    if not question:
        await ctx.send("you did not a menssage! Try again")
    return
    responses = [
        "Absolutely not." ,
        "It is certain" ,
        "No way, jose" ,
        "yes!" ,
        "Death!" ,
        "Nope! Not even a litlle bit"
    ]

    response = random.choice(responses)
    await ctx.send(f'question: {question}\n:eightball: answer: {responsed }')

snipes ={}

bot.event
async def on_message_delete(message):
    global snipes
    chanel_id = str(message.chanel.id)
    snipes[chanel_id] = {
        'message' : message.connect,
        'snipee_id' : message.athuor.id
    }
    print(f'{message.athuor} just sent {message.connect} and it was saved to the snipes dict.')
bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')