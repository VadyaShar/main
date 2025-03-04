import json
import random


with open('ddd.json', 'r', encoding='utf-8') as f:
    wort = json.load(f)

x1 = wort


x = (random.sample(list(x1.items()), 1))
print(x)


y = x[0][0]
y1 = x[0][1][0]
y2 = x[0][1][1]
y3 = x[0][1][2]
y4 = x[0][1][3]


# print("Немецкое слово: ", y)
#
# An1 = input("Введите перевод: ")
# if An1 == y1 or y2 or y3 or y4:
#     print("Das Stimmt")
# else:
#     print("Falsch")
#
#
# print("Немецкое слово: ", x[1][0])
# An2 = input("Введите перевод: ")
# if An2 == y1 or y2 or y3 or y4:
#     print(True)
# else:
#     print(False)

