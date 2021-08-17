
@bot.event
async def on_message(message):
    if message.content.startwith('dic'):
        word=message.content.split(' ',2)
        try:

            link='https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/'+word
            await message.channel.send(link) 
        except:
            await message.channel.send('failed!')
        #把網址記下來
    
    await message.channel.send('要存下來嗎? (y/n)')
    if message.content=='n':
        return
    elif message.content=='y':
        try:
            f=open(dictionary.txt,'a')
            f.write(word)
            f.write(link+'\n')
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
    if message.content=='review dic(q:quit)':
        try:
            with open('dictionary.txt','r') as f:
                i=0
                for line in f.readlines():
                    if i%3==0:
                        ans=line
                    elif i%3==1:
                        await message.channel.send('中文解釋:')
                        await message.channel.send(line)
                        await message.channel.send('輸入此英文單字:')
                        if message.content==ans:
                            await message.channel.send('正解!')
                        elif await message.content=='q':
                            return
                        else :
                            await message.channel.send('答錯囉!答案為'+line)
                    i+=1
        except:
            await message.channel.send('failed!')






        
    