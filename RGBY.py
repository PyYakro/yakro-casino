import random as r
from clear import clear

def rgby():
    clear()
    name = ['10', 'J', 'Q', 'K', 'A']
    color = ['Красный', 'Зеленый', 'Синий', 'Желтый']

    card = [r.choice(name) for _ in range(3)]
    ccard = [r.choice(color) for _ in range (3)]

    print("| {} {} | {} {} | {} {} |".format(card[0], ccard[0], card[1], ccard[1], card[2], ccard[2]))