v=int(input('Введите сумму выручки: '))
i=int(input('Введите сумму издержек: '))
if v>i:
    print("Ваша компания рентабельна, поздравляю!!!")
    print(f'Рентабельность компании составляет {(v-i)/v:.1f}')
    e=int(input('Сколько сотрудников работает в Вашей компании? '))
    print(f'Прибыль компании на 1 сотрудника составила {((v-i)/v)/e:.2f}')
elif v==i:
    print("Ваша компания в точке безубыточности, еще немного усилий и Вы - ОЛИГАРХ!")
else:
    print("Подумайте, как сократить издержки, иначе обанкротитесь...")