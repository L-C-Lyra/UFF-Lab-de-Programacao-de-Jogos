from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import main_menu

def main(difficulty_value = 0):
    game_window = Window(1000, 600)

    game_background = GameImage("./src/assets/game_background.png")

    game_keyboard = game_window.get_keyboard()

    game_window.set_title("Space Invaders of Leonardo Brasil -> Lucas Correa")

    player_spaceship = Sprite("./src/assets/player_spaceship.png")
    player_spaceship.set_position((game_window.width / 2) - (player_spaceship.width / 2), ((game_window.height / 2) - (player_spaceship.height / 2)) * 1.90)

    shot_list = []
    recharge = 0

    vel_x = 350

    while True:
        if(game_keyboard.key_pressed("ESC")):
            main_menu.main()
        
        if(player_spaceship.x > 0):
            if(game_keyboard.key_pressed("A")):
                player_spaceship.x -= vel_x * game_window.delta_time()
        if(player_spaceship.x < (game_window.width - player_spaceship.width)):
            if(game_keyboard.key_pressed("D")):
                player_spaceship.x += vel_x * game_window.delta_time()

        game_background.draw()

        player_spaceship.draw()

        recharge += game_window.delta_time()
        if((game_keyboard.key_pressed("SPACE")) and (recharge >= 1)):
            shot_list = player_shooting(player_spaceship, shot_list)
            recharge = 0
        if(len(shot_list) != 0):
            for s in shot_list:
                s.draw()
                s.y -= 200 * game_window.delta_time()
                s = limits_shot(s, shot_list)
    
        game_window.update()


def player_shooting(player_spaceship, shot_list):
    shot = Sprite("./src/assets/player_shot.png", 5)
    shot.set_sequence_time(0, 4, 300, True)

    shot.x = player_spaceship.x + (shot.width * 0.25)
    shot.y = player_spaceship.y - shot.height

    shot_list.append(shot)

    return shot_list


def limits_shot(shot, shot_list):
    if(shot.y <= (shot.height * 3)):
        shot.update()
    if(shot.y <= 0):
        shot_list.remove(shot)
