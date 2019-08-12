from typing import NewType, Sequence, Union, List, Tuple, NamedTuple
from enum import Enum
from dataclasses import dataclass
from random import randrange

XY = NewType('XY', Tuple[int, int])
Board = NewType('Board', XY)
Speed = NewType('Speed', float)

Direction = NewType("Direction", XY)
UP: Direction = (0, 1)
DOWN: Direction = (0, -1)
LEFT: Direction = (-1, 0)
RIGHT: Direction = (1, 0)


Snake = NewType("Snake", Sequence[Union[XY, None]])
Food = NewType("Food", XY)

class GameOver(Exception):
    pass

def move(snake: Snake, direction: Direction) -> Snake:
    head = snake[0]
    new_head: XY = (head[0] + direction[0], head[1] + direction[1])
    return (new_head,) + tuple(snake)[:-1] if len(snake) == 1 or new_head != snake[1] else tuple(snake)


def grow(snake: Snake) -> Snake:
    return snake + (None,)


def touches_food(snake: Snake, food: Food) -> bool:
    return food in snake


def touches_self(snake: Snake) -> bool:
    return len(set(snake)) != len(snake)


def is_inside(snake: Snake, board: Board) -> bool:
    head = snake[0]
    return 0 <= head[0] < board[0] and 0 <= head[1] < board[1]


@dataclass
class Game:
    board: Board
    snake: Snake
    food: Union[Food, None]
    speed: Speed
    direction: Direction
    speed_increase: float

    def __post_init__(self):
        self.last_step_time = 0.  # Time since last frame (for monitoring time)

    @classmethod
    def create(cls, width: int, height: int, speed: float = 0.5):
        return cls(board = Board(XY((width, height)),),
                   snake=((1, 1),),
                   food=Food(XY((3, 3))),
                   speed=Speed(speed),
                   direction=UP,
                   speed_increase=1.05)

    def step(self, time) -> None:

        if time - self.last_step_time < self.speed:
            return
        self.last_step_time = time

        self.snake = move(snake=self.snake, direction=self.direction)
        if not is_inside(self.snake, self.board):
            raise GameOver
        if touches_self(self.snake):
            raise GameOver

        if touches_food(self.snake, self.food):
            self.snake = grow(self.snake)
            self.speed = self.speed / self.speed_increase

            food = tuple(randrange(c) for c in self.board)
            while touches_food(snake=self.snake, food=food):
                food = tuple(randrange(c) for c in self.board)
            self.food = food

    @property
    def width(self):
        return self.board[0]

    @property
    def height(self):
        return self.board[1]

    def set_direction(self, direction: str):
        """Sets direction to "up", "left", "down", "right".  """
        directions = {'up': UP, 'left': LEFT, 'right': RIGHT, 'down': DOWN}
        opposite_direction = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}
        new_direction = directions[direction.lower()]
        if new_direction != self.direction and new_direction != opposite_direction[self.direction]:
            print(self.direction, new_direction)
            self.direction = new_direction
