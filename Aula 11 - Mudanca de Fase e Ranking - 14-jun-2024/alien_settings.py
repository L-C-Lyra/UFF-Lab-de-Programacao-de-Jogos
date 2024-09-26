from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import random
import player_settings

def new_matrix(matrix, lin, col):
    for i in range(lin):
        alien_col = []
        for j in range(col):
            choice = random.randint(1, 2)
            
            if(choice == 1):
                switch = 1
            else:
                switch = 2
            
            alien = Sprite(f"./src/assets/alien_{choice}.png", switch)
            alien.set_position((alien.width + (alien.width / 2)) * j + 10, (alien.height + (alien.height / 2)) * i)
            
            alien_col.append(alien)
        matrix.append(alien_col)
    
    return matrix


def matrix_collision(matrix, vel_ax, player_spaceship, game_window):  
    side = False
    base = True

    for lin in matrix:
        for alien in lin:
            alien.x += vel_ax * game_window.delta_time()

            if(alien.x <= 0):
                side = True
            if(alien.x >= (game_window.width - alien.width)):
                side = True
            if(alien.y + alien.height >= player_spaceship.y):
                base = False
    
    return side, base


def matrix_movement(matrix, vel_ax, vel_ay, player_spaceship, game_window):
    side, base = matrix_collision(matrix, vel_ax, player_spaceship, game_window)

    if(side):
        vel_ax = -vel_ax
        for lin in matrix:
            for alien in lin:
                alien.x += vel_ax * game_window.delta_time()
                alien.y += vel_ay
    
    return matrix, vel_ax, base


def matrix_limits(alien_matrix):
    array_x = []
    array_y = []

    for lin in alien_matrix:
        for alien in lin:
            array_x.append(alien.x)
            array_y.append(alien.y)
    
    return min(array_x), (max(array_x) + alien_matrix[0][0].x), min(array_y), (max(array_y) + alien_matrix[0][0].y)


def alien_shooting(alien, shot_array):
    shot = Sprite("./src/assets/alien_shot.png", 5)
    shot.set_sequence_time(0, 4, 300, True)

    shot.x = alien.x + 2
    shot.y = alien.y + alien.height + shot.height

    shot_array.append(shot)

    return shot_array


def alien_limits_shot(shot, shot_array, game_window):
    if(shot.y >= game_window.height):
        shot_array.remove(shot)
    if(shot.y >= (game_window.height - shot.height * 6)):
        shot.update()


def alien_shot_hit(shot_array, player_spaceship, player_life, game_window):
    inv = False

    for shot in shot_array:
        if(shot.collided(player_spaceship) and (shot in shot_array)):
            shot_array.remove(shot)
            inv = True
            player_life -= 1
            player_spaceship.x = (game_window.width / 2) - (player_spaceship.width / 2)
            break
    
    return player_life, inv
