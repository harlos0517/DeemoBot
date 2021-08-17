import discord as dc
from discord.ext.commands import Context as Ctx

async def pac(ctx: Ctx):
    embed = dc.Embed(title="土鳳梨酥", url="https://youtu.be/HM3PnOEJ1jI", description="阿就土鳳梨酥阿!", color=0x11ff00)
    embed.set_thumbnail(url="https://www.pineappletown.com.tw/upfiles/tw_product11523519466.jpg")
    embed.add_field(name="這部影片究竟要業配什麼東西呢?", value=
     """一、是貝卡斯穿的這件感覺魯魯的T-Shire
        二、是遊戲潮流的項鍊
        三、還是這張看起來很稀有的遊戲王卡
        四、亦或是後面這盒鳳梨小鎮的土鳳梨酥
        喔喔~土鳳梨酥!!!""",
    inline=True)
    await ctx.send(embed=embed)
