import random as r
from clear import clear

def nvuti():
    clear()
    nvuti = r.randint(0, 999999)
    print("Выберите:\n[ < ] Меньше 499999 | [ > ] Больше 500000\n")
    uinput = input("< или >: ")
    if uinput == '<':
        if nvuti <= 499999:
            clear()
            print(f"Выпало число: {nvuti}")
            print("Вы выиграли!")
        else:
            clear()
            print(f"Выпало число: {nvuti}")
            print("Вы проиграли!")
    elif uinput == '>':
        if nvuti >= 500000:
            clear()
            print(f"Выпало число: {nvuti}")
            print("Вы выиграли!")
        else:
            clear()
            print(f"Выпало число: {nvuti}")
            print("Вы проиграли!")
    else:
        clear()
        print("Ошибка ввода!")