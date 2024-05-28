from milestone_4 import Hangman
import random

def play_game(word_list):
    num_lives = 4
    word = random.choice(word_list)
    num_letters = len(set(word))
    game = Hangman(word_list, num_lives)

    while True:
        if num_lives == 0:
            print("You lost!")
        elif num_letters > 0:
            Hangman.ask_for_input()
        elif num_lives != 0 and num_letters < 0:
            print('Congratulations. You won the game!')


play_game()