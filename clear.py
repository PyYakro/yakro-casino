import os

def clear():
    try:
        os.system("clear")
    except:
        os.system("cls")