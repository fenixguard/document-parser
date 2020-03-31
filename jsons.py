import json

total_count_word = dict()

with open(r"C:\Users\FenixGuard\Desktop\newsafr.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)
    word_list = list()
    for item in data['rss']['channel']['items']:
        temp_list = list()
        temp_list.extend(item['description'].split())
        for t in temp_list:
            if len(t) > 6:
                word_list.append(t)
    for w in word_list:
        try:
            total_count_word[w] = word_list.count(w)
        except KeyError:
            pass
    stats_sorted = sorted(total_count_word.items(), key=lambda x: -x[1])
    for stat in stats_sorted[:10]:
        print(f"{stat[0]}: {stat[1]}")
