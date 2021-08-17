'''
在on_message之下呼叫這個function並傳入message，若message.content == "weather會回傳解釋weather的embede。
但不確定在on_message之下這樣做會不會有問題，若有，直接在on_message之下貼上if那一段。
'''
import discord


async def weather_explane(message):
    if message.content == "weather":
        embed = discord.Embed(
            title="weather相關Command 表", description="輸入command，順利的話會收到表格or圖表\n範例輸入1. !plot \n範例輸入2. !weather a \n註:merge到deemo bot之後要改範例輸入指令", color=0x98bee6)
        embed.set_author(
            name="資料從這邊整理來ㄉ(點我)", url="https://opendata.cwb.gov.tw/dataset/forecast/F-B0053-033")
        embed.set_thumbnail(
            url="https://img.cdn.nimg.jp/s/nicovideo/thumbnails/38135262/38135262.98063237.original/r1280x720l?key=4a095172beb00cb26112965018095abb2aa38b8b704a45b0029a39b4336a4d6f")
        embed.add_field(name="圖表", value="!weather a 小風口停車場\n!weather b 鳶峰停車場\n!weather c 台大梅峰實驗農場\n!weather d 新中橫塔塔加停車場\n!weather e 武陵農場\n!weather f 大雪山森林遊樂區\n!weather g 陽明山小油坑\n!weather h 陽明山擎天崗\n", inline=True)
        embed.add_field(name="表格", value="!plot", inline=True)
        await message.channel.send(embed=embed)
    if message.content == "buffer":
        embed = discord.Embed(
            title="醋酸鈉Buffer", description="依序輸入pH值、濃度(mM)、體積(ml)，可以知道要秤多少克醋酸、醋酸鈉\npH建議在3.7 - 5.6之間\n(其實不知道算式有沒有寫對 鉿鉿)\n範例輸入: !buffer 4 50 100", color=0x9bdfd7)
        embed.add_field(
            name="所使用參數", value="醋酸的pKa: 4.76\n醋酸分子量: 60.052\n醋酸鈉分子量: 82.03", inline=False)
        await message.channel.send(embed=embed)
