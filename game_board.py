from random import randint
from celle import Celle

class GameBoard:
    def __init__(self, row, column):
        # Game bords size
        self.row = row
        self.column = column

        # Current generation
        self.generation = 0

        # List of the game board
        self.board = []

        # Create game borad
        for _ in range(self.row):
            self.board_rows = []      
            for _ in range(self.column):
                self.board_rows.append(Celle())
            self.board.append(self.board_rows)

        # Go to generate
        self.generate()


    # Returns info about game
    def __str__(self):
        return (f"Generation: {self.generation} // Cells alive: {self.total_cells_alive()}")


    # Generate first generation
    def generate(self) :
        for i in range(self.row):
            for j in range(self.column):
                birth_status = randint(0, 2)  # 1/3 Chance of cell being alive at birth
                if birth_status == 2:
                    self.board[i][j].set_alive()    


    # Print out curent board
    def draw_board(self):
        for i in range(self.row):
            for j in range(self.column):
                print(self.board[i][j].get_sign(), end= "")
            print("")


    # Update generation
    def update(self):
        # List of cells that will change status
        new_dead_cells = []
        new_alive_cells = []

        # Find neighbor to all cells
        for i in range(self.row):
            for j in range(self.column):
                # Current cell
                cell_status = self.board[i][j].is_alive()

                # Checking alive neighbors to current cell
                alive_neighbors = self.find_neighbor(i, j)

                # Checks game rules for living cell
                if cell_status:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_dead_cells.append(self.board[i][j])
                # Check game rules for dead cell
                elif not cell_status and alive_neighbors == 3:
                    new_alive_cells.append(self.board[i][j])

        # Changing cell status
        for cell in new_dead_cells:
            cell.set_dead()

        for cell in new_alive_cells:
            cell.set_alive()

        # Update generations
        self.generation += 1


    # Find neighbors to cell
    def find_neighbor(self, row, column):
        # Count of living neighbors
        alive_neighbors = 0

        # Loop through neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_row = row + i
                neighbor_column = column + j

                # Do not count itself
                if not (neighbor_row == row and neighbor_column == column):
                    # Check if it's inside the map
                    if not (neighbor_row < 0 or neighbor_row > self.row-1 or
                            neighbor_column < 0 or neighbor_column > self.column-1):
                            # Check if its alive
                        if self.board[neighbor_row][neighbor_column].is_alive() == True:
                            alive_neighbors += 1

        # Returns living neighbors
        return alive_neighbors


    # Count current cells alive
    def total_cells_alive(self):
        cells_alive = 0
        for i in range(self.row):
            for j in range(self.column):
                if self.board[i][j].is_alive() == True:
                    cells_alive += 1
        return cells_alive              