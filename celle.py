class Celle:
    def __init__(self):
        # 0 = dead // 1 = alive
        self.status = 0

    # Change status to dead
    def set_dead(self):
        self.status = 0

    # Change status to alive
    def set_alive(self):
        self.status = 1

    # Check if cell is alive
    def is_alive(self):
        if self.status == 1:
            return True
        else:
            return False

    # Return  current sign for cell
    def get_sign(self):
        if self.status == 1:
            return "0"
        else:
            return "."