from random import randint
import json

def game_state(data, filename="game_state.json"):
    """Saves a game statues as a Json file"""
    with open(filename, "w") as game_state_file:
        json.dump(data, game_state_file, indent=4)


def roll_dice():
    """rolls two six-sided dice and returns their values as a list"""
    return [randint(1, 6) for _ in range(2)]

def player_info():
    """prompts the user for their name and returns it"""
    name = input("Enter your name: ")
    piece = input("Choose your piece, 1 for Race Car, 2 for Top Hat, 3 for Scottie Dog, 4 for Cat, 5 for Penguin, 6 for Rubber duck, 7 for T-Rex and 8 for Battleship: ")

    return name, piece

def save_player_data(player_info, filename="players.json"):
    """Saves a player's data statues as a Json file"""
        with open(filename, "w") as f:
            json.dump(player_info, f, indent=4)

def load_player_data(filename="players.json"):
    """Loads a player's data statues from a Json file"""
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        

def main():
    name, piece = player_info()
    players = load_player_data()
    players.append({"name": name, "piece": piece})
    save_player_data(players)

    

    print(f"Welcome {name}! You have chosen the piece number {piece}.")
    input("Press Enter to roll the dice...")
    dice = roll_dice()
    print(f"You rolled a {dice[0]} and a {dice[1]}, for a total of {sum(dice)}.")
