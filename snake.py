from coords import Coords


class Snake:
    def __init__(self, canvas, length=3, size=20):
        self.canvas = canvas

        self.length = length
        self.size = size

        self.direction = 'Right'
        self.next_direction = self.direction

        self.body_parts = []

    @property
    def head(self):
        return self.body_parts[-1]

    @property
    def head_coords(self):
        return self.get_coords(self.head)

    @property
    def tail(self):
        return self.body_parts[0]

    @property
    def tail_coords(self):
        return self.get_coords(self.tail)

    @property
    def next_head_coords(self):
        next_head_coords = self.get_next_coords(coords=self.head_coords, direction=self.direction)
        return next_head_coords

    def get_coords(self, body_part):
        coords = self.canvas.coords(body_part)
        return Coords(x1=coords[0], y1=coords[1], x2=coords[2], y2=coords[3])

    def get_next_coords(self, coords, direction):
        if direction == 'Right':
            coords.x1 += self.size
            coords.x2 += self.size
        if direction == 'Left':
            coords.x1 -= self.size
            coords.x2 -= self.size
        if direction == 'Up':
            coords.y1 -= self.size
            coords.y2 -= self.size
        if direction == 'Down':
            coords.y1 += self.size
            coords.y2 += self.size
        return coords

    def spawn(self, start_x, start_y):
        head = self.canvas.create_rectangle(
            start_x,
            start_y,
            start_x + self.size,
            start_y + self.size,
            fill='dark green', outline='black'
        )
        self.body_parts.insert(0, head)

        for x in range(0, self.length):
            body_part_coords = self.get_next_coords(coords=self.tail_coords, direction=opposite(self.direction))
            self.add_body_part(body_part_coords)

    def add_body_part(self, coords):
        body_part = self.canvas.create_rectangle(
            coords.x1,
            coords.y1,
            coords.x2,
            coords.y2,
            fill='light green', outline='black'
        )
        self.body_parts.insert(0, body_part)
        return body_part

    def grow(self):
        tail_parent_coords = self.get_coords(self.body_parts[1])

        if self.tail_coords.y1 < tail_parent_coords.y1:
            new_tail_coords = self.get_next_coords(coords=self.tail_coords, direction='Up')
        elif self.tail_coords.y1 > tail_parent_coords.y1:
            new_tail_coords = self.get_next_coords(coords=self.tail_coords, direction='Down')
        elif self.tail_coords.x1 < tail_parent_coords.x1:
            new_tail_coords = self.get_next_coords(coords=self.tail_coords, direction='Left')
        elif self.tail_coords.x1 > tail_parent_coords.x1:
            new_tail_coords = self.get_next_coords(coords=self.tail_coords, direction='Right')

        self.add_body_part(new_tail_coords)

    def hit_wall(self):
        if self.direction == 'Right' and self.next_head_coords.x2 > int(self.canvas['width']):
            return True
        elif self.direction == 'Left' and self.next_head_coords.x1 < 0:
            return True
        elif self.direction == 'Up' and self.next_head_coords.y1 < 0:
            return True
        elif self.direction == 'Down' and self.next_head_coords.y2 > int(self.canvas['height']):
            return True
        else:
            return False

    def hit_body(self):
        for body_part in self.body_parts:
            if (self.next_head_coords == self.get_coords(body_part)) and (body_part != self.tail):
                return True
        return False

    def check_if_dead(self):
        if self.hit_wall():
            return True
        if self.hit_body():
            return True
        return False

    def set_direction(self):
        if self.next_direction != opposite(self.direction):
            self.direction = self.next_direction

    def move_body_part(self, body_part, new_coords):
        self.canvas.coords(body_part, new_coords.x1, new_coords.y1, new_coords.x2, new_coords.y2)

    def move(self):
        for i, body_part in enumerate(self.body_parts):
            if body_part != self.head:
                parent_body_part_coords = self.get_coords(self.body_parts[i + 1])
                self.move_body_part(body_part=body_part, new_coords=parent_body_part_coords)
            else:
                self.move_body_part(body_part=self.head, new_coords=self.next_head_coords)


def opposite(direction):
    if direction == 'Right':
        return 'Left'
    elif direction == 'Left':
        return 'Right'
    elif direction == 'Up':
        return 'Down'
    elif direction == 'Down':
        return 'Up'
