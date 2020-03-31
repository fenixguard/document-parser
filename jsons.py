import json


def create_wordlist(path):
    word_list = list()
    with open(path, "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
        for item in data['rss']['channel']['items']:
            temp_list = list()
            temp_list.extend(item['description'].split())
            for t in temp_list:
                if len(t) > 6:
                    word_list.append(t)
    return word_list


def count_word():
    word_count = dict()
    for word in word_list:
        try:
            word_count[word] = word_list.count(word)
        except KeyError:
            pass  # Исключаем повторы
    return word_count


def sorted_word():
    stats_sorted = sorted(word_count.items(), key=lambda x: -x[1])
    return stats_sorted


def print_result():
    for stat in stats_sorted[:10]:
        print(f"{stat[0]}: {stat[1]}")


if __name__ == '__main__':
    word_list = create_wordlist('newsafr.json')
    word_count = count_word()
    stats_sorted = sorted_word()
    print_result()
