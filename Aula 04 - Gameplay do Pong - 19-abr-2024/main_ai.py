from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import random

cycle_counter = 0
def pong_racket_ai():
    if vel_x < 0 and move_ball == True:
        if(pong_l_racket.y < pong_ball.y and ((pong_l_racket.y + pong_l_racket.height) // 2) < pong_ball.y and (pong_l_racket.y + pong_l_racket.height) < game_window.height):
            pong_l_racket.set_position(pong_l_racket.x, pong_l_racket.y + (vel_ky * game_window.delta_time()))
        elif(pong_l_racket.y > 0):
            pong_l_racket.set_position(pong_l_racket.x, pong_l_racket.y - (vel_ky * game_window.delta_time()))

game_window = Window(600, 600)

game_background = GameImage('./src/assets/game_background.png')

game_keyboard = game_window.get_keyboard()

game_window.set_title('Pong of Lucas Correa')

pong_ball = Sprite('./src/assets/pong_ball.png', 1)
pong_l_racket = Sprite('./src/assets/pong_racket.png', 1)
pong_r_racket = Sprite('./src/assets/pong_racket.png', 1)

pong_ball.set_position((game_window.width / 2) - (pong_ball.width / 2), (game_window.height / 2) - (pong_ball.height / 2))

pong_l_racket.set_position(12, (game_window.height / 2) - (pong_l_racket.height / 2))

pong_r_racket.set_position(game_window.width - (pong_r_racket.width + 12), (game_window.height / 2) - (pong_r_racket.height / 2))

vel_x = -1 * random.uniform(200.0, 300.0)
vel_y = -1 * random.uniform(200.0, 300.0)

vel_ky = 300.0

l_player_score = 0
r_player_score = 0

last_delta_time = 0.0
game_time = 0
move_ball = 0

# Game Loop:
while True:
    collided = False
    game_time = int(game_window.time_elapsed() / 1000)
    
    if(game_keyboard.key_pressed("ESC")):
        game_window.close()
    if(game_keyboard.key_pressed("SPACE") and move_ball == 0):
        move_ball = 1
    if(cycle_counter <= 25):
        pong_racket_ai()
    
    if(game_keyboard.key_pressed("UP") and pong_r_racket.y >= 0):
        pong_r_racket.y = pong_r_racket.y - (vel_ky * game_window.delta_time())
    elif(game_keyboard.key_pressed("DOWN") and pong_r_racket.y <= (game_window.height - pong_r_racket.height)):
        pong_r_racket.y = pong_r_racket.y + (vel_ky * game_window.delta_time())
    
    if(pong_ball.y >= (game_window.height - pong_ball.height) or pong_ball.y <= 0):
        vel_y *= -1
        collided = True
    if(pong_ball.collided(pong_l_racket) or pong_ball.collided(pong_r_racket)):
        vel_x *= -1
        collided = True
    
    if(pong_ball.x >= (game_window.width - pong_ball.height)):
        l_player_score += 1
        pong_ball.set_position((game_window.width / 2) - (pong_ball.width / 2), (game_window.height / 2) - (pong_ball.height / 2))
        move_ball = 0
    if(pong_ball.x <= 0):
        r_player_score += 1
        pong_ball.set_position((game_window.width / 2) - (pong_ball.width / 2), (game_window.height / 2) - (pong_ball.height / 2))
        move_ball = 0

    if(collided == False):
        last_delta_time = game_window.delta_time()
        pong_ball.set_position((pong_ball.x + (vel_x * game_window.delta_time() * move_ball)), (pong_ball.y + (vel_y * game_window.delta_time() * move_ball)))
    else:
        pong_ball.set_position((pong_ball.x + (vel_x * last_delta_time * move_ball)), (pong_ball.y + (vel_y * last_delta_time * move_ball)))

    game_background.draw()

    pong_ball.draw()
    pong_l_racket.draw()
    pong_r_racket.draw()

    cycle_counter += 1
    if(cycle_counter == 33):
        cycle_counter = 0

    if(move_ball == 0):
        game_window.draw_text("Press \"SPACE\" to START.", 12, game_window.height - 52, size=40, color=(0, 255, 0), font_name="monospace", bold=True, italic=True)
        game_window.draw_text("Press \"ESC\" to EXIT.", 12, game_window.height - 94, size=40, color=(0, 127, 0), font_name="monospace", bold=True, italic=True)
    game_window.draw_text(str(game_time), (game_window.width / 2) - 33, 12, size=40, color=(0, 255, 0), font_name="monospace", bold=True, italic=False)
    game_window.draw_text(str(l_player_score), (game_window.width * 0.25) - 24, 12, size=40, color=(255, 0, 0), font_name="monospace", bold=True, italic=False)
    game_window.draw_text(str(r_player_score), (game_window.width * 0.75) - 24, 12, size=40, color=(0, 0, 255), font_name="monospace", bold=True, italic=False)

    game_window.update()
