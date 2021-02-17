import random

from coords import Coords


class Food:
    def __init__(self, canvas, size=10):
        self.canvas = canvas
        self.size = size
        self.id = None

    @property
    def coords(self):
        coords = self.canvas.coords(self.id)
        return Coords(x1=coords[0], y1=coords[1], x2=coords[2], y2=coords[3])

    def respawn(self):
        self.canvas.delete(self.id)
        self.spawn()

    def spawn(self):
        game_width = int(self.canvas['width'])
        game_height = int(self.canvas['height'])

        random_multiplier_x = random.randint(0, (int(game_width / 20)) - 1)
        random_multiplier_y = random.randint(0, (int(game_height / 20)) - 1)

        random_x1 = (20 * random_multiplier_x) + 5
        random_y1 = (20 * random_multiplier_y) + 5

        self.id = self.canvas.create_oval(
            random_x1, random_y1,
            random_x1 + self.size, random_y1 + self.size,
            fill='red', outline='blue'
        )
