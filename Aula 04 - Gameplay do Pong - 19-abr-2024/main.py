from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import random

game_window = Window(600, 600)

game_background = GameImage('./src/assets/game_background.png')

game_keyboard = game_window.get_keyboard()

game_window.set_title('Pong of Lucas Correa')

pong_ball = Sprite('./src/assets/pong_ball.png', 1)
pong_l_racket = Sprite('./src/assets/pong_racket.png', 1)
pong_r_racket = Sprite('./src/assets/pong_racket.png', 1)

pong_ball.x = (game_window.width / 2) - (pong_ball.width / 2)
pong_ball.y = (game_window.height / 2) - (pong_ball.height / 2)

pong_l_racket.x = 12
pong_l_racket.y = (game_window.height / 2) - (pong_l_racket.height / 2)

pong_r_racket.x = game_window.width - (pong_r_racket.width + 12)
pong_r_racket.y = (game_window.height / 2) - (pong_r_racket.height / 2)

vel_x = random.uniform(200.0, 300.0)
vel_y = random.uniform(200.0, 300.0)

vel_ky = 300.0

l_player_score = 0
r_player_score = 0

game_time = 0

# Game Loop:
while True:
    game_time = int(game_window.time_elapsed() / 1000)
    
    if(game_keyboard.key_pressed("ESC")):
        game_window.close()
    
    pong_ball.x = pong_ball.x + (vel_x * game_window.delta_time())
    pong_ball.y = pong_ball.y + (vel_y * game_window.delta_time())

    if(pong_ball.x >= game_window.width):
        l_player_score += 1
        vel_x *= -1
        pong_ball.x = (game_window.width / 2) - (pong_ball.width / 2)
        pong_ball.y = (game_window.height / 2) - (pong_ball.height / 2)
    if(pong_ball.x <= -1 * pong_ball.width):
        r_player_score += 1
        vel_x *= -1
        pong_ball.x = (game_window.width / 2) - (pong_ball.width / 2)
        pong_ball.y = (game_window.height / 2) - (pong_ball.height / 2)

    if(pong_ball.y >= (game_window.height - pong_ball.height) or pong_ball.y <= 0):
        vel_y *= -1
        if(pong_ball.y <= 0):
            pong_ball.y = 0
        if(pong_ball.y >= (game_window.height - pong_ball.height)):
            pong_ball.y = game_window.height - pong_ball.height

    if(pong_l_racket.collided(pong_ball)):
        vel_x *= -1
        pong_ball.x = pong_l_racket.x + pong_l_racket.width
    if(pong_r_racket.collided(pong_ball)):
        vel_x *= -1
        pong_ball.x = pong_r_racket.x - pong_ball.width

    if(game_keyboard.key_pressed("W") and pong_l_racket.y >= 0):
        pong_l_racket.y = pong_l_racket.y - (vel_ky * game_window.delta_time())
    elif(game_keyboard.key_pressed("S") and pong_l_racket.y <= (game_window.height - pong_l_racket.height)):
        pong_l_racket.y = pong_l_racket.y + (vel_ky * game_window.delta_time())

    if(game_keyboard.key_pressed("UP") and pong_r_racket.y >= 0):
        pong_r_racket.y = pong_r_racket.y - (vel_ky * game_window.delta_time())
    elif(game_keyboard.key_pressed("DOWN") and pong_r_racket.y <= (game_window.height - pong_r_racket.height)):
        pong_r_racket.y = pong_r_racket.y + (vel_ky * game_window.delta_time())

    game_background.draw()

    pong_ball.draw()
    pong_l_racket.draw()
    pong_r_racket.draw()

    game_window.draw_text(str(game_time), (game_window.width / 2) - 33, 12, size=40, color=(0, 255, 0), font_name="monospace", bold=True, italic=False)
    game_window.draw_text(str(l_player_score), (game_window.width * 0.25) - 24, 12, size=40, color=(255, 0, 0), font_name="monospace", bold=True, italic=False)
    game_window.draw_text(str(r_player_score), (game_window.width * 0.75) - 24, 12, size=40, color=(0, 0, 255), font_name="monospace", bold=True, italic=False)

    game_window.update()
