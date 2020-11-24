from game_board import GameBoard

def main():
    # Game Info // Create game
    game = GameBoard(5, 5) # (row, column)
    exit_game = False
    
    # Game loop
    while not exit_game:
        # Print game board and info
        game.draw_board()
        print(game)

        # Update or quit
        continue_or_not = input("Press enter to continue, or type 'q' and press enter to stop\n")
        if continue_or_not.lower() == "q":
            exit_game = True
        else:
            game.update()


# Starts Game
if __name__ == "__main__":
    main()