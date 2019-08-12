from collections import deque
from typing import Tuple, Iterable, NewType, Sequence, NamedTuple, Union


class Coord(NamedTuple):
    x: int
    y: int

class Direction(NamedTuple):
    dx: int
    dy: int


UP = Direction(0, 1)
DOWN = Direction(0, -1)
LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)

Snake = NewType("Snake", Sequence[Union[Coord, None]])


def move_snake(snake: Snake, direction: Direction) -> Snake:
    head = snake[0]
    new_head = Coord(x=head.x + direction.dx, y=head.y + direction.dy)
    return (new_head,) + tuple(snake)[:-1] if len(snake) == 1 or new_head != snake[1] else tuple(snake)


def grow_snake(body: Snake) -> Snake:
    return body + (None,)


snake: Snake = (Coord(0, 0),)
snake2 = move_snake(snake, UP)
snake3 = grow_snake(snake2)
snake4 = grow_snake(snake3)
snake5 = move_snake(snake4, LEFT)
snake6 = move_snake(snake5, UP)
snake7 = move_snake(snake6, UP)
snake8 = move_snake(snake7, DOWN)
print(snake, snake2, snake3, snake4, snake5, snake6, snake7, snake8, sep='\n')