import os

def __read_file(file_path, max_char_seq_len):
    char_texts, slots, intents = [], [], []
    char_text, slot= [], []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            items = line.strip().split()

            if len(items) == 1:
                char_texts.append(char_text)
                slots.append(slot)

                intents.append(items)

                # clear buffer lists.
                char_text, slot = [], []

            elif len(items) >= 2:
                char, slot_tag = items[0].strip(), items[1].strip()
                if len(char_text) >= max_char_seq_len:
                    continue
                #     超过规定长度的句子就不接受了
                char_text.append(char)
                slot.append(slot_tag)
    return char_texts, slots, intents


train_path = os.path.join("../mergeCAIS","train.txt")
dev_path = os.path.join("../mergeCAIS", "dev.txt")
test_path = os.path.join("../mergeCAIS", "test.txt")
train_char,train_slot,train_intent=__read_file(train_path,50)
dev_char,dev_slot,dev_intent=__read_file(dev_path,50)
test_char,test_slot,test_intent=__read_file(test_path,50)

print("success")