class Coords:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __eq__(self, other):
        return (self.x1 == other.x1) and (self.y1 == other.y1) and (self.x2 == other.x2) and (self.y2 == other.y2)
