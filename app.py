from time import time
from typing import List, Tuple
from entities import Direction, Board, Snake, Food, Game, XY, Speed, move
import pyxel as px


class App:

    def __init__(self, width = 10, height = 10, speed=0.4):
        self.game = Game.create(width=width, height=height, speed=speed)
        px.init(width=width, height=height, caption="Snake")
        print(self.game.snake)
    def update(self):

        self.game.step(time=time())

    def draw(self):
        for x, y in self.game.snake:
            px.pix(x=x, y=self.game.height - y, col=3)

        food = self.game.food
        if food:
            px.pix(x=food[0], y=food[1], col=4)


    def run(self):
        px.run(draw=self.draw, update=self.update)



app = App()
app.run()