#intializing the game
#initializing the board,tile bag, and players
board = initialize_board()
tile_bag = initialize_tile_bag()
players = [Player('Human', tile_bag), Player('Computer', tile_bag)]
current_player = 0
