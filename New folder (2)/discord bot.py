import discord 
from discord.ext import commands
import random
intents = discord.Intents.all()


bot = commands.Bot(command_prefix= "!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have loggedin as {bot.user.name}')

@bot.command()
async def maclin(ctx):
    await ctx.send('I am running from maclins computer')

@bot.command(name= "AteBall")
async def ateball(ctx, *, question: str = None):
    if not question:
        await ctx.send("you didn't ask anything!")
        return
    responses =  [
        "Nope",
        "100%",
        "ehh maybe",
        "why are you even asking this",
        "Yep",
        "No",
        "Touch grass",
        "Why are you even asking this",
        "The voices.."
    ]
    response = random.choice(responses)
    await ctx.send(f'Question: {question}\n:8ball: {response} ')


snipes = {}


@bot.event
async def on_message_delete(message):
    global snipes
    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'message' : message.content, 
        'snipee_id' : message.author.id
    }
    print (f'{message.author}I just sent {message.content} and it was saved to snipes dict')

bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')

