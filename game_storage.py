


import random

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

    l = []
    await message.channel.send('要存下來嗎? (y/n)')
    if message.content=='n':
        return
    elif message.content=='y':
        try:
            f=open("dictionary.txt",'a')
            f.write(record_dict,"\n")
            
            
            
        except:
            await message.channel.send('failed!')
    else :
        await message.channel.send('沒有這個選項喔!!')

    if message.content=='clear dic':
        with open('dictionary.txt','w') as f:
            pass
    if message.content=='view dic':
        try:
            list=[]
            with open('dictionary.txt','r') as f:
                for line in f.readlines():
                    #list.append(line)
                    await message.channel.send(line)
        except:
            await message.channel.send('failed!')
    if message.content=='review dic':
        if message.content == "q":
            return

        try:
            with open('dictionary.txt','r') as f:
                for line in f.readlines():
                    l.append(line)

                ran = random.choice(l)
                Q = ran.keys()
                A = ran.values()
                message.send(Q + "  " +A[0]+"_"*(len(A)-2)+A[-1])

                if message.content == A:
                    await message.send("correct")
                else:
                    await message.send("wrong")                    
        except:
            await message.channel.send('failed!')





# if i%3==0:
#                         ans=line
#                     elif i%3==1:
#                         await message.channel.send('中文解釋:')
#                         await message.channel.send(line)
#                         await message.channel.send('輸入此英文單字:')
#                         if message.content==ans:
#                             await message.channel.send('正解!')
#                         elif await message.content=='q':
#                             return
#                         else :
#                             await message.channel.send('答錯囉!答案為'+line)
#                     i+=1