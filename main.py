from random import randint
import json

def roll_dice():
    # rols two six-sided dice and returns their values as a list
    return [randint(1, 6) for _ in range(2)]

def player_info():
    # prompts the user for their name and returns it
    name = input("Enter your name: ")
    peice = input("Choose your piece, 1 for Race Car, 2 for Top Hat, 3 for Scottie Dog, 4 for Cat, 5 for Penguin, 6 for Rubber duck, 7 for T-Rex and 8 for Battleship: ")

    return name, peice

def save_player_data(player_info, filename="players.json"):
        with open(filename, "w") as f:
            json.dump(player_info, f, indent=4)

def load_player_data(filename="players.json"):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        

def main():
    name, peice = player_info()
    players = load_player_data()
    players.append({"name": name, "peice": peice})
    save_player_data(players)

    num_players = int(input("Enter number of players (2-8): "))
    while not num_players.isdigit() or not (2 <= int(num_players) <= 8):
        num_players = input("Invalid input. Please enter a number between 2 and 8: ")

        

    print(f"Welcome {name}! You have chosen the piece number {peice}.")
    input("Press Enter to roll the dice...")
    dice = roll_dice()
    print(f"You rolled a {dice[0]} and a {dice[1]}, for a total of {sum(dice)}.")