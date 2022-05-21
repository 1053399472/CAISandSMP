import json
# from ltp import LTP
#
# ltp = LTP()
import jieba
data = json.load(open("train.json", 'r', encoding='utf-8'))
texts=[]
intents=[]
slots=[]
for line in data:
    texts.append([line['text']])
    intents.append([line['intent']])
    slot=['O']*len(line['text'])
    for e in line['entities']:
        start, end, label = e['start_idx'], e['end_idx'], e['type']
        if(start==end):
            slot[start]='S-'+label
        else:
            slot[start]='B-'+label
            slot[end]='E-'+label
            for i in range(start+1,end):
                slot[i]='I-'+label
    slots.append(slot)
slipetext=[]
for text in texts:
    slipetext.append(list(jieba.cut(''.join(text))))
slipeslots=[]
for text in slipetext:
    slipeslot = []
    for line in text:
        if len(line)==1:
            slipeslot.extend('B')
        elif len(line)==2:
            slipeslot.extend('B')
            slipeslot.extend('E')
        else:
            slipeslot.extend('B')
            for i in range(len(line)-2):
                slipeslot.extend('I')
            slipeslot.extend('E')
    slipeslots.append(slipeslot)
copytexts=[]
for text in texts:
    copytexts.append(list(text[0]))
texts=copytexts
with open('jieba/train.txt', 'w', encoding='utf-8') as fw:
    for t,i,s,sl in zip(texts,intents,slots,slipeslots):
        for text,slot,slipeslot in zip(t,s,sl):
            fw.write(text + '\t' + slot +'\t'+slipeslot + '\n')
        fw.write("".join(i))
        fw.write('\n\n')

print("success")