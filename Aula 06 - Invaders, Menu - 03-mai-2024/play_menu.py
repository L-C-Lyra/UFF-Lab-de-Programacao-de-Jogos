from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
import main_menu

def play():
    game_window = Window(600, 600)
    
    game_window.set_background_color([0, 0, 0])

    game_keyboard = game_window.get_keyboard()
    game_mouse = game_window.get_mouse()

    game_window.set_title('Space Invaders of Lucas Correa')

    while True:
        if(game_keyboard.key_pressed("ESC")):
            return 0

        game_window.update()