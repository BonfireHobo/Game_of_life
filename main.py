from game_board import GameBoard

def main():
    # Game Info // Create game
    game = GameBoard(15, 15) # (row, column)
    exit_game = False
    
    # Game loop
    while not exit_game:
        # Print game board and info
        game.draw_board()
        print(game)

        # Update or quit
        _continue = input("Press enter to continue, or type 'q' and press enter to stop\n")
        if _continue.lower() == "q":
            exit_game = True
        else:
            game.update()


# Starts Game
if __name__ == "__main__":
    main()