from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *
import play_menu
import ranking_menu
import difficulty_menu

def main():
    game_window = Window(1000, 600)

    game_background = GameImage("./src/assets/game_background.png")

    game_mouse = game_window.get_mouse()

    game_window.set_title("Space Invaders of Leonardo Brasil -> Lucas Correa")

    game_title = Sprite("./src/assets/game_title.png")
    game_title.set_position(100, (game_window.height - game_title.height) / 2)

    play_button = Sprite("./src/assets/play_button.png")
    play_button.set_position((game_window.width - play_button.width) - 100, play_button.height * 2)

    ranking_button = Sprite("./src/assets/ranking_button.png")
    ranking_button.set_position((game_window.width - ranking_button.width) - 100, ranking_button.height * 4)

    difficulty_button = Sprite("./src/assets/difficulty_button.png")
    difficulty_button.set_position((game_window.width - difficulty_button.width) - 100, difficulty_button.height * 6)

    exit_button = Sprite("./src/assets/exit_button.png")
    exit_button.set_position((game_window.width - exit_button.width) - 100, exit_button.height * 8)

    while True:
        if(game_mouse.is_button_pressed(1)):
            if(game_mouse.is_over_object(play_button)):
                play_menu.main()
            elif(game_mouse.is_over_object(ranking_button)):
                ranking_menu.main()
            elif(game_mouse.is_over_object(difficulty_button)):
                difficulty_menu.main()
            elif(game_mouse.is_over_object(exit_button)):
                game_window.close()

        game_background.draw()

        game_title.draw()
        play_button.draw()
        ranking_button.draw()
        difficulty_button.draw()
        exit_button.draw()

        game_window.update()

if __name__ == "__main__":
    main()
