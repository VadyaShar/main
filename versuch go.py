import json
import random
import tkinter as tk
import json

with open('ddd.json', 'r', encoding='utf-8') as f:
    wort = json.load(f)

x1 = wort


y = (random.sample(list(x1.items()), 1))

def get_entry_value():
    value = entry.get()


# Создание окна Tkinter
window = tk.Tk()
window.title("Entry Widget Value Retrieval")

# Создание виджета Entry
entry = tk.Entry(window)
entry.pack()
# Создание кнопки для запуска получения значения
button = tk.Button(window, text="Get Entry Value", command=get_entry_value)
button.pack()

# Запуск цикла событий Tkinter
window.mainloop()


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

print("Немецкое слово: ", y)

An1 = input("Введите перевод: ")
if An1 == y1 or y2 or y3 or y4:
    print("Das Stimmt")
else:
    print("Falsch")




