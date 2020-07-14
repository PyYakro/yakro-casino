#21 points
from random import randint
from clear import clear

dealer = randint(4, 21)
me = 0
take = 0

def game21():
    
    clear()
    
    me = randint(4, 21)
    
    print("Сумма карт дилера: **")
    print("Сумма Ваших карт:", me)
    print()
    print("1. Взять")
    print("2. Все")
    print()
    
    uinput = input("Выбор: ")
    
    if uinput == "Взять" or uinput == "взять" or uinput == "1":
        
        clear()
        
        take = randint(2, 11)
        me += take
        
        if dealer < me and me < 21:
            print("Сумма карт дилера:", dealer)
            print("Сумма Ваших карт:", me)
            print()
            print("Сумма карт добавлена:", take)
            print()
            print("Вы победили!")
        elif dealer < me and me == 21:
            print("Сумма карт дилера:", dealer)
            print("Сумма Ваших карт:", me)
            print()
            print("Сумма карт добавлена:", take)
            print()
            print("Вы набрали 21 очко и выиграли!")
        elif me < dealer or me > 21:
            print("Сумма карт дилера:", dealer)
            print("Сумма Ваших карт:", me)
            print()
            print("Сумма карт добавлена:", take)
            print()
            print("Вы проиграли!")
        elif dealer == me:
            print("Сумма карт дилера:", dealer)
            print("Сумма Ваших карт:", me)
            print()
            print("Сумма карт добавлена:", take)
            print()
            print("Ничья!")
            
    elif uinput == "Все" or uinput == "все" or uinput == "2":
        
        clear()
        
        if dealer < me and me != 21:
            print("Сумма карт дилера:", dealer)
            print("Сумма Ваших карт:", me)
            print()
            print("Вы победили!")
        elif dealer < me and me == 21:
            print("Сумма карт дилера:", dealer)
            print("Сумма Ваших карт:", me)
            print()
            print("Вы набрали 21 очко и выиграли!")
        elif me < dealer:
            print("Сумма карт дилера:", dealer)
            print("Сумма Ваших карт:", me)
            print()
            print("Вы проиграли!")
        elif dealer == me:
            print("Сумма карт дилера:", dealer)
            print("Сумма Ваших карт:", me)
            print()
            print("Ничья!")