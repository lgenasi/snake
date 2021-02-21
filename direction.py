from enum import Enum


class Direction(Enum):
    UP = 'Up'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'

    def opposite(self):
        if self.name == 'UP':
            return Direction.DOWN
        if self.name == 'DOWN':
            return Direction.UP
        if self.name == 'LEFT':
            return Direction.RIGHT
        if self.name == 'RIGHT':
            return Direction.LEFT