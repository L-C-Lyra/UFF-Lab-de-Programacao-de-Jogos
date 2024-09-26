from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import random
import main_menu
import ranking_menu
import difficulty_menu
import player_settings
import alien_settings

def main(difficulty_value = 1):
    game_window = Window(1000, 600)

    game_background = GameImage("./src/assets/game_background.png")

    game_keyboard = game_window.get_keyboard()

    game_window.set_title("Play - Space Invaders of Leonardo Brasil -> Lucas Correa")

    player_spaceship = Sprite("./src/assets/player_spaceship.png")
    player_spaceship.set_position((game_window.width / 2) - (player_spaceship.width / 2), ((game_window.height / 2) - (player_spaceship.height / 2)) * 1.90)

    player_score = 0
    player_life = 3
    player_status = True

    inv = False
    inv_timer = 0
    blinking = False

    shot_array = []
    recharge = 1
    shot_sequence = 1

    alien_matrix = []
    alien_shot_array = []
    alien_recharge = 0
    alien_level = -1

    vel_x = 250.0
    vel_y = 25.0
    vel_s = 200.0

    vel_ax = 50.0
    vel_ay = 25.0
    vel_as = 50.0

    clock = 0
    fps_final = 0
    fps_counter = 0

    barrier_a = Sprite("./src/assets/barrier.png")
    barrier_a.set_position((game_window.width / 4) - (barrier_a.width / 2), ((game_window.height / 2) - (player_spaceship.height + (barrier_a.height / 2))) * 1.90)
    barrier_b = Sprite("./src/assets/barrier.png")
    barrier_b.set_position((game_window.width / 2) - (barrier_b.width / 2), ((game_window.height / 2) - (player_spaceship.height + (barrier_b.height / 2))) * 1.90)
    barrier_c = Sprite("./src/assets/barrier.png")
    barrier_c.set_position(((game_window.width / 4) * 3) - (barrier_c.width / 2), ((game_window.height / 2) - (player_spaceship.height + (barrier_c.height / 2))) * 1.90)

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
        if(difficulty_value == 1):
            if((game_keyboard.key_pressed("SPACE")) and (recharge >= 1)):
                shot_array = player_settings.player_shooting(player_spaceship, shot_array)
                if(game_keyboard.key_pressed("SPACE") and (recharge <= 1.1)):
                    shot_sequence += 1
                    if(game_keyboard.key_pressed("SPACE") and (shot_sequence >= 5)):
                        aux_x = player_spaceship.x
                        aux_y = player_spaceship.y
                        player_spaceship = Sprite("./src/assets/hot_player_spaceship.png")
                        player_spaceship.set_position(aux_x, aux_y)
                        player_spaceship.draw()
                        if(game_keyboard.key_pressed("SPACE") and (shot_sequence == 10)):
                            player_life -= 1
                            player_spaceship = Sprite("./src/assets/player_spaceship.png")
                            player_spaceship.set_position((game_window.width / 2) - (player_spaceship.width / 2), ((game_window.height / 2) - (player_spaceship.height / 2)) * 1.90)
                            player_spaceship.draw()
                else:
                    shot_sequence = 1
                    aux_x = player_spaceship.x
                    aux_y = player_spaceship.y
                    player_spaceship = Sprite("./src/assets/player_spaceship.png")
                    player_spaceship.set_position(aux_x, aux_y)
                    player_spaceship.draw()
                recharge = 0
        elif(difficulty_value == 2):
            if((game_keyboard.key_pressed("SPACE")) and (recharge >= 2)):
                shot_array = player_settings.player_shooting(player_spaceship, shot_array)
                recharge = 0
        elif(difficulty_value == 3):
            if((game_keyboard.key_pressed("SPACE")) and (recharge >= 3)):
                shot_array = player_settings.player_shooting(player_spaceship, shot_array)
                recharge = 0

        if((len(alien_matrix) == 0) and player_status):
            alien_level += 1
            alien_lin = 3
            alien_col = 5
            alien_matrix = alien_settings.new_matrix(alien_matrix, alien_lin, alien_col)

            barrier_a_counter = 0
            barrier_b_counter = 0
            barrier_c_counter = 0

            barrier_a_hide = False
            barrier_b_hide = False
            barrier_c_hide = False

        game_background.draw()

        player_spaceship.draw()

        if(len(shot_array) != 0):
            for shot in shot_array:
                shot.draw()
                shot.y -= vel_s * game_window.delta_time()
                shot = player_settings.limits_shot(shot, shot_array)

        if((len(alien_matrix) != 0) and player_status):
            alien_matrix, vel_ax, player_status = alien_settings.matrix_movement(alien_matrix, vel_ax, vel_ay, player_spaceship, game_window)
            
            if(len(shot_array) != 0):
                player_score = player_settings.shot_hit(shot_array, alien_matrix, player_score, difficulty_value, barrier_a, barrier_b, barrier_c, barrier_a_hide, barrier_b_hide, barrier_c_hide)
            
            for lin in alien_matrix:
                for alien in lin:
                    alien.draw()
            
                alien_recharge += game_window.delta_time()

                if((alien_recharge >= (4 - difficulty_value) - (alien_level / 10)) and player_status):
                    x = random.randint(0, len(alien_matrix) - 1)
                    y = random.randint(0, len(alien_matrix[x]) - 1)
                    alien_shot_array = alien_settings.alien_shooting(alien_matrix[x][y], alien_shot_array)
                    alien_recharge = 0
                
                if((len(alien_shot_array) != 0) and player_status):
                    for shot in alien_shot_array:
                        shot.draw()
                        shot.y += (vel_as + alien_level) * game_window.delta_time()
                        shot = alien_settings.alien_limits_shot(shot, alien_shot_array, game_window)
                
                if(not inv):
                    player_life, inv = alien_settings.alien_shot_hit(alien_shot_array, player_spaceship, player_life, game_window)
                    if(not barrier_a_hide):
                        barrier_a.draw()
                    if(not barrier_b_hide):
                        barrier_b.draw()
                    if(not barrier_c_hide):
                        barrier_c.draw()
                    barrier_a, barrier_b, barrier_c, barrier_a_counter, barrier_b_counter, barrier_c_counter, barrier_a_hide, barrier_b_hide, barrier_c_hide = alien_settings.alien_shot_barrier_hit(alien_shot_array, barrier_a, barrier_b, barrier_c, barrier_a_counter, barrier_b_counter, barrier_c_counter, barrier_a_hide, barrier_b_hide, barrier_c_hide)
                else:
                    inv_timer += game_window.delta_time()
                    while(inv_timer < 2):
                        if(not blinking):
                            player_spaceship.curr_frame = 1
                            blinking = True
                        elif(blinking):
                            player_spaceship.curr_frame = 0
                            blinking = False
                        break
                    if(inv_timer >= 2):
                        inv_timer = 0
                        player_spaceship.curr_frame = 0
                        inv = False
            
            if(((not barrier_a_hide) or (not barrier_b_hide) or (not barrier_c_hide)) and player_status):
                if(alien.y >= (((game_window.height / 2) - (barrier_a.height)) * 1.90)):
                    player_status = False
                    if(not player_status):
                        ranking_menu.player_rank_input(player_score)
            elif((alien.y >= (((game_window.height / 2) - (player_spaceship.height)) * 1.90)) and player_status):
                player_status = False
                if(not player_status):
                    ranking_menu.player_rank_input(player_score)

        clock += game_window.delta_time()
        if(clock >= 1):
            fps_final = fps_counter
            fps_counter = 0
            clock = 0

        game_window.draw_text(f"FPS: {fps_final}", 12, 12, size=40, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        game_window.draw_text(f"Score: {player_score}", 12, 52, size=40, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        game_window.draw_text(f"Lifes: {player_life}", 12, 92, size=40, color=(255, 0, 0), font_name="monospace", bold=True, italic=False)
        fps_counter += 1

        if(player_life < 1):
            player_status = False
            if(not player_status):
                ranking_menu.player_rank_input(player_score)
        

        game_window.update()
