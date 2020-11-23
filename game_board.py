from random import randint
from celle import Celle

class GameBoard:
    def __init__(self, row, column):
        # Game bords general info
        self.row = row
        self.column = column
        self.generation = 0

        # Create game borad
        self.board = []
        for _ in range(self.row):
            self.board_rows = []      
            for _ in range(self.column):
                self.board_rows.append(Celle())
            self.board.append(self.board_rows)

        # Go to generate
        self.generate()


    # Returns current generation
    def __str__(self):
        return (f"Generation: {self.generation} // Cells alive: {self.total_cells_alive()}")


    # Generate first generation
    def generate(self) :
        for i in range(self.row):
            for j in range(self.column):
                birth_status = randint(0, 2)
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
        self.new_dead_cells = []
        self.new_alive_cells = []

        #Find neighbor to all cells
        for i in range(self.row):
            for j in range(self.column):
                self.find_neighbor(i, j)
                
        #Changing cell status
        for cell in self.new_dead_cells:
            cell.set_dead()

        for cell in self.new_alive_cells:
            cell.set_alive()

        # Update generations
        self.generation += 1


    # Updates next generation of cells
    def find_neighbor(self, row, column):
        # Variables related to curent cell
        alive_neighbors = 0
        cell_status = self.board[row][column].is_alive()

        # Loop through neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if i == 0 and j == 0:
                        continue
                    elif self.board[row + i][column + j].is_alive() == True:
                        alive_neighbors += 1
                except IndexError:
                    continue

        # Checks with game rules for living cell
        if cell_status == True:
            if alive_neighbors < 2 or alive_neighbors > 3:
                self.new_dead_cells.append(self.board[row][column])

        # Checks with game rules for death cell
        elif cell_status == False and alive_neighbors == 3:
            self.new_alive_cells.append(self.board[row][column])


    # Count current cells alive
    def total_cells_alive(self):
        cells_alive = 0
        for i in range(self.row):
            for j in range(self.column):
                if self.board[i][j].is_alive() == True:
                    cells_alive += 1
        return cells_alive              