import os
from dotenv import load_dotenv

import discord as dc
from discord.ext import commands as cmds
from discord.ext.commands import Context as Ctx
from discord import Status, Game, Reaction, User

import text2score as t2s_m
import weather.weather_fram_command as w
import weather.weather_plot_command as wp
import weather.weather_embed as we
# import plot_test2
# import dic_mix
# import p
# import decision
from cat import cat as cat_m
from pac import pac as pac_m
# import deemo_bot

load_dotenv()

bot = cmds.Bot(command_prefix=['!D ', '!Deemo '])


@bot.event
async def on_ready():
    await bot.change_presence(status=dc.Status.online, activity = dc.Game(name="人生"))
    print('-----機器人已上線-----\n機器人名稱:', bot.user)


@bot.event
async def on_message(message: dc.Message):
    if message.author.bot: return
    await bot.process_commands(message)
    # https://stackoverflow.com/questions/49331096/why-does-on-message-stop-commands-from-working


# Repeats what you says.
@bot.command(aliases=['e'])
async def echo(ctx: Ctx, *, arg: str):
    await ctx.send(arg)


# Lilypond to PNG by Deemo, Nebula, PAC
@bot.command(aliases=['t2s'])
async def text2score(ctx: Ctx, *, arg: str):
    await t2s_m.lily(ctx, arg)


# 可愛ㄉ貓咪，不看ㄇ
@bot.command()
async def cat(ctx: Ctx, *, arg: str):
    await cat_m(ctx, arg)


# 無情葉配！土鳳梨酥！！
@bot.command(aliases=['土鳳梨酥'])
async def pac(ctx: Ctx):
    await pac_m(ctx)


# WEATHER BOT by NEBULA
@bot.command(aliases=['w'])
async def weather(ctx: Ctx, *, arg: str):
    await w.weather(ctx, arg)


@bot.command(aliases=['wp'])
async def weather_plot(ctx: Ctx):
    await wp.plot(ctx)


@bot.command(aliases=['we'])
async def weather_explane(ctx: Ctx):
    await we.weather_explane(ctx)


@bot.event
async def on_reaction_add(_: Reaction, user: User):
    if user.bot: return


bot.run(os.getenv("TOKEN"))
