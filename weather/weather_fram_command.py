
from os import remove as rm
import discord
from discord.ext.commands import Context as Ctx

import weather.weather_big as w_big

async def weather(ctx: Ctx, arg: str):
    '''
    回傳表格，其中產生圖表的function來自w.get_fram
    '''
    await ctx.send(w_big.r[arg])
    try:
        w_big.get_fram(arg)
    except Exception as e:
        print(e)
        # await ctx.send("failed to get picture")
    try:
        with open('a_styled.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
            rm('a_styled.png')
        print(w_big.r[arg])
    except Exception as e:
        print(e)
        # await ctx.send("failed")
