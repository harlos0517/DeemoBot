'''
在on_message之下呼叫這個function並傳入message，若message.content == "weather會回傳解釋weather的embede。
但不確定在on_message之下這樣做會不會有問題，若有，直接在on_message之下貼上if那一段。
'''
import discord
from discord.ext.commands import Context as Ctx


async def weather_explane(ctx: Ctx):
    embed = discord.Embed(
        title="weather相關Command 表", description="輸入command，順利的話會收到表格or圖表\n範例輸入1. !Dplot \n範例輸入2. !Dweather a \n註:merge到deemo bot之後要改範例輸入指令", color=0x98bee6)
    embed.set_author(
        name="資料從這邊整理來ㄉ(點我)", url="https://opendata.cwb.gov.tw/dataset/forecast/F-B0053-033")
    embed.set_thumbnail(
        url="https://img.cdn.nimg.jp/s/nicovideo/thumbnails/38135262/38135262.98063237.original/r1280x720l?key=4a095172beb00cb26112965018095abb2aa38b8b704a45b0029a39b4336a4d6f")
    embed.add_field(name="圖表", value="!weather a 小風口停車場\n!weather b 鳶峰停車場\n!weather c 台大梅峰實驗農場\n!weather d 新中橫塔塔加停車場\n!weather e 武陵農場\n!weather f 大雪山森林遊樂區\n!weather g 陽明山小油坑\n!weather h 陽明山擎天崗\n", inline=True)
    embed.add_field(name="表格", value="!plot", inline=True)
    await ctx.send(embed=embed)
    
