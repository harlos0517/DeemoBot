from discord.ext.commands import Context as Ctx
from discord import Embed

async def buffer_eg(ctx: Ctx):
    embed = Embed(
        title="醋酸鈉Buffer", description="依序輸入pH值、濃度(mM)、體積(ml)，可以知道要秤多少克醋酸、醋酸鈉\npH建議在3.7 - 5.6之間\n(其實不知道算式有沒有寫對 鉿鉿)\n範例輸入: !buffer 4 50 100", color=0x9bdfd7)
    embed.add_field(
        name="所使用參數", value="醋酸的pKa: 4.76\n醋酸分子量: 60.052\n醋酸鈉分子量: 82.03", inline=False)
    await ctx.send(embed=embed)