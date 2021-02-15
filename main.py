from tkinter import *


class Snake:
    def __init__(self, canvas):
        self.canvas = canvas

        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.handle_keypress)

        self.direction = 'Right'
        self.next_direction = self.direction

        self.length = 11
        self.size = 20
        self.body_parts = []

        self.build_snake(start_x=300, start_y=300)

    @property
    def head(self):
        return self.body_parts[-1]

    @property
    def head_coords(self):
        return self.canvas.coords(self.head)
    
    @property
    def next_head_coords(self):
        next_head_coords = self.head_coords
        if self.direction == 'Right':
            next_head_coords[0] += self.size
            next_head_coords[2] += self.size
        if self.direction == 'Left':
            next_head_coords[0] -= self.size
            next_head_coords[2] -= self.size
        if self.direction == 'Up':
            next_head_coords[1] -= self.size
            next_head_coords[3] -= self.size
        if self.direction == 'Down':
            next_head_coords[1] += self.size
            next_head_coords[3] += self.size
        return next_head_coords

    def build_snake(self, start_x, start_y):
        head = canvas.create_rectangle(
            start_x, start_y, (start_x + self.size), (start_y + self.size),
            fill='dark green', outline='black'
        )
        self.body_parts.insert(0, head)

        for x in range(0, self.length):
            parent_body_part = self.canvas.coords(self.body_parts[0])
            body_part = self.canvas.create_rectangle(
                parent_body_part[0] - self.size, parent_body_part[1],
                parent_body_part[2] - self.size, parent_body_part[3],
                fill='light green', outline='black'
            )
            self.body_parts.insert(0, body_part)

    def handle_keypress(self, event):
        self.next_direction = event.keysym

    def valid_next_direction(self):
        if (self.next_direction == 'Right' and self.direction == 'Left') or \
                (self.next_direction == 'Left' and self.direction == 'Right') or \
                (self.next_direction == 'Up' and self.direction == 'Down') or \
                (self.next_direction == 'Down' and self.direction == 'Up'):
            return False
        else:
            return True

    def hit_wall(self):
        if self.direction == 'Right' and self.next_head_coords[2] > game_width:
            return True
        elif self.direction == 'Left' and self.next_head_coords[0] < 0:
            return True
        elif self.direction == 'Up' and self.next_head_coords[1] < 0:
            return True
        elif self.direction == 'Down' and self.next_head_coords[3] > game_height:
            return True
        else:
            return False

    def hit_body(self):
        for body_part in self.body_parts[1:]:
            if self.next_head_coords == self.canvas.coords(body_part):
                return True
        return False

    def check_if_dead(self):
        if self.hit_wall():
            return True
        if self.hit_body():
            return True
        return False

    def draw(self):
        if self.valid_next_direction():
            self.direction = self.next_direction
        else:
            self.direction = self.direction

        if self.check_if_dead():
            game_over_text = self.canvas.create_text(game_width/2, game_height/2)
            self.canvas.itemconfig(game_over_text, text='GAME OVER')
            self.canvas.itemconfig(self.head, fill='red')
            return

        # Update body
        for i, body_part in enumerate(self.body_parts):
            if body_part != self.head:
                parent_body_part = self.canvas.coords(self.body_parts[i + 1])
                self.canvas.coords(
                    body_part,
                    parent_body_part[0],
                    parent_body_part[1],
                    parent_body_part[2],
                    parent_body_part[3],
                )
            else:
                self.canvas.coords(
                    self.head,
                    self.next_head_coords[0],
                    self.next_head_coords[1],
                    self.next_head_coords[2],
                    self.next_head_coords[3]
                )

        self.canvas.after(1000, self.draw)


if __name__ == '__main__':
    window = Tk()
    window.title('Snake')
    window.resizable(0, 0)
    window.attributes('-topmost', True)  # TODO: remove after development

    game_width, game_height = 600, 600

    canvas = Canvas(window, width=game_width, height=game_height, bd=0)
    canvas.pack()

    snake = Snake(canvas)
    snake.draw()

    window.mainloop()
