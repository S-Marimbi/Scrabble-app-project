import random

# Defining the tile bag (score-worth of each letter-tile)
tile_bag = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 1,
    "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
    "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10, "#": 0
    # The "#" tile represents a blank tile holding zero points
}

# Container of all the letter tiles in the game
class Bag:
    def __init__(self, tile_bag):
        # Sets up the bag according to the specified quantities.
        self.tile_bag = tile_bag
        self.bag = []
        self.initialize_bag()

    def initialize_bag(self):
        # Fills the bag according to the defined quantities.
        for letter, quantity in self.tile_bag.items():
            self.bag.extend([letter] * quantity)
            random.shuffle(self.bag)  # Shuffle the bag to ensure randomness of letter picking

    def take_from_bag(self):
        # Removes a tile from the bag and provides it to the user for restocking the hand
        return self.bag.pop()

    def get_remaining_tiles(self):
        # Provides the number of tiles remaining in the bag.
        return len(self.bag)

    def distribute_tiles(self, number_of_tiles):
        # Distributes a specified number of tiles to a player.
        player_tiles = []
        for _ in range(number_of_tiles):
            if self.bag:
                player_tiles.append(self.take_from_bag())
        return player_tiles

# Create an instance of the Bag class
# bag_instance = Bag(tile_bag)

# Take tiles from the bag
# tile1 = bag_instance.take_from_bag()
# tile2 = bag_instance.take_from_bag()

# Check the number of remaining tiles
# remaining_tiles = bag_instance.get_remaining_tiles()

# print("Taken tiles:", tile1, tile2)
# print("Remaining tiles:", remaining_tiles)

# Distribute 7 tiles to a player's hand
# player_hand = bag_instance.distribute_tiles(7)
# print("Player's hand:", player_hand)
# print("Remaining tiles in bag:", bag_instance.get_remaining_tiles())
