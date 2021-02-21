import tkinter as tk
from tkinter import ttk

from direction import Direction
from snake import Snake
from food import Food


class Game:
    def __init__(self, width=400, height=400, speed=150):
        self.width = width
        self.height = height
        self.speed = speed
        self.score = 0

        self.canvas = tk.Canvas(window, width=self.width, height=self.height, bd=0)
        self.canvas.pack()
        self.canvas.focus_set()

        self.canvas.bind('<Up>', self.set_snake_direction)
        self.canvas.bind('<Down>', self.set_snake_direction)
        self.canvas.bind('<Left>', self.set_snake_direction)
        self.canvas.bind('<Right>', self.set_snake_direction)
        self.canvas.bind('r', self.restart)

        self.snake = Snake(self.canvas)
        self.snake.spawn()

        self.food = Food(self.canvas)
        self.food.spawn()

    def restart(self, event):
        self.canvas.delete('all')
        self.score = 0
        self.snake = Snake(self.canvas)
        self.snake.spawn()
        self.food.respawn()
        self.draw()

    def set_snake_direction(self, event):
        self.snake.next_direction = Direction(event.keysym)

    def end(self):
        game_over_text = self.canvas.create_text(self.width/2, self.height/2, justify=tk.CENTER)
        self.canvas.itemconfig(game_over_text, text=f'GAME OVER\nSCORE: {self.score}\nPress <R> to restart')
        self.canvas.itemconfig(self.snake.head, fill='red')

    def snake_has_eaten_food(self):
        if (self.snake.head_coords.x1 < self.food.coords.x1 < self.snake.head_coords.x2) and \
                (self.snake.head_coords.y1 < self.food.coords.y1 < self.snake.head_coords.y2):
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
            self.food.respawn()
            self.snake.grow()
            self.score += 10

        self.canvas.after(self.speed, self.draw)


def start():
    start_button.destroy()
    game = Game()
    game.draw()


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Snake')
    window.resizable(0, 0)
    window.geometry('400x400')

    start_button = ttk.Button(window, text="START", command=start)
    start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # TODO: remove after development
    # import os
    # os.system("open -a Python")
    # window.attributes('-topmost', True)

    window.mainloop()
