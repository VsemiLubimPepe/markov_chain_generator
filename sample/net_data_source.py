import requests
import json

# http(s)://2ch.hk/доска/res/номертреда.json
# Список тредов:
# http(s)://2ch.hk/доска/номерстраницы.json (первая страница: index)
# Все треды с сортировкой по последнему посту:
# http(s)://2ch.hk/доска/catalog.json
# Все треды с сортировкой по времени создания треда:
# http(s)://2ch.hk/доска/catalog_num.json
# Все треды с доски(облегченный вариант, с просмотрами и рейтингом для топа тредов):
# http(s)://2ch.hk/доска/threads.json

source_data_json = requests.get("https://2ch.hk/b/threads.json").json()
thread_names = source_data_json['threads']
for thread in thread_names:
    thread_json = requests.get("https://2ch.hk/b/res/" + str(thread["num"]) + ".json").json()
    print(thread_json['threads'][0]['posts'][0]['comment'])
    print()
# thread_json = requests.get("https://2ch.hk/b/res/288669593.json").json()


# print(source_data_json)

# print(thread_json)