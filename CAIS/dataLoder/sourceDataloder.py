import os

def __read_slot_file(file_path, max_char_seq_len):
    char_texts, slots = [], []
    char_text, slot = [], []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            items = line.strip().split()
            if len(items) == 0:
                char_texts.append(char_text)
                slots.append(slot)
                # clear buffer lists.
                char_text, slot = [], []

            elif len(items) >= 2:
                char, slot_tag = items[0].strip(), items[1].strip()
                if len(char_text) >= max_char_seq_len:
                    continue
                #     超过规定长度50的句子就不接受了
                char_text.append(char)
                slot.append(slot_tag)
        if(len(slot)!=0 and len(char_text)!=0):
            char_texts.append(char_text)
            slots.append(slot)
            # 最后一行空白可能识别不到，所以再加一次防止漏掉
    return char_texts, slots

def __read_intent_file(file_path):
    intents = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if(line==' '):
                continue
            intents.append(line.strip())
    return intents

train_slot_path = os.path.join("../source/train","ch.train")
dev_slot_path = os.path.join("../source/valid", "ch.valid")
test_slot_path = os.path.join("../source/test", "ch.test")
train_Intent_path = os.path.join("../source/train","ch.train.intent")
dev_Intent_path = os.path.join("../source/valid", "ch.valid.intent")
test_Intent_path = os.path.join("../source/test", "ch.test.intent")
train_char,train_slot=__read_slot_file(train_slot_path,50)
train_intent=__read_intent_file(train_Intent_path)
dev_char,dev_slot=__read_slot_file(dev_slot_path,50)
dev_intent=__read_intent_file(dev_Intent_path)
test_char,test_slot=__read_slot_file(test_slot_path,50)
test_intent=__read_intent_file(test_Intent_path)
print("success")