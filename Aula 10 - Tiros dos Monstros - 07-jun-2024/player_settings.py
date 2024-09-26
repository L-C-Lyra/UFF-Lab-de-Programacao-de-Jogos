from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import alien_settings

def player_shooting(player_spaceship, shot_array):
    shot = Sprite("./src/assets/player_shot.png", 5)
    shot.set_sequence_time(0, 4, 300, True)

    shot.x = player_spaceship.x + (shot.width * 0.25)
    shot.y = player_spaceship.y - shot.height

    shot_array.append(shot)

    return shot_array


def limits_shot(shot, shot_array):
    if(shot.y <= (shot.height * 5)):
        shot.update()
    if(shot.y <= 0):
        shot_array.remove(shot)


def shot_hit(shot_array, alien_matrix, player_points):
    min_x, max_x, min_y, max_y = alien_settings.matrix_limits(alien_matrix)

    for shot in shot_array:
        if((shot.x >= min_x) and (shot.x <= max_x) and (shot.y >= min_y) and (shot.y <= max_y)):
            for i in range(len(alien_matrix) - 1, -1, -1):
                if(len(alien_matrix[i]) != 0):
                    min_x, max_x, min_y, max_y = alien_settings.matrix_limits(alien_matrix)

                    for alien in alien_matrix[i]:
                        if(shot.collided(alien) and shot in shot_array):
                            shot_array.remove(shot)
                            
                            if(alien.total_frames == 1):
                                alien_matrix[i].remove(alien)
                                player_points += 10
                            elif(alien.total_frames == 2):
                                alien_matrix[i].remove(alien)
                                player_points += 20
                
                if(len(alien_matrix[i]) == 0):
                    alien_matrix.pop(i)
    
    return player_points