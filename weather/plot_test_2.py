'''
裡面含有要被import的東東
'''
from discord.ext.commands import Context as Ctx
from os import remove as rm
import discord as dc
import matplotlib.pyplot as plt
import seaborn as sns
from weather.weather_big import Bframe
# plt.savefig('filename.jpg')

# 重要 不能刪
#
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False
sns.set(font='SimHei', font_scale=0.8)
tips = Bframe
g = sns.relplot(x="時間", y="降雨機率(%)", hue="地點", size="相對濕度(%)", data=tips)
plt.gcf().set_size_inches(10, 5)
g.fig.autofmt_xdate()


async def get_plot():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
    plt.rcParams['axes.unicode_minus'] = False
    sns.set(font='SimHei', font_scale=0.8)
    tips = Bframe
    g = sns.relplot(x="時間", y="降雨機率(%)", hue="地點",
                    size="相對濕度(%)", data=tips)
    plt.gcf().set_size_inches(10, 5)
    g.fig.autofmt_xdate()
    plt.savefig('plot.png')


# 重要 不能刪
async def plot(ctx: Ctx, arg: str):
    try:
        if get_plot():
            with open('plot.png', 'rb') as f:
                picture = dc.File(f)
                await ctx.send(file=picture)
                rm('plot.png')
        else:
            await ctx.send("failed")
    except:
        await ctx.send("failed")
