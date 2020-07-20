from clear import clear
from time import sleep
from dice import dice
from slots import slots
from roulette import roulette
from point21 import game21
from nvuti import nvuti
from RGBY import rgby

while True:
    
    print()
    print("YAKRO CASINO")
    print()
    print("Выберите режим:")
    print("1. Dice")
    print("2. Slots")
    print("3. Roulette")
    print("4. 21 points")
    print("5. Nvuti")
    print("6. RGBY")
    print("7. Quit")
    print()
    print("#. Help")
    print()
    
    user_input = input(">>> ")
    
    if user_input == 'Dice' or user_input == 'dice':
        clear()
        dice()
        sleep(5)
        clear()
    elif user_input == 'Slots' or user_input == 'slots':
        clear()
        slots()
        sleep(5)
        clear()
    elif user_input == 'Roulette' or user_input == 'roulette':
        clear()
        roulette()
        sleep(5)
        clear()
    elif user_input == "21 points":
        game21()
        sleep(5)
        clear()
    elif user_input.lower() == "nvuti":
        nvuti()
        sleep(5)
        clear()
    elif user_input.lower() == "rgby":
        rgby()
        sleep(5)
        clear()
    elif user_input == 'Help' or user_input == 'help':
        clear()
        print("Помощь:")
        print()
        print("Режимы:\n\n1. Dice - Простенькая игра. Выпадает рандомное число от 0 до 100.\n2. Slots - Обычные игровые слоты.\n3. Roulette - Рулетка. 'Крутится' шарик, и выпадает рандомное число от 0 до 36 с своим цветом и честностью.\n4. 21 points - Карточная игра 21 очко. Выигрывает тот, у кого будет больше всех очков, но не больше 21.\n5. Nvuti - чем-то похожее на режим Dice, но более больший разброс. От 0 до 999999.\n6. RGBY - Совершенно новый режим игры. Есть 5 случайно генерирующихся значений карт: 10, J, Q, K, A. Для каждой карты генерируется свой цвет: Красный, Зеленый, Синий, Желтый. По задумке автора (Yakro), ваша задача угадать значение карты и ее цвет.")
        sleep(25)
        clear()
    elif user_input == 'Quit' or user_input == 'quit':
        clear()
        break
    else:
        print('Ошибка ввода!')
        sleep(2)
        clear()