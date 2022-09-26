import discord
from discord.ext import commands
import os
import json

bot = commands.Bot(command_prefix = "!")
dirPath = os.path.dirname(os.path.realpath(__file__))

async def is_owner(ctx):
    return (ctx.author.id == 451112923671035904)


bot.remove_command("help")


bot.load_extension(f"cogs.ready")
bot.load_extension(f"cogs.good")

@bot.command()
@commands.check(is_owner)
async def load(ctx, extension):
    try:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"{ctx.author.mention} Successfully loaded {extension}")
    except: await ctx.send(f"{ctx.author.mention} No such extension.")

@bot.command()
@commands.check(is_owner)
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f"{ctx.author.mention} Successfully unloaded {extension}")
    except: await ctx.send(f"{ctx.author.mention} No such extension.")

#==================== Errors ====================#

@load.error
async def load_error(ctx, error):
  if isinstance(error, (commands.CommandError)):
    await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

@unload.error
async def unload_error(ctx, error):
  if isinstance(error, (commands.CommandError)):
    await ctx.send(f"{ctx.author.mention} You are not allowed to use owner commands.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, (commands.MissingRequiredArgument)):
        await ctx.send(f"{ctx.author.mention} Please input all necessary parameters")
    elif isinstance(error, (commands.CommandNotFound)):
        await ctx.send(f"{ctx.author.mention} Command '{ctx.message.content}' not found. Please type a valid command.")
    else: raise error

bot.run('ODM1NDk4NTEzNTI5MTc2MDc1.YIQUoA.9P4zJFt_o5SUKOM9e8LbyYaFsQw')