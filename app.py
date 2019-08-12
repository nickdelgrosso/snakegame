from time import time
from entities import Game
import pyxel as px


class App:

    controls = {px.KEY_UP: 'up', px.KEY_DOWN: 'down', px.KEY_LEFT: 'left', px.KEY_RIGHT: 'right'}

    def __init__(self, width = 10, height = 10, speed=0.4):
        self.game = Game.create(width=width, height=height, speed=speed)
        px.init(width=width, height=height, caption="Snake")

    def update(self):
        for control, direction in self.controls.items():
            if px.btn(control):
                self.game.set_direction(direction=direction)

        self.game.step(time=time())

    def draw(self):
        px.cls(0)
        for pos in self.game.snake:
            if pos:
                x, y = pos
                px.pix(x=x, y=self.game.height - y - 1, col=3)

        food = self.game.food
        if food:
            px.pix(x=food[0], y=self.game.height - food[1] - 1, col=4)


    def run(self):
        px.run(draw=self.draw, update=self.update)



app = App()
app.run()