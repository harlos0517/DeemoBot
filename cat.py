from os import remove as rm

import requests as req
import discord as dc
from discord.ext.commands import Context as Ctx

async def cat(ctx: Ctx, arg: str):
    try:
        img = req.get(f"https://http.cat/{arg}")
        with open("cat.jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)
        with open("cat.jpg", 'rb') as f:
            picture = dc.File(f)
            await ctx.send(file=picture)
            rm("cat.jpg")
    except Exception as e:
        print(e)