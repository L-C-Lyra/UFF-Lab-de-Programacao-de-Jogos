from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
import play_menu
import difficulty_menu

def main():
    game_window = Window(600, 600)

    game_background = GameImage('./src/assets/game_background.png')

    game_keyboard = game_window.get_keyboard()
    game_mouse = game_window.get_mouse()

    game_window.set_title('Space Invaders of Lucas Correa')

    play_button = Sprite('./src/assets/play_button.png', 1)
    play_button.x = game_window.width / 2 - play_button.width / 2
    play_button.y = 191

    difficulty_button = Sprite('./src/assets/difficulty_button.png', 1)
    difficulty_button.x = game_window.width / 2 - difficulty_button.width / 2
    difficulty_button.y = play_button.y + (play_button.height + 24)

    ranking_button = Sprite('./src/assets/ranking_button.png', 1)
    ranking_button.x = game_window.width / 2 - ranking_button.width / 2
    ranking_button.y = difficulty_button.y + (difficulty_button.height + 24)

    exit_button = Sprite('./src/assets/exit_button.png', 1)
    exit_button.x = game_window.width / 2 - exit_button.width / 2
    exit_button.y = ranking_button.y + (ranking_button.height + 24)

    while True:
        if(game_mouse.is_over_area([play_button.x, play_button.y], [play_button.x + play_button.width, play_button.y + play_button.height]) and game_mouse.is_button_pressed(1)):
            play_menu.play()
        if(game_mouse.is_over_area([difficulty_button.x, difficulty_button.y], [difficulty_button.x + difficulty_button.width, difficulty_button.y + difficulty_button.height]) and game_mouse.is_button_pressed(1)):
            difficulty_menu.difficulty()
        if(game_mouse.is_over_area([ranking_button.x, ranking_button.y], [ranking_button.x + ranking_button.width, ranking_button.y + ranking_button.height]) and game_mouse.is_button_pressed(1)):
            pass
        if(game_mouse.is_over_area([exit_button.x, exit_button.y], [exit_button.x + exit_button.width, exit_button.y + exit_button.height]) and game_mouse.is_button_pressed(1)):
            game_window.close()
        
        game_background.draw()

        play_button.draw()
        difficulty_button.draw()
        ranking_button.draw()
        exit_button.draw()

        game_window.update()


if __name__ == '__main__':
    main()