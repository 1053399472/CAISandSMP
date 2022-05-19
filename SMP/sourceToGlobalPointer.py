# from collections import Counter
# import json
# from pprint import pprint
#
# with open("2019train.json", 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     counter = Counter((row['intent']) for row in data)
# pprint(dict(counter))
# 测试函数，可以查询json指定键值的类别数目

import json
import os
import random
from collections import Counter
from pprint import pprint
from collections import defaultdict

def convert(data):
    dataText,entities,dataIntent=[],[],[]
    for x in data:
        dataText.append(x['text'])
        dataIntent.append(x['intent'])
        sententEntity=[]
        copyText = x['text']
        for key,values in x['slots'].items():
            copyText = x['text']
            entitie = [-1, -1, -1]
            entitie[0] = key
            cur_list = []
            end_list = []
            last_cur = 0
            if(isinstance(values,list)):
                for value in values:
                    entitie = [-1, -1, -1]
                    entitie[0] = key
                    copyText = x['text']
                    cur_list = []
                    end_list = []
                    last_cur = 0
                    while (1):
                        where = copyText.find(value)
                        if (not where == -1 and len(copyText)!=0):
                            cur_list.append(last_cur + where)
                            copyText = copyText[where + len(value):]
                            last_cur = last_cur + where + len(value)-1
                            end_list.append(last_cur)
                        else:
                            break
                    for i,j in zip(cur_list,end_list):
                        entitie[1]=i
                        entitie[2] =j
                        sententEntity.append(entitie)
            else:
                while (1):
                    where = copyText.find(values)
                    if (not where == -1 and len(copyText)!=0):
                        cur_list.append(last_cur + where)
                        copyText = copyText[where + len(values):]
                        last_cur = last_cur + where + len(values)-1
                        end_list.append(last_cur)
                    else:
                        break
                for i,j in zip(cur_list,end_list):
                    entitie[1]=i
                    entitie[2] =j
                    sententEntity.append(entitie)
        entities.append(sententEntity)
    return dataText,entities,dataIntent
# 核心转换函数

data = json.load(open("2020train.json", 'r', encoding='utf-8'))
tosplit = defaultdict(list)

# 2020
# total 5024 train 4011 dev 493 test 520
intent = ['QUERY', 'PLAY', 'SEND', 'LAUNCH', 'SET', 'TRANSLATION', 'ROUTE', 'DIAL', 'OPEN', 'CREATE', 'QUERY_GROUP',
          'WAVE_QUERY', 'CONVERSION_WITH_NUMBER', 'CONVERSION_HOW', 'HISTORY_DATE_QUERY', 'HISTORY_YEAR_QUERY',
          'POSITION', 'CITY_QUERY_THREE', 'SEARCH', 'SENDCONTACTS', 'NUMBER_QUERY', 'SET_CLOCK', 'TURN_ON_LIGHT',
          'TURN_OFF_LIGHT', 'CLEAN', 'ALLINFO_FAMILY_NAMES', 'DEFAULT', 'CITY_QUERY_TWO', 'REPLY', 'FORWARD',
          'PROVINCE_CITY', 'CITY_PROVINCE', 'CITY_QUERY', 'MORECITY_QUERY', 'PROVINCE_QUERY', 'MOREPROVINCE_QUERY',
          'DATE_QUERY', 'DESCRIPTION_QUERY', 'SCORE_QUERY', 'ALL_FAMILY_NAMES', 'ORDER_FAMILY_NAME',
          'EXISTENT_FAMILY_NAMES', 'CITY_QUERY_ONE', 'CITY_QUERY_FOUR', 'LOOK_BACK', 'VIEW', 'DOWNLOAD',
          'RISERATE_QUERY', 'CLOSEPRICE_QUERY', 'CLOSE', 'PREVIOUS', 'CHANGE', 'NEXT', 'LIVE', 'CHANNELLISE',
          'CHANNELNAME', 'PREVIOUSCHANNEL', 'CHANGECHANNEL', 'NEXTCHANNEL']

# 2019
# total 2579 train 2053 dev 256 test 270
# intent = ['CLOSEPRICE_QUERY', 'CREATE', 'DATE_QUERY', 'DEFAULT', 'DIAL', 'DOWNLOAD', 'FORWARD', 'LAUNCH', 'LOOK_BACK',
#           'NUMBER_QUERY', 'OPEN', 'PLAY', 'POSITION', 'QUERY', 'REPLAY_ALL', 'REPLY', 'RISERATE_QUERY', 'ROUTE',
#           'SEARCH', 'SEND', 'SENDCONTACTS', 'TRANSLATION', 'VIEW'
#           ]
for row in data:
    for x in intent:
        if (row['intent'] == x):
            tosplit[x].append(row)
train=[]
dev=[]
test=[]
for x in intent:
    sum = 0
    sum=len(tosplit.get(x))
    TrainDataRate=int(sum*0.8)
    DevDataRate = int(sum*0.9)
    random.shuffle(tosplit.get(x))
    TrainData=tosplit.get(x)[:TrainDataRate]
    DevData=tosplit.get(x)[TrainDataRate:DevDataRate]
    TestDate=tosplit.get(x)[DevDataRate:]
    train.extend(TrainData)
    dev.extend(DevData)
    test.extend(TestDate)
random.shuffle(train)
random.shuffle(dev)
random.shuffle(test)

keys = ['type', 'start_idx', 'end_idx']
keysJson = ['text', 'entities', 'intent']

fileObject = open("GlobalPointerSMP2019/dev.json", "w", encoding="utf-8")
devdataText,deventities,devdataIntent=convert(dev)
fileObject.write('[')
for items, itemchar, itemIntent in zip(deventities, devdataText, devdataIntent):
    example = []
    for item in items:
        example.append(dict(zip(keys, item)))
    fileObject.write(json.dumps(dict(zip(keysJson, [itemchar, example, itemIntent])), ensure_ascii=False))
    fileObject.write(',')
fileObject.write(']')

fileObject = open("GlobalPointerSMP2019/train.json", "w", encoding="utf-8")
traindataText,trainentities,traindataIntent=convert(train)
fileObject.write('[')
for items, itemchar, itemIntent in zip(trainentities, traindataText, traindataIntent):
    example = []
    for item in items:
        example.append(dict(zip(keys, item)))
    fileObject.write(json.dumps(dict(zip(keysJson, [itemchar, example, itemIntent])), ensure_ascii=False))
    fileObject.write(',')
fileObject.write(']')

fileObject = open("GlobalPointerSMP2019/test.json", "w", encoding="utf-8")
testdataText,testentities,testdataIntent=convert(test)
fileObject.write('[')
for items, itemchar, itemIntent in zip(testentities, testdataText, testdataIntent):
    example = []
    for item in items:
        example.append(dict(zip(keys, item)))
    fileObject.write(json.dumps(dict(zip(keysJson, [itemchar, example, itemIntent])), ensure_ascii=False))
    fileObject.write(',')
fileObject.write(']')

print("success")
