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


#以上為函式設計


#from translate import Translator
import discord
import os
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv


#以上為import module



load_dotenv()
TOKEN = getenv('TOKEN')

bot_1 = discord.Client()




@bot.event
async def on_message(message):
    input = message.content
    #if message.author == bot.user:
        #return
    if message.content == prefix + "dic":
        if message.content.count(" ") > 5:
            await message.send("最多五個字")
            return

        else:
            translator = translate_text(input.replace("!Dd"," "))

            try:
                link = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'  +input.replace("!D"," ")
                record_dict = {}
                record_dict[translator] = input
                await message.channel.send(translator + "  " + "link")

            except:
                await message.send("failure")


    
    




bot.run(TOKEN)