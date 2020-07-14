#slots
import random as r
list = ['A', 'B', 'C', 'Z', '7']

def slots():
    slots = [r.choice(list) for _ in range(3)]
    print("_______")
    print("|{}|{}|{}|".format(*slots))
    print("=======")