# roulette
from random import choice

def roulette():
    list = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
    list2 = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
    
    r = choice(list)
    
    if r % 2 == 0:
        parity = 'Четное'
    else:
        parity = 'Нечетное'

    if r == 0:
        color = 'Зеленое'
    elif r in list2:
        color = 'Красное'
    else:
        color = 'Черное'

    roulette = r

    print("Выпало число:",roulette,"|",parity,"|",color)