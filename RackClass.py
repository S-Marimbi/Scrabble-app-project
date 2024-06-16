from lib.TileBag import Bag

class Rack:
    """
    Creates each player's hand. 
    Allows players to add, remove and replenish the number of tiles in their hand.
    """
    def __init__(self, bag):
        # Takes the bag from which the racks tiles will come as an argument.
        self.rack = []
        self.bag = bag
        self.initialize()

    def add_to_rack(self):
        self.rack.append(self.bag.take_from_bag())

    def initialize(self):
        # Adds the initial 7 tiles to the player's hand.
        [self.add_to_rack() for _ in range(7)]

    def get_rack_str(self):
        return ", ".join(map(str, (item.get_letter() for item in self.rack)))

    def get_rack_arr(self):
        return self.rack

    def remove_from_rack(self, tile):
        # Removes a tile from the rack (for example, when a tile is being played).
        self.rack.remove(tile)

    def get_rack_length(self):
        # Returns the number of tiles left in the rack.
        return len(self.rack)

    def replenish_rack(self):
        # Adds tiles to the rack after a turn returning it to 7 tiles
        while self.get_rack_length() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_to_rack()
