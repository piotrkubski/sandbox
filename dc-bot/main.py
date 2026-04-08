import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix= '!', intents=intents)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Nie znam takiej komendy... Jesteś pewien, że dobrze wpisałeś?")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Hej, zapomniałeś o argumentach!")
    else:
        print(f'Nieobsłużony błąd: {error}')

@client.event
async def on_ready():
    print('The bot is now ready for use!')
    print(30*'-')


@client.command()
async def hello(ctx):
    await ctx.send('Hello, I am Kevin')

client.run(TOKEN)