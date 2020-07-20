import random as r

nvuti = r.randint(0, 999999)

def nvuti_choose():
    print("Выберите:\n[ < ] Меньше 499999 | [ > ] Больше 500000\n")
    uinput = input("< или >: ")
    if uinput == '<':
        if nvuti <= 499999:
            print(f"Выпало число: {nvuti}")
            print("Вы выиграли!")
        else:
            print(f"Выпало число: {nvuti}")
            print("Вы проиграли!")
    elif uinput == '>':
        if nvuti >= 500000:
            print(f"Выпало число: {nvuti}")
            print("Вы выиграли!")
        else:
            print(f"Выпало число: {nvuti}")
            print("Вы проиграли!")
    else:
        print("Ошибка ввода!")
nvuti_choose()