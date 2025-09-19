from random import randint
import json
import os

def game_state(data, filename="game_state.json"):
    """Saves the entire game state as a JSON file"""
    with open(filename, "w") as game_state_file:
        json.dump(data, game_state_file, indent=4)

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
    """Rolls two six-sided dice and returns their values as a list"""
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
    bank = 1500
    properties = []
    return name, piece, bank, properties

def save_player_data(players, filename="players.json"):
    """Saves player data as a JSON file"""
    with open(filename, "w") as f:
        json.dump(players, f, indent=4)

def load_player_data(filename="players.json"):
    """Loads player data from a JSON file"""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def game_loop(players):
    turn = 0
    
    while True:
        current_player = players[turn % len(players)]
        player_enter = input(f"\n{current_player['name']}'s turn. Press X to roll the dice or Q to access the menu: ")
         
        if player_enter != "X" and player_enter != "x" and player_enter != "q":
            print("Please enter a vaild input.")
            player_enter = input(f"\n{current_player['name']}'s turn. Press X to roll the dice : ")
            continue
        elif player_enter == "X" or player_enter == "x":
            dice = roll_dice()

        print(f"{current_player['name']} rolled {dice[0]} and {dice[1]} (Total: {sum(dice)})")

        # Load the board
        try:
            with open("property.json", "r") as f:
                board = json.load(f)
        except FileNotFoundError:
            print("property.json not found. Exiting game loop.")
            return

        # Track player position
        if "position" not in current_player:
            current_player["position"] = 0

        board_size = len(board)
        move_steps = sum(dice)
        current_player["position"] = (current_player["position"] + move_steps) % board_size
        current_property = board[current_player["position"]]

        print(f"{current_player['name']} landed on {current_property['name']} (Position: {current_player['position']})")

        if player_enter == "q":

            while True:
                print("\nMenu:")
                print("1. View property details")
                print("2. Exit game")
                print("3. Continue turn")
                menu_choice = input("Choose an option (1-3): ").strip()
                if menu_choice == "1":
                    print(json.dumps(current_property, indent=4))
                elif menu_choice == "2":
                    print("Exiting game. Progress saved.")
                    save_player_data(players)
                    False
                    exit()
                elif menu_choice == "3":
                    break
                else:
                    print("Invalid choice. Please select again.")

        # Check if player passed GO (position 0) after the first turn
        if "last_position" in current_player:
            if current_player["position"] < current_player["last_position"]:
                current_player["bank"] += 200
                print(f"{current_player['name']} passed GO! +$200 (Bank: ${current_player['bank']})")
        current_player["last_position"] = current_player["position"]

        # Save progress every turn
        save_player_data(players)

        turn += 1

def new_game():
    num_players = get_num_players()
    players = []
    used_pieces = set()
    for i in range(num_players):
        print(f"\nPlayer {i+1}:")
        name, piece, bank, properties = player_info(used_pieces)
        players.append({
            "name": name,
            "piece": PIECES[piece],
            "bank": bank,
            "properties": []
        })
        used_pieces.add(piece)
    save_player_data(players)
    print("\nNew game started and saved to players.json.")
    return players

def main():
    print("Welcome to Monopoly!")
    if os.path.exists("players.json"):
        choice = input("Load saved game? (y/n): ").strip().lower()
        if choice == "y":
            players = load_player_data()
            print("Game loaded.")
        else:
            players = new_game()
    else:
        players = new_game()

    game_loop(players)

if __name__ == "__main__":
    main()
