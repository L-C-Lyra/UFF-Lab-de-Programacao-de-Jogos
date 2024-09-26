from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import random

game_window = Window(600, 600)
window_title = 'Pong of Lucas Correa'

game_window.set_background_color([0, 0, 255])
game_window.set_title(window_title)

pong_ball = Sprite('./src/assets/pong_ball.png', 1)

pong_ball.x = (game_window.width / 2) - (pong_ball.width / 2)
pong_ball.y = (game_window.height / 2) - (pong_ball.height / 2)

vel_x = random.uniform(0.6, 0.8)
vel_y = random.uniform(0.6, 0.8)

# Game Loop:
while True:
    pong_ball.x = pong_ball.x + vel_x
    pong_ball.y = pong_ball.y + vel_y

    if(pong_ball.x >= (game_window.width - pong_ball.width) or pong_ball.x <= 0):
        vel_x *= -1
    if(pong_ball.y >= (game_window.height - pong_ball.height) or pong_ball.y <= 0):
        vel_y *= -1

    game_window.set_background_color([0, 0, 255])
    pong_ball.draw()
    game_window.update()
