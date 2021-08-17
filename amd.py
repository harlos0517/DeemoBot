from discord.ext.commands import Context as Ctx
from discord import Embed, Colour

async def amd(ctx: Ctx):
    embed = Embed(
        title='AMD Where The Future Starts',
        colour=Colour(0xE5E242),
        url='https://youtu.be/PJbomsA8b38',
        description='準備好使用 Radeon RX 6600 XT 顯示卡，​體驗前所未有的 1080p 遊戲效能。'
    )
    embed.set_image(url='https://inside-assets1.inside.com.tw/2021/5/jvs3gwkmljd9sxyu6xqp87tmckcs3q.jpg?w=1200&h=630&fit=crop&q=80')
    await ctx.send(embed=embed)