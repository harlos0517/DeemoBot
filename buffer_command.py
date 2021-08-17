from typing import List
import discord as dc
from discord.ext.commands import Context as Ctx

async def buffer(ctx: Ctx, args: List[str]):
    pKa = 4.76
    acetic_acid_M = 60.052
    sodium_acetate_M = 82.03
    pH = eval(args[0])
    concentration = eval(args[1])
    volume = eval(args[2])
    t = pH - pKa
    s = 10**t
    acetic_acid_con = concentration/(s + 1)
    sodium_acetate_con = concentration*(1 - (1/(s + 1)))
    acetic_acid_wei = acetic_acid_con*acetic_acid_M/(volume/1000)/1000
    sodium_acetate_wei = sodium_acetate_con*sodium_acetate_M/(volume/1000)/1000
    embed = dc.Embed(
        title="計算結果", description=f"所以你想要pH = {pH}，{concentration:.3f}mM，{volume:.3f}ml的醋酸鈉buffer，好喔\n 如果pH值不準，自己滴定一下吧 鉿鉿(X", color=0x9bdfd7)
    embed.add_field(
        name="配置方法", value=f"秤取{sodium_acetate_wei:.3f}g 醋酸鈉、{acetic_acid_wei:.3f}克醋酸\n溶解後定量到{volume:.0f}ml", inline=False)
    embed.add_field(
        name="成品", value=f"你有機率獲得pH值接近{pH:.0f}的buffer\n其中，醋酸的期望濃度是{acetic_acid_con:.3f}mM，醋酸鈉的期望濃度是{sodium_acetate_con:.3f}mM", inline=True)
    await ctx.send(embed=embed)
    # Ans = f"[pH = {pH}，{concentration:.3f}mM，{volume:.3f}ml 醋酸鈉溶液配置方法]\n取{sodium_acetate_wei:.3f}g 醋酸鈉，{acetic_acid_wei:.3f}克醋酸，溶解後定量到{volume:.0f}ml，你有機率獲得pH值接近{pH:.0f}的buffer。\n其中，醋酸的期望濃度是{acetic_acid_con:.3f}mM，醋酸鈉的期望濃度是{sodium_acetate_con:.3f}mM"
    # await ctx.send(Ans)