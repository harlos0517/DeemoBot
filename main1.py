import discord
from os import getenv, remove as rm
from discord import file
from dotenv import load_dotenv
from discord.ext import commands
from llily import lili_to_png
from mingus.extra import lilypond

bot = commands.Bot(command_prefix='!')


@bot.command()
async def sum(ctx: commands.Context, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)


@bot.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)


@bot.command()
async def Lily(ctx: commands.Context, *, arg: str):
    # https://www.python.org/dev/peps/pep-3102/
    try:
        if lilypond.to_png(arg, "temp.png"):
            with open("temp.png", 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
                rm("temp.png")
        else:
            await ctx.send("Conversion failed")
    except:
        await ctx.send("Conversion failed")


@bot.event
async def on_ready():
    print("目前登入身分", bot.user)  # print在terminal
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game("Himawari衛星")
                              )


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.split()[0] == "change":
        await bot.change_presence(
            activity=discord.Game(message.content.split()[1])
        )
    if message.content == "//"+"上山嗎":
        global reaction_msg
        reaction_msg = await message.channel.send("決定要去的按ㄍ愛心吧")
        await reaction_msg.add_reaction('❤️')
    if message.content == "笑":
        with open("smile.gif", 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
    await bot.process_commands(message)
    # https://stackoverflow.com/questions/49331096/why-does-on-message-stop-commands-from-working


@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return
    if reaction.message.id != reaction_msg.id:
        return
    if reaction.emoji == "❤️":
        role = discord.utils.get(user.guild.roles, id=876061510793834536)
        await user.add_roles(role)

load_dotenv()

TOKEN = getenv('TOKEN')
bot.run(TOKEN)
