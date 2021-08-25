


game = Tictactoe_class.Tictactoe()
game.make_move(-1, (0, 0))
game.make_move(-1, (1, 1))
game.make_move(-1, (2, 2))
print(game.check_end())
print(game.board)
print()

game.reset_game()
game.make_move(1, (0, 0))
game.make_move(1, (1, 1))
game.make_move(1, (2, 2))
print(game.check_end())
print(game.board)
print()

game.reset_game()
game.make_move(1, (0, 0))
game.make_move(1, (0, 1))
game.make_move(-1, (0, 2))
game.make_move(1, (1, 0))
game.make_move(1, (1, 1))
game.make_move(-1, (1, 2))
game.make_move(1, (2, 0))
game.make_move(-1, (2, 1))
game.make_move(-1, (2, 2))
print(game.check_end())
print(game.board)
print()



game.reset_game()
game.make_move(-1, (0, 0))
game.make_move(-1, (0, 2))
game.make_move(1, (1, 0))
game.make_move(-1, (1, 2))
game.make_move(1, (2, 0))
game.make_move(1, (2, 0))
game.make_move(1, (2, 2))

game.make_move(1, (0, 1))
game.make_move(-1, (1, 1))
game.make_move(-1, (2, 1))

print(game.check_end())
print(game.board)
print()
game.reset_game()
game.make_move(1, (0, 0))
game.make_move(1, (1, 1))
game.make_move(1, (2, 2))
print(game.board)
print(game.get_valid_move())

