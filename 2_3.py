d = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}  # словарь и список
m = int(input('Введите номер месяца в диапазоне от 1 до 12: '))
if m < 1 or m > 12:
    print('Введите корректное число')
else:
    for a in d.keys():
        if m in d[a]:
            print(a)