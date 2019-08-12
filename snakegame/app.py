from time import time
from snakegame.entities import Game, GameOver
import pyxel as px


class App:

    controls = {px.KEY_UP: 'up', px.KEY_DOWN: 'down', px.KEY_LEFT: 'left', px.KEY_RIGHT: 'right'}

    def __init__(self, width = 10, height = 10, speed=0.2):
        self.width = width
        self.height = height
        self.speed = speed
        self.game_over = False
        self.new_game()
        px.init(width=width, height=height, caption="Snake")

    def new_game(self):
        self.game = Game.create(width=self.width, height=self.height, speed=self.speed)

    def update(self):

        if not self.game_over:
            try:
                for control, direction in self.controls.items():
                    if px.btn(control):
                        self.game.set_direction(direction=direction)

                self.game.step(time=time())
            except GameOver:
                self.game_over = True
        else:
            if px.btn(px.KEY_SPACE):
                self.new_game()
                self.game_over = False

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



