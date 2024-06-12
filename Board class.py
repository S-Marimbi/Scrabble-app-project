class Board:
    """
    Creates the Scrabble board.
    """
    def __init__(self):
        # Creates a 2-dimensional array that serves as the board, 
        # as well as adds in the premium squares.
        self.board = [["   " for _ in range(15)] for _ in range(15)]
        self.add_premium_squares()
        self.board[7][7] = " * "

    def get_board(self):
        # Returns the board in string form.
        board_str = ""
        for i in range(15):
            board_str += " | ".join(self.board[i]) + "\n"
        return board_str

    def add_premium_squares(self):
        """
         Adds all of the premium squares that influence the word's score.
         TWS- Triple Word Score
         DWS- Double Word Score
         TLS- Triple Letter Score
         DLS- Double Letter Score
        """
        premium_squares = {
            (0, 0): "TWS", (7, 0): "TWS", (14, 0): "TWS",
            (0, 7): "TWS", (14, 7): "TWS", (0, 14): "TWS",
            (7, 14): "TWS", (14, 14): "TWS",
            (1, 1): "DWS", (2, 2): "DWS", (3, 3): "DWS", (4, 4): "DWS",
            (1, 13): "DWS", (2, 12): "DWS", (3, 11): "DWS", (4, 10): "DWS",
            (13, 1): "DWS", (12, 2): "DWS", (11, 3): "DWS", (10, 4): "DWS",
            (13, 13): "DWS", (12, 12): "DWS", (11, 11): "DWS", (10, 10): "DWS",
            (1, 5): "TLS", (1, 9): "TLS", (5, 1): "TLS", (5, 5): "TLS",
            (5, 9): "TLS", (5, 13): "TLS", (9, 1): "TLS", (9, 5): "TLS",
            (9, 9): "TLS", (9, 13): "TLS", (13, 5): "TLS", (13, 9): "TLS",
            (0, 3): "DLS", (0, 11): "DLS", (2, 6): "DLS", (2, 8): "DLS",
            (3, 0): "DLS", (3, 7): "DLS", (3, 14): "DLS", (6, 2): "DLS",
            (6, 6): "DLS", (6, 8): "DLS", (6, 12): "DLS", (7, 3): "DLS",
            (7, 11): "DLS", (8, 2): "DLS", (8, 6): "DLS", (8, 8): "DLS",
            (8, 12): "DLS", (11, 0): "DLS", (11, 7): "DLS", (11, 14): "DLS",
            (12, 6): "DLS", (12, 8): "DLS", (14, 3): "DLS", (14, 11): "DLS"
        }
        for (x, y), value in premium_squares.items():
            self.board[x][y] = f" {value} "

    def place_word(self, word, location, direction, player):
        # Allows you to play words
        direction = direction.lower()
        word = word.upper()

        for i, letter in enumerate(word):
            x, y = location
            if direction == "right":
                y += i
            elif direction == "down":
                x += i
            self.board[x][y] = f" {letter} "

        # Removes tiles from player's rack and replaces them with tiles from the bag.
        for letter in word:
            for tile in player.get_rack_arr():
                if tile.get_letter() == letter:
                    player.remove_from_rack(tile)
        player.replenish_rack()

    def board_array(self):
        # Returns the 2-dimensional board array.
        return self.board
