import random
import json

@bot.event
async def on_message(message):
    
    if message.content.startswith('dic'):
        input = message.content
        try:

            link='https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'+word
            await message.channel.send(link) 
        except:
            await message.channel.send('failed!')
        #把網址記下來
# ----------------------

    await message.channel.send('要存下來嗎? (y/n)')
    if message.content=='n':
        return
    elif message.content=='y':
        try:
            with open('dic.json','a',encoding='utf-8') as f:
                json.dump(record_dict,f, ensure_ascii=False, indent=4,sort_keys=True)
            
            
        except:
            await message.channel.send('failed!')
    else :
        await message.channel.send('沒有這個選項喔!!')

    if message.content=='clear dic':
        with open('dic.json','w',encoding='utf-8') as f:
            pass
            
    if message.content=='view dic':
        try:
            with open('dic.json') as f:
               file=json.load(f)
               await message.channel.send(file)
        except:
            await message.channel.send('failed!')
    if message.content=='review dic':
        try:
           with open('dic.json') as f:
               file=json.load(f)
               await message.channel.send(file)

                q ,a = random.choice(list(file.items()))
                    for i in len(q):
                    Q=q[i]
                    A=a[i]
                    message.send(Q + "  " +A[0]+"_"*(len(A)-2)+A[-1])

                    if message.content == A:
                        await message.send("correct")
                    elif message.content == "q":
                        return
                    else:
                        await message.send("wrong")                    
        except:
            await message.channel.send('failed!')

