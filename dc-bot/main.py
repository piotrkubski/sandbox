import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix= '!', intents=intents)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Unknown Command')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing arguments')
    else:
        print(f'Error: {error}')

@client.event
async def on_ready():
    print('The bot is now ready for use!')
    print(30*'-')

@client.command()
async def hello(ctx):
    await ctx.send('Hello, I am Kevin')

@client.event
async def on_member_join(member):
    channel = client.get_channel(1491503862107078740)
    await channel.send('hello')

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1491503862107078740)
    await channel.send('bye')

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('You must be in a voice channel to run this command!')

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send('I left the voice channel')
    else:
        await ctx.send('I am not in a voice channel')

client.run(TOKEN)