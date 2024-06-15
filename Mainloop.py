from lib.TileBag import Bag, tile_distribution
from lib.BoardClass import Board
from lib.PlayerClass import Player
import random

# Load the word list from dictionary.txt
def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip().upper() for line in file]

# Validate if a word is in the dictionary
def is_valid_word(word, word_list):
    return word in word_list

# Generate a valid random word from the computer's rack
def generate_computer_word(rack, word_list):
    rack_letters = [tile.get_letter() for tile in rack]
    random.shuffle(rack_letters)
    for word in word_list:
        if all(rack_letters.count(char) >= word.count(char) for char in word):
            return word
    return None

# Generate a hint for the human player
def generate_hint(rack, word_list):
    rack_letters = [tile.get_letter() for tile in rack]
    for word in word_list:
        if all(rack_letters.count(char) >= word.count(char) for char in word):
            return word
    return None

def main():
    # Load words from the dictionary.txt
    word_list = load_words("dictionary.txt")  
    tile_bag = Bag(tile_distribution)
    board = Board()
    human_player = Player(tile_bag)
    computer_player = Player(tile_bag)
    players = [human_player, computer_player]
    current_player_index = 0
    pass_count = [0]  # Using a list to keep track of pass count

    def print_game_state():
        print("Current Board:")
        print(board.get_board())
        print(f"Human's hand: {human_player.get_rack_str()}")
        print(f"Computer's hand: {computer_player.get_rack_str()}")
        print(f"Remaining tiles in bag: {tile_bag.get_remaining_tiles()}")

    # Human turn with a pass and hint option
    # Human player chooses the direction and placement of tiles
    def human_turn():
        print("Human's turn")
        print_game_state()
        while True:
            action = input("Enter 'P' to pass, 'H' for a hint, or any word to play: ").upper()
            if action == 'P':
                pass_count[0] += 1
                return 'pass'
            elif action == 'H':
                hint = generate_hint(human_player.get_rack_arr(), word_list)
                print(f"Hint: try to form a word with these letters - {hint}")
            else:
                word = action
                if not is_valid_word(word, word_list):
                    print("Invalid word. Please try again.")
                    continue
                direction = input("Enter direction (right/down): ").lower()
                row = int(input("Enter starting row (0-14): "))
                col = int(input("Enter starting column (0-14): "))
                board.place_word(word, (row, col), direction, human_player)
                pass_count[0] = 0
                return 'played'
                
    # Human turn with a pass and hint option
    # Human player chooses the direction and placement of tiles
    def computer_turn():
        print("Computer's turn")
        rack_arr = computer_player.get_rack_arr()
        word = generate_computer_word(rack_arr, word_list)
        if word:
            direction = random.choice(['right', 'down'])
            row = random.randint(0, 14)
            col = random.randint(0, 14)
            board.place_word(word, (row, col), direction, computer_player)
            print(f"Computer placed: {word} at ({row}, {col}) {direction}")
            pass_count[0] = 0
            return 'played'
        else:
            print("Computer could not find a valid word to play.")
            pass_count[0] += 1
            return 'pass'

    # Checking game conditions
    while True:
        current_player = players[current_player_index]
        if current_player == human_player:
            human_turn()
        else:
            computer_turn()

        # Check for game over conditions
        if pass_count [0] >= 2:
            print("Both players passed. Game over!")
            break
            
        if tile_bag.get_remaining_tiles() == 0 and (not human_player.get_rack_arr() or not computer_player.get_rack_arr()):
            print("Game over!")
            break

        # Switch turns
        current_player_index = 1 - current_player_index

        print_game_state()

if __name__ == "__main__":
    main()
