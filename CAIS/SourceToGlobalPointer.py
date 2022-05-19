import json
if __name__ == "__main__":
    char_texts, slots = [], []
    char_text=""
    slot=[]
    intents = []
    with open("datasets/CAIS/ch.test.intent", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if (line == ' '):
                continue
            intents.append(line.strip())
    with open("datasets/CAIS/test.char.bmes", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            items = line.strip().split()
            if len(items) == 0:
                char_texts.append(char_text)
                slots.append(slot)
                slot= []
                char_text = ""
            elif len(items) >= 2:
                char, slot_tag = items[0].strip(), items[1].strip()
                char_text=char_text+char
                x = slot_tag.split('-')
                if(len(x)==2):
                    if (x[0] == "E"):
                        x[0] = "I"
                    slot_tag=x[0]+'-'+x[1]
                slot.append(slot_tag)
        char_texts.append(char_text)
        slots.append(slot)
    examples = []
    for items in slots:
        chunks = []
        chunk = [-1, -1, -1]
        for indx, tag in enumerate(items):
            if tag.startswith("S-"):
                if chunk[2] != -1:
                    chunks.append(chunk)
                chunk = [-1, -1, -1]
                chunk[1] = indx
                chunk[2] = indx
                chunk[0] = tag.split('-')[1]
                chunks.append(chunk)
                chunk = (-1, -1, -1)
            if tag.startswith("B-"):
                if chunk[2] != -1:
                    chunks.append(chunk)
                chunk = [-1, -1, -1]
                chunk[1] = indx
                chunk[0] = tag.split('-')[1]
            elif tag.startswith('I-') and chunk[1] != -1:
                _type = tag.split('-')[1]
                if _type == chunk[0]:
                    chunk[2] = indx
                if indx == len(items) - 1:
                    chunks.append(chunk)
            else:
                if chunk[2] != -1:
                    chunks.append(chunk)
                chunk = [-1, -1, -1]
        examples.append(chunks)
    keys = ['type','start_idx', 'end_idx']
    keysJson=['text','entities','intent']
    toJson=[]
    fileObject = open("datasets/jsonCAIS/test.json", "w", encoding="utf-8")
    fileObject.write('[')
    for items,itemchar,itemIntent in zip(examples,char_texts,intents):
        example=[]
        for item in items:
            example.append(dict(zip(keys, item)))
        fileObject.write(json.dumps(dict(zip(keysJson,[itemchar,example,itemIntent])), ensure_ascii=False))
        fileObject.write(',')
    fileObject.write(']')
