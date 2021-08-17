import os
import random
from typing import List
from dotenv import load_dotenv

import discord as dc
from discord.ext import commands as cmds
from discord.ext.commands import Context as Ctx
from discord import Status, Game, Reaction, User

import text2score as t2s_m
import weather.weather_fram_command as w
import weather.weather_plot_command as wp
import weather.weather_embed as we
import buffer_command as buf
import buffer_embed as bufeg
from cat import cat as cat_m
from pac import pac as pac_m
from amd import amd as amd_m

load_dotenv()

bot = cmds.Bot(command_prefix=['!D ', '!Deemo '])


@bot.event
async def on_ready():
    await bot.change_presence(status=Status.online, activity = Game(name="人生"))
    print('-----機器人已上線-----\n機器人名稱:', bot.user)


@bot.event
async def on_message(message: dc.Message):
    # ignore bot messages
    if message.author.bot: return
    # AMD YES by Miso
    if message.content == 'AMD':
        await message.channel.send('Yes!')
    # https://stackoverflow.com/questions/49331096/why-does-on-message-stop-commands-from-working
    await bot.process_commands(message)


# Repeats what you says.
@bot.command(aliases=['e'])
async def echo(ctx: Ctx, *, arg: str):
    await ctx.send(arg)


# Lilypond to PNG by Deemo, Nebula, PAC
@bot.command(aliases=['t2s'])
async def text2score(ctx: Ctx, *, arg: str):
    await t2s_m.lily(ctx, arg)


# 可愛ㄉ貓咪，不看ㄇ by Deemo & Nebula
@bot.command()
async def cat(ctx: Ctx, *, arg: str):
    await cat_m(ctx, arg)


# 無情葉配！土鳳梨酥！！ by xiaojie
@bot.command(aliases=['土鳳梨酥'])
async def pac(ctx: Ctx):
    await pac_m(ctx)


# 無情葉配！土鳳梨酥！！ by Miso
@bot.command(aliases=['無情業配'])
async def amd(ctx: Ctx):
    await amd_m(ctx)


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

# Chemistry!!! by Nebula
@bot.command(aliases=['buf'])
async def buffer(ctx: Ctx, *args: List[str]):
    await buf.buffer(ctx, args)


@bot.command(aliases=['bufeg'])
async def buffer_eg(ctx: Ctx):
    await bufeg.buffer_eg(ctx)


# Have a hard time making a decision? by Deemo
@bot.command()
async def decision(ctx: Ctx, *, arg: str):
    options = arg.split(",")
    await ctx.send(random.choice(options))


# The Core of Deemo Bot by xiaojie & Deemo
@bot.command()
async def deemo(ctx: Ctx, *, arg: str):
    await ctx.send('<@351754768118710272> 請彈奏 ' + arg)


@bot.event
async def on_reaction_add(_: Reaction, user: User):
    if user.bot: return


bot.run(os.getenv("TOKEN"))
