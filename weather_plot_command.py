'''
加上@bot.command()裝飾器正常運作的話可以回傳圖表，其中產生圖表的function來自plot_test2
'''
import plot_test2
import discord
from os import remove as rm
# @bot.command()


async def plot(ctx):
    try:
        if plot_test2.get_plot():
            with open('plot.png', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
                rm('plot.png')
        else:
            pass
            # await ctx.send("failed")
    except:
        pass
        # await ctx.send("failed")
