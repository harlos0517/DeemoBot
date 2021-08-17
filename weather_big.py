
'''
主要處理資料的檔案，把json爬下來後拆解做表格。很亂很可怕，其中get_fram會被其他檔案import。
'''
import dataframe_image as dfi
import numpy as np
import pandas as pd
import urllib.request
import json

jsonres = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-B0053-069?Authorization=CWB-D83A7BB1-9603-410A-97D0-D413CA8369AB&downloadType=WEB&format=JSON"
response = urllib.request.urlopen(jsonres)
hjason = json.loads(response.read())
GET_TIME = hjason['cwbopendata']['sent']
# print(hjason)

hh = hjason
x = hh.keys()
# print(x)

a = hh['cwbopendata']["dataset"]["locations"]['location'][0]['locationName']
b = hh['cwbopendata']["dataset"]["locations"]['location']  # for #是list
c = hh['cwbopendata']["dataset"]["locations"]['location'][0]["weatherElement"]  # 是list
# 是dict #是天氣總述
d = hh['cwbopendata']["dataset"]["locations"]['location'][0]["weatherElement"][14]
# 是list #for #wee # 天氣總數中有時間跟結果那段
e = hh['cwbopendata']["dataset"]["locations"]['location'][0]["weatherElement"][14]['time']

# print(e)

# ['多雲', '降雨機率 10%', '溫度攝氏15至17度', '寒冷至稍有寒意', '西南風 風速2級(每秒2公尺)', '相對濕度96%', '']


def con(vali):
    z = vali[2][4:6]
    x = vali[2][7:9]
    c = z+'~'+x
    # print(c)
    vali[2] = c

    '''
    d = vali[4].split()[1].split('(')[0][2]
    dd = vali[4].split()[0]
    ddd = dd+ ' '+d
    vali[4] = ddd
    '''
    if len(vali[5]) == 7:
        f = int(vali[5][4:6])
    elif len(vali[5]) == 8:
        f = int(vali[5][4:7])
    else:
        pass

    vali[5] = f


class tableob:
    def __init__(self, los, my_frame):
        self.my_frame = my_frame
        self.los = los
        self.name = los['locationName']
        fradict[self.name] = self.my_frame
        dicdict[self.name] = self.los
        # print(objdict)

    def getframe(self):
        return self.my_frame


loclist = ["小風口停車場", "鳶峰停車場", "台大梅峰實驗農場", "新中橫塔塔加停車場",
           "武陵農場", "大雪山國家森林遊樂區", "陽明山國家公園小油坑停車場", "陽明山國家公園擎天崗"]
locdict = {"小風口停車場": 1, "鳶峰停車場": 2, "台大梅峰實驗農場": 3, "新中橫塔塔加停車場": 4,
           "武陵農場": 17, "大雪山國家森林遊樂區": 18, "陽明山國家公園小油坑停車場": 21, "陽明山國家公園擎天崗": 22}
objdict = {}
fradict = {}
dicdict = {}
okdict = {}

Bwe0list = []
Bwe1list = []
Bwe2list = []
Bwe3list = []
Bwe4list = []
Bwe5list = []
Bnamelist = []
Btimelist = []
for los in b:
    listt = []

    if los['locationName'] in loclist:
        id = locdict[los['locationName']]

        # print(los['locationName'])
        wee = b[id]["weatherElement"][14]['time']
        stime = []
        we0list = []
        we1list = []
        we2list = []
        we3list = []
        we4list = []
        we5list = []
        for tim in wee:
            ll = tim['startTime'].split('+')[0].split('T')[0]
            lll = tim['startTime'].split('+')[0].split('T')[1]
            # print(ll+' '+lll)
            t = ll+' '+lll
            stime += t,

            # print(tim['elementValue']['value'])
            value = tim['elementValue']['value']
            vali = value.split('。')
            # ['多雲', '降雨機率 10%', '溫度攝氏15至17度', '寒冷至稍有寒意', '西南風 風速2級(每秒2公尺)', '相對濕度96%', '']
            # ['陰時多雲短暫陣雨或雷雨', '溫度攝氏16至17度', '稍有寒意', '偏西風 風速2級(每秒2公尺)', '相對濕度90%', '']
            vali.pop(-1)
            if len(vali) == 5:
                vali.insert(1, np.nan)
            else:
                if vali[1] == "降雨機率 100%":
                    a = int(vali[1].split()[1][:3])
                elif vali[1] == "降雨機率 0%":
                    a = int(vali[1].split()[1][:1])
                else:
                    a = int(vali[1].split()[1][:2])

                vali[1] = a

            tit = ['天氣現象', '降雨機率(%)', '溫度(攝氏)', '舒適度', '風向 風速', '相對濕度(%)']
            con(vali)
            Bnamelist.append(los['locationName'])
            we0list.append(vali[0])
            we1list.append(vali[1])
            we2list.append(vali[2])
            we3list.append(vali[3])
            we4list.append(vali[4])
            we5list.append(vali[5])
            dic = {tit[0]: we0list, tit[1]: we1list, tit[2]: we2list,
                   tit[3]: we3list, tit[4]: we4list, tit[5]: we5list}

        Bwe0list += we0list
        Bwe1list += we1list
        Bwe2list += we2list
        Bwe3list += we3list
        Bwe4list += we4list
        Bwe5list += we5list
        Btimelist += stime

        listt.append(dic)

        my_frame = pd.DataFrame(data=listt[0], index=stime)
        index = my_frame.index
        index.name = '開始記錄時間'
        i = 0
        for x in my_frame.loc[:, "降雨機率(%)"]:
            if x >= 99:
                okdict[los['locationName']] = []
                okdict[los['locationName']].append(stime[i])

            else:
                pass
            i += 1
        # my_frame = my_frame.style.set_caption(los['locationName']+' '+'1週逐12小時天氣預報').set_table_styles([{
        #     'selector': 'caption',
        #     'props': [  # ('color', 'gray'),
        #         ('font-size', '16px')]
        # }])
        # my_frame.format({"降雨機率(%)": "{:.0f}"})

        A = tableob(los, my_frame)
        objdict[los['locationName']] = A
        # my_frame.background_gradient(
        #     cmap="YlGnBu", vmin=0, vmax=100).highlight_null('')

        # # display(my_frame)

    else:
        pass
# print(len(Bwe0list), len(Bwe1list), len(Bwe2list), len(
    # Bwe3list), len(Bwe4list), len(Bwe5list), len(Bnamelist))
Bdic = {tit[0]: Bwe0list, tit[1]: Bwe1list, tit[2]: Bwe2list, tit[3]: Bwe3list,
        tit[4]: Bwe4list, tit[5]: Bwe5list, "location name": Bnamelist, "time": Btimelist}
Bframe = pd.DataFrame(data=Bdic)
# print(Bframe)


def get_fram(arg: str):
    '''
    前面把dic跟frame存在dicdict(key是地點中文名) 跟fradict(同前)裡，可以叫出來用
    r = {"a":"小風口停車場", "b":"鳶峰停車場", "c":"台大梅峰實驗農場", "d":"新中橫塔塔加停車場",
        "e":"武陵農場", "f":"大雪山國家森林遊樂區", "g":"陽明山國家公園小油坑停車場", "h":"陽明山國家公園擎天崗"}
    return fradict[r["id"]]
    '''
    r = {"a": "小風口停車場", "b": "鳶峰停車場", "c": "台大梅峰實驗農場", "d": "新中橫塔塔加停車場",
         "e": "武陵農場", "f": "大雪山國家森林遊樂區", "g": "陽明山國家公園小油坑停車場", "h": "陽明山國家公園擎天崗"}
    a = fradict[r[arg]]
    dfi.export(a, 'a_styled.png')


# print()
# print(okdict)

if __name__ == '__main__':
    print(fradict)
    print(GET_TIME)
    print(str(["08", "15 "]))
