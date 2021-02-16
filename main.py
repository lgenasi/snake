from tkinter import *

from snake import Snake
from food import Food


class Game:
    def __init__(self, width=600, height=600, speed=100):
        self.width = width
        self.height = height
        self.speed = speed

        self.canvas = Canvas(window, width=self.width, height=self.height, bd=0)
        self.canvas.pack()
        self.canvas.focus_set()

        self.canvas.bind('<Key>', self.set_snake_direction)

        self.snake = Snake(self.canvas)
        self.snake.spawn(start_x=300, start_y=300)

        self.food = Food(self.canvas)
        self.food.spawn()

    def set_snake_direction(self, event):
        self.snake.next_direction = event.keysym

    def end(self):
        game_over_text = self.canvas.create_text(self.width/2, self.height/2)
        self.canvas.itemconfig(game_over_text, text='GAME OVER')
        self.canvas.itemconfig(self.snake.head, fill='red')

    def snake_has_eaten_food(self):
        if (self.snake.head_coords[0] < self.food.coords[0] < self.snake.head_coords[2]) and \
                (self.snake.head_coords[1] < self.food.coords[1] < self.snake.head_coords[3]):
            return True
        else:
            return False

    def draw(self):
        self.snake.set_direction()

        if self.snake.check_if_dead():
            self.end()
            return

        self.snake.move()

        if self.snake_has_eaten_food():
            self.canvas.delete(self.food.id)
            self.food.spawn()
            self.snake.grow()

        self.canvas.after(self.speed, self.draw)


if __name__ == '__main__':
    window = Tk()
    window.title('Snake')
    window.resizable(0, 0)
    window.attributes('-topmost', True)  # TODO: remove after development

    game = Game()
    game.draw()

    window.mainloop()
