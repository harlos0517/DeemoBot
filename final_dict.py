def translate_text( text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language="zh-TW")

    #print(u"Text: {}".format(result["input"]))
    #print(u"Translation: {}".format(result["translatedText"]))
    #print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return result["translatedText"] 
#a = input()
#out_put= translate_text(a)
#print(out_put)


#from translate import Translator
import discord
import os
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv



'''用translate module翻譯成中文'''
load_dotenv()
TOKEN = getenv('TOKEN')

bot_1 = discord.Client()
bot = commands.Bot(command_prefix='!Dd')

@bot.event
async def on_message(message):
    input = message.content
    if message.author == bot.user:
        return
   
    translator = translate_text(input.replace("!Dd"," "))
    
    link = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'  +input.replace("!D"," ")
    await message.channel.send(translator + "  " + "link")

bot.run(TOKEN)