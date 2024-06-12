class Player:
    """
    Create an instance of a player. 
    Initializes the player's rack, 
    Allows you to set/get a player name.
    """
    def __init__(self, bag):
        # Creates the player's rack by creating an instance of that class.
        # Takes the bag as an argument, in order to create the rack.
        self.name = ""
        self.rack = Rack(bag)
        self.score = 0

    def increase_score(self, increase):
        self.score += increase

    def get_score(self):
        return self.score

    def get_rack_str(self):
        # Returns the player's rack.
        return self.rack.get_rack_str()

    def get_rack_arr(self):
        # Returns the player's rack in the form of an array.
        return self.rack.get_rack_arr()
