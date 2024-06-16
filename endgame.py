# End the game when there are no tiles left in the bag and players can't make a move.
def game_over(players):
    return all(not player.tiles for player in players)

while not game_over(players):
    player_turn(players[current_player], board, tile_bag)
    current_player = (current_player + 1) % len(players)

print("Game over!")
for player in players:
    print(f"{player.name}'s final score: {player.score}")
