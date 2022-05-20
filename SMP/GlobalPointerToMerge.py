import json
data = json.load(open("dev.json", 'r', encoding='utf-8'))
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
copytexts=[]
for text in texts:
    copytexts.append(list(text[0]))
texts=copytexts
with open('merge/dev.txt', 'w', encoding='utf-8') as fw:
    for t,i,s in zip(texts,intents,slots):
        for text,slot in zip(t,s):
            fw.write(text + '\t' + slot + '\n')
        fw.write("".join(i))
        fw.write('\n\n')

print("success")