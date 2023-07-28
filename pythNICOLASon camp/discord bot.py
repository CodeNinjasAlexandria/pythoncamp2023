import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!nk* ", intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command()
async def nico(ctx):
    await ctx.send('I am running from nicos computer')

@bot.command()
async def death(ctx):
    await ctx.send('im dead')

@bot.command()
async def  laugh(ctx):
    await ctx.send('haha')

@bot.command(name='8ball')
async def  eightball(ctx, *, question:str = None):
    if not question:
        await ctx.send("You did not send a messsage. Try again!")
        return
    if str(question[:7]).lower() == 'testing':
        await ctx.send(f'Testing mode')
        return

    responses = [
        "Absolutely not",
        "It is certain",
        "No way, Jose",
        "Yes!",
        "Death!",
        "Nope! Not even a little bit"
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



