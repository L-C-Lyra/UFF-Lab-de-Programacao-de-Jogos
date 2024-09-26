from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
import datetime
import main_menu
import play_menu
import difficulty_menu

def player_rank_input(player_score):
    game_window = Window(1000, 600)

    game_window.set_title("Game Over!")

    player_name = ""
    while(not player_name):
        player_name = input("Enter your name: ")
    
    player_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("./src/ranking.txt", "a") as file:
        file.write(f"{player_name};{player_score};{player_date}\n")
    
    main_menu.main()

    game_window.update()


def write_ranking():
    game_ranking = []
    try:
        with open("./src/ranking.txt", "r") as file:
            for line in file:
                player_name, player_score, player_date = line.strip().split(";")
                game_ranking.append((player_name, int(player_score), player_date))
    except FileNotFoundError:
        pass

    return game_ranking


def main():
    game_window = Window(1000, 600)

    game_background = GameImage("./src/assets/game_background.png")

    game_keyboard = game_window.get_keyboard()

    game_window.set_title("Ranking Menu - Space Invaders of Leonardo Brasil -> Lucas Correa")

    game_ranking = write_ranking()
    sorted_game_ranking = sorted(game_ranking, key=lambda x: x[1], reverse=True)

    while True:
        game_background.draw()
        
        if(game_keyboard.key_pressed("ESC")):
            main_menu.main()

        game_window.draw_text("Ranking:", 12, 12, size=40, color=(255, 255, 255), font_name="monospace", bold=True, italic=False)
        for i, (player_name, player_score, player_date) in enumerate(sorted_game_ranking[:5], 1):
            game_window.draw_text(f"{i}. {player_name} - {player_score} - {player_date}", 12, 12 + (i * 40), size=40, color=(255, 255, 255), font_name="monospace", bold=False, italic=False)

        game_window.update()
