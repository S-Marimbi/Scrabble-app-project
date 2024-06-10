# Defining the tile bag (score-worth of each letter-tile)
bag = {
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

    def take_from_bag(self):
        # Removes a tile from the bag and provides it to the user for restocking the hand
        return self.bag.pop()

    def get_remaining_tiles(self):
        # Provides the number of tiles remaining in the bag.
        return len(self.bag)

