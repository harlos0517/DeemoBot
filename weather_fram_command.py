'''
加上@bot.command()裝飾器正常運作的話可以回傳表格，其中產生圖表的function來自w.get_fram
'''
import discord
from os import remove as rm
import weather_big as w

# @bot.command()


async def weather(ctx, *, arg):
    await ctx.send(w.r[arg])
    try:
        await w.get_fram(arg)
    except Exception as e:
        print(e)
        # await ctx.send("failed to get picture")
    try:
        if w.get_fram(arg):
            with open('a_styled.png', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
                rm('a_styled.png')

            print(w.r[arg])
        else:
            await ctx.send("failed QQ")
    except Exception as e:
        print(e)
        # await ctx.send("failed")
