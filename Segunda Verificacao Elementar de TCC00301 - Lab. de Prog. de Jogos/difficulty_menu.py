from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.mouse import *
import main_menu
import play_menu
import ranking_menu

def main():
    game_window = Window(1000, 600)

    game_background = GameImage("./src/assets/game_background.png")

    game_keyboard = game_window.get_keyboard()
    game_mouse = game_window.get_mouse()

    game_window.set_title("Difficulty Menu - Space Invaders of Leonardo Brasil -> Lucas Correa")

    easy_button = Sprite("./src/assets/easy_button.png")
    easy_button.set_position((game_window.width - easy_button.width) / 2, easy_button.height * 2)

    medium_button = Sprite("./src/assets/medium_button.png")
    medium_button.set_position((game_window.width - medium_button.width) / 2, medium_button.height * 5)

    hard_button = Sprite("./src/assets/hard_button.png")
    hard_button.set_position((game_window.width - hard_button.width) / 2, hard_button.height * 8)

    while True:
        if(game_keyboard.key_pressed("ESC")):
            main_menu.main()
        
        if(game_mouse.is_button_pressed(1)):
            if(game_mouse.is_over_object(easy_button)):
                play_menu.main(1)
            elif(game_mouse.is_over_object(medium_button)):
                play_menu.main(2)
            elif(game_mouse.is_over_object(hard_button)):
                play_menu.main(3)

        game_background.draw()

        easy_button.draw()
        medium_button.draw()
        hard_button.draw()

        game_window.update()
