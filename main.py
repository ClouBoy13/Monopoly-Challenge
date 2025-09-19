from random import randint

def roll_dice():
    # rols two six-sided dice and returns their values as a list
    return [randint(1, 6) for _ in range(2)]

def player_info():
    # prompts the user for their name and returns it
    name = input("Enter your name: ")
    peice = input("Choose your piece, 1 for Race Car, 2 for Top Hat, 3 for Scottie Dog, 4 for Cat, 5 for Penguin, 6 for Rubber duck, 7 for T-Rex and 8 for Battleship: ")
    
    return name

