from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import main_menu
import player_settings
import alien_settings

def main(difficulty_value = 0):
    game_window = Window(1000, 600)

    game_background = GameImage("./src/assets/game_background.png")

    game_keyboard = game_window.get_keyboard()

    game_window.set_title("Space Invaders of Leonardo Brasil -> Lucas Correa")

    player_spaceship = Sprite("./src/assets/player_spaceship.png")
    player_spaceship.set_position((game_window.width / 2) - (player_spaceship.width / 2), ((game_window.height / 2) - (player_spaceship.height / 2)) * 1.90)
    player_points = 0
    player_lifes = 3
    player_status = True

    shot_array = []
    recharge = 1

    alien_matrix = []

    vel_x = 250.0

    vel_ax = 50.0
    vel_ay = 25.0

    clock = 0
    fps_final = 0
    fps_counter = 0

    while True:
        if(game_keyboard.key_pressed("ESC")):
            main_menu.main()
        
        if(player_spaceship.x > 0):
            if(game_keyboard.key_pressed("A")):
                player_spaceship.x -= vel_x * game_window.delta_time()
        if(player_spaceship.x < (game_window.width - player_spaceship.width)):
            if(game_keyboard.key_pressed("D")):
                player_spaceship.x += vel_x * game_window.delta_time()

        recharge += game_window.delta_time()
        if((game_keyboard.key_pressed("SPACE")) and (recharge >= 1)):
            shot_array = player_settings.player_shooting(player_spaceship, shot_array)
            recharge = 0
        
        if((len(alien_matrix) == 0) and player_status):
            alien_lin = 5
            alien_col = 11
            alien_matrix = alien_settings.new_matrix(alien_matrix, alien_lin, alien_col)

        game_background.draw()

        player_spaceship.draw()

        if(len(shot_array) != 0):
            for shot in shot_array:
                shot.draw()
                shot.y -= 200 * game_window.delta_time()
                shot = player_settings.limits_shot(shot, shot_array)

        if((len(alien_matrix) != 0) and player_status):
            alien_matrix, vel_ax, player_status = alien_settings.matrix_movement(alien_matrix, vel_ax, vel_ay, player_spaceship, game_window)
            
            if(len(shot_array) != 0):
                player_points = player_settings.shot_hit(shot_array, alien_matrix, player_points)
            
            for lin in alien_matrix:
                for alien in lin:
                    alien.draw()
            
            if((alien.y >= (((game_window.height / 2) - (player_spaceship.height)) * 1.90)) and player_status):
                game_window.close()
                # player_lifes -= 1
                # player_spaceship.set_position((game_window.width / 2) - (player_spaceship.width / 2), ((game_window.height / 2) - (player_spaceship.height / 2)) * 1.90)
                # alien_matrix = []

        clock += game_window.delta_time()
        if(clock >= 1):
            fps_final = fps_counter
            fps_counter = 0
            clock = 0

        game_window.draw_text(f"FPS: {fps_final}", 12, 12, size=40, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        game_window.draw_text(f"Score: {player_points}", 12, 52, size=40, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        game_window.draw_text(f"Lifes: {player_lifes}", 12, 92, size=40, color=(255, 0, 0), font_name="monospace", bold=True, italic=False)
        fps_counter += 1

        # if(player_lifes < 1):
        #     player_status = False
        #     if(not player_status):
        #         game_window.close()
        

        game_window.update()
