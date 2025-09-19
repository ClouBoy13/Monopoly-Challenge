from random import randint
import json

PIECES = {
    "1": "Race Car",
    "2": "Top Hat",
    "3": "Scottie Dog",
    "4": "Cat",
    "5": "Penguin",
    "6": "Rubber Duck",
    "7": "T-Rex",
    "8": "Battleship"
}

def roll_dice():
    return [randint(1, 6) for _ in range(2)]

def get_num_players():
    while True:
        try:
            num = int(input("Enter number of players (2-8): "))
            if 2 <= num <= 8:
                return num
            else:
                print("Please enter a number between 2 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def choose_piece(available_pieces):
    print("Available pieces:")
    for key in available_pieces:
        print(f"{key}: {PIECES[key]}")
    while True:
        choice = input("Choose your piece by number: ")
        if choice in available_pieces:
            return choice
        else:
            print("Invalid or already chosen piece. Please select again.")

def player_info(used_pieces):
    name = input("Enter your name: ")
    available_pieces = [k for k in PIECES if k not in used_pieces]
    piece = choose_piece(available_pieces)
    return name, piece

def save_player_data(player_info, filename="players.json"):
    with open(filename, "w") as f:
        json.dump(player_info, f, indent=4)

def main():
    num_players = get_num_players()
    players = []
    used_pieces = set()
    for i in range(num_players):
        print(f"\nPlayer {i+1}:")
        name, piece = player_info(used_pieces)
        players.append({"name": name, "piece": PIECES[piece]})
        used_pieces.add(piece)
    save_player_data(players)
    print("\nPlayer data saved to players.json.")

if __name__ == "__main__":
    main()