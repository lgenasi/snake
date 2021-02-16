import random


class Food:
    def __init__(self, canvas, size=10):
        self.canvas = canvas
        self.size = size
        self.id = None

    @property
    def coords(self):
        return self.canvas.coords(self.id)

    def spawn(self):
        game_width = int(self.canvas['width'])
        game_height = int(self.canvas['height'])

        random_multiplier_x = random.randint(0, (int(game_width / 20)) - 1)
        random_multiplier_y = random.randint(0, (int(game_height / 20)) - 1)

        random_x1 = (20 * random_multiplier_x) + 5
        random_y1 = (20 * random_multiplier_y) + 5

        # random_x1 = 365
        # random_y1 = 305

        self.id = self.canvas.create_oval(
            random_x1, random_y1,
            random_x1 + self.size, random_y1 + self.size,
            fill='red', outline='blue'
        )