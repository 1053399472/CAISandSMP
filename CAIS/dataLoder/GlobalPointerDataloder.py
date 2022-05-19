import os
import json
slot2id = {"singer_name": 0, "song_name": 1, "crosstalk_name": 2, "location": 3, "date": 4, "joke_tag": 5,
          "song_type": 6, "actor_name": 7, "album_name": 8, "event": 9, "joke_name": 10, "movie_name": 11, "list": 12,
          "story_name": 13, "story_tag": 14, "author_name": 15, "fiction_name": 16, "song_language": 17,
          "poem_name": 18, "fiction_tag": 19, "news_time": 20, "ranking": 21, "poem_tag": 22, "news_tag": 23}
slot2id={}
def load_data(path):
    D = []
    for d in json.load(open(path, 'r', encoding='utf-8')):
        D.append([d['intent']])
        D[-1].append(d['text'])
        for e in d['entities']:
            start, end, label = e['start_idx'], e['end_idx'], e['type']
            if start <= end:
                D[-1].append((start, end, slot2id[label]))
    return D

train_path = os.path.join("../GlobalPointerCAIS","train.json")
dev_path = os.path.join("../GlobalPointerCAIS", "dev.json")
test_path = os.path.join("../GlobalPointerCAIS", "test.json")
train_dateset=load_data(train_path)
dev_dateset=load_data(dev_path)
test_dateset=load_data(test_path)
print("success")