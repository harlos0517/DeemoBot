import discord as dc
from os import remove as rm
from discord.ext.commands import Context as Ctx
from mingus.extra import lilypond

async def lily(ctx: Ctx, arg: str):
    try:
        if lilypond.to_png(arg, "temp.png"):
            with open("temp.png", 'rb') as f:
                picture = dc.File(f)
                await ctx.send(file=picture)
                rm("temp.png")
        else:
            await ctx.send("Conversion failed")
    except:
        await ctx.send("Conversion failed")