#dice
import random as r

def dice():
    dice = r.uniform(0, 100)
    dice = round(dice, 2)
    print("Выпало число:", dice)