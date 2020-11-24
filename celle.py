class Celle:
    def __init__(self):
        # Alive status for cell
        self.status = False


    # Change status to dead
    def set_dead(self):
        self.status = False


    # Change status to alive
    def set_alive(self):
        self.status = True


    # Check if cell is alive
    def is_alive(self):
        status = True if self.status else False
        return status


    # Return  current sign for cell
    def get_sign(self):
        sign = "0" if self.status else "."
        return sign