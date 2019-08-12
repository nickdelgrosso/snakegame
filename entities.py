from typing import NewType, Sequence, Union, List, Tuple
from enum import Enum

XY = NewType('XY', Tuple[int, int])
Board = NewType('Board', XY)


class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


Snake = NewType("Snake", Sequence[Union[XY, None]])
Food = NewType("Food", XY)
FoodCollection = NewType('FoodCollection', List[Food])


class SnakeAction:

    def move(snake: Snake, direction: Direction) -> Snake:
        head = snake[0]
        new_head: XY = (head[0] + direction[0], head[1] + direction[1])
        return (new_head,) + tuple(snake)[:-1] if len(snake) == 1 or new_head != snake[1] else tuple(snake)

    def grow(snake: Snake) -> Snake:
        return snake + (None,)

    def touches(snake: Snake, food: Food) -> bool:
        return food in snake

    def is_inside(snake: Snake, board: Board) -> bool:
        head = snake[0]
        return 0 <= head[0] < board[0] and 0 <= head[1] < board[1]


