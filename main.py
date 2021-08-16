import discord as dc
from discord.ext import commands

import os
from dotenv import load_dotenv

# import text2score as t2s_m
# import dict_game
# import popcat
# import decision
# import pineapple_cake
# import deemo_bot

load_dotenv()

bot = commands.Bot(command_prefix=['!D ', '!Deemo '])


@bot.event
async def on_ready():
    print("機器人 Start", bot.user)


@bot.event
async def on_message(message: dc.Message):
    if message.author.bot: return
    await bot.process_commands(message)
    # https://stackoverflow.com/questions/49331096/why-does-on-message-stop-commands-from-working


@bot.command(aliases=['e'])
async def echo(ctx: commands.Context, *, arg: str):
    await ctx.send(arg)


# @bot.command(aliases=['t2s'])
# async def text2score(ctx: commands.Context, *, arg: str):
    # t2s_m.Lily(ctx, arg)


@bot.event
async def on_reaction_add(reaction: dc.reaction, user: dc.User):
    if user.bot: return


bot.run(os.getenv("TOKEN"))
