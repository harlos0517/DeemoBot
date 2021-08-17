from translate import Translator
import discord
import os
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
'''用translate module翻譯成中文'''
load_dotenv()
TOKEN = getenv('TOKEN')

bot_1 = discord.Client()
bot = commands.Bot(command_prefix='!D')

@bot.command()
async def on_message(ctx,message):
    input = ctx.message.content
    if ctx.message.author == bot.user:
        return
   
    translator = Translator(to_lang="zh-TW")
    translation = translator.translate(input.replace("!D"," "))
    link = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'  +input.replace("!D"," ")
    await message.channel.send(translation + "  " + "link")

bot.run(TOKEN)