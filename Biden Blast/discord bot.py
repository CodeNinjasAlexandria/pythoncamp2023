import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!ms ", intents=intents)

@bot.event
async def on_ready():
    print(f'we have loggged in as {bot.user.name}')

@bot.command()
async def Madsen(ctx):
    await ctx.send('I am running from Madsens computer')

@bot.command(name='8ball')
async def magic_ball(ctx, *, questoin: str = None):
    if not questoin:
        await ctx.send("You did not send a message! try agian")
        return
    respones = [
        "absolutely not.",
        "It is certain",
        "nah its joever",
        "Yes!",
        "no goobber",
        "Nope! not even a little bit",
        "yeah"

    ]

    response = random.choice(respones)
    await ctx.send(f'questoin: {questoin}\n:8ball: Ansewer: {response}')

snipes = {}

@bot.event
async def on_message_delete(message):
    global snipes 
    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'message' : message.content,
        'snipee_id' : message.author.id
    }
    print(f'{message.author} justsent {message.content} and it was saved to the snipes dict.')


bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')