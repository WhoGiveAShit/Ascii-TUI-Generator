import os, sys

Platform = os.name
if Platform == "nt":
    os.system("cls")
else:
    os.system("clear")

def Position_Text(text, x, y):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))


class Generate:
    def __init__(self, shape, position_x, position_y, size) -> None:
        self.shape = shape
        self.position_x = int(position_x)
        self.position_y = int(position_y)
        self.size = int(size)
        self.zero = 0
    
    def Box(self):
        Position_Text("* " * self.size, self.position_x, self.position_y)
        for i in range(self.size):
            if self.zero == self.size - 1:
                Position_Text("* " * self.size, self.position_x + self.zero, self.position_y)
                break
            self.zero += 1
            Position_Text("*", self.position_x + self.zero, self.position_y)
            Position_Text("*", self.position_x + self.zero, self.position_y + self.size * 2 -2)
    
    def BoxClean(self):
        Position_Text("═" * self.size * 2, self.position_x, self.position_y)
        for i in range(self.size):
            Position_Text("╔", self.position_x, self.position_y)
            Position_Text("╗", self.position_x, self.position_y + self.size * 2)
            if self.zero == self.size - 1:
                Position_Text("═" * self.size * 2, self.position_x + self.zero + 1, self.position_y)
                Position_Text("╚", self.position_x + self.zero + 1, self.position_y)
                Position_Text("╝", self.position_x + self.zero + 1, self.position_y + self.size * 2)
                break
            self.zero += 1
            Position_Text("║", self.position_x + self.zero, self.position_y)
            Position_Text("║", self.position_x + self.zero, self.position_y + self.size * 2)
    
    def BarChart(self):
        Position_Text("═" * self.size * 2, self.position_x, self.position_y)
        for i in range(self.size):
            Position_Text("║", self.position_x - self.zero, self.position_y)
            self.zero += 1