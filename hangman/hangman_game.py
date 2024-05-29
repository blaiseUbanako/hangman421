import random


class Hangman:
    '''
    A class that initiates the hangman 
    '''
    def __init__(self, word_list, num_lives = 5):

        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]  
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        lower_case = guess.lower()
        if lower_case in self.word:           
            print(lower_case, "is in", self.word)
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            print(self.word_guessed)
            self.num_letters -= 1
            print(self.num_letters)
        else:
            print(lower_case, "is not in", self.word)
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
             new_input = input("guess an alphabet:")
             
             if len(new_input) !=1 or new_input.isnumeric():
                print("Invalid letter. Please, enter a single alphabetical character.")
             elif  new_input in self.list_of_guesses:
                print("You already tried that letter!")
             else: 
                self.list_of_guesses.append(new_input)
                print(f"{new_input} is a good guess")
                self.check_guess(new_input)   
                break   


def play_game(word_list):
    num_lives = 4
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters < 0:
            print('Congratulations. You won the game!')
            break

if __name__ == '__main__':     
    word_list = ["apple", "banana", "mango", "orange", "strawberry" ]
    play_game(word_list)

