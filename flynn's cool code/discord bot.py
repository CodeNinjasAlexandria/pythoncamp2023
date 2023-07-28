import discord
from discord.ext import commands
import random

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!FB ", intents=intents)

@bot.event
async def on_ready():

    print(f'we have logged in as {bot.user.name}')

@bot.command()
async def Flynn_Brophy(ctx):
    await ctx.send("I am running on Flynn's computer")

@bot.command(name="8ball")
async def magic_ball(ctx, *, question: str = None):
    if not question:
        await ctx.send("you did not send a message! try again")
        return
    responses = [
        'absolutley not', 
        'you should do that',
        'definetly do not',
        'yes',
        'no',
        'you should totally do that',
        'no, no, no',
        'nope, nope, do not',
        'yes, yes, do it, do it'
    ]
    response = random.choice(responses)
    await ctx.send(f'question: {question}\n:8ball: answer: {response}')

snipes = {}
@bot.event
async def on_message_delete(message):
    global snipes
    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'message' : message.content,
        'snipee_id' : message.author.id
    }
    print(f'{message.author} just sent {message.content} and it was saved to the snipes dic')
    


bot.run('MTEzMzQxMDY3MTkxMzA3NDc3MA.G6o8di.y6uuxeqRxBxdPU9_2-Dc_RTRuJTfAmJnmdRrxs')