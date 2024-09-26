from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
import main_menu
import play_menu

def difficulty():
    game_window = Window(600, 600)
    
    game_background = GameImage('./src/assets/game_background.png')

    game_keyboard = game_window.get_keyboard()
    game_mouse = game_window.get_mouse()

    game_window.set_title('Space Invaders of Lucas Correa')

    easy_button = Sprite('./src/assets/easy_button.png', 1)
    easy_button.x = game_window.width / 2 - easy_button.width / 2
    easy_button.y = 217

    medium_button = Sprite('./src/assets/medium_button.png', 1)
    medium_button.x = game_window.width / 2 - medium_button.width / 2
    medium_button.y = easy_button.y + (easy_button.height + 24)

    hard_button = Sprite('./src/assets/hard_button.png', 1)
    hard_button.x = game_window.width / 2 - hard_button.width / 2
    hard_button.y = medium_button.y + (medium_button.height + 24)

    while True:
        if(game_keyboard.key_pressed("ESC")):
            return 0
        
        if(game_mouse.is_over_area([easy_button.x, easy_button.y], [easy_button.x + easy_button.width, easy_button.y + easy_button.height]) and game_mouse.is_button_pressed(1)):
            pass
        if(game_mouse.is_over_area([medium_button.x, medium_button.y], [medium_button.x + medium_button.width, medium_button.y + medium_button.height]) and game_mouse.is_button_pressed(1)):
            pass
        if(game_mouse.is_over_area([hard_button.x, hard_button.y], [hard_button.x + hard_button.width, hard_button.y + hard_button.height]) and game_mouse.is_button_pressed(1)):
            pass
        
        game_background.draw()

        easy_button.draw()
        medium_button.draw()
        hard_button.draw()

        game_window.update()