from milestone_2 import word_list
import random


class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for letter in self.word]  #"_" for letter in self.word is a comprehension
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

               

    def check_guess(self, guess):
        lower_case = guess.lower()
        if lower_case in self.word:           
            print(lower_case, "is in", self.word)
            for letter in self.word:
                if letter == guess:
                    [guess for letter in self.word]
        else:
            print(lower_case, "is not in", self.word)
            self.num_lives - 1
            print("Sorry, {letter} is not in the word.")
            print("You have {num_lives} lives left.")



    def ask_for_input(self):
        while True:
             new_input = input("guess an alphabet:")
             
             if len(new_input) !=1 and new_input.isnumeric:
                 print("Invalid letter. Please, enter a single alphabetical character.")
             elif len(new_input) == 1 and new_input.isalpha: 
                print(f"{new_input} is a good guess") 
             elif  new_input in self.list_of_guesses:
                 print("You already tried that letter!")
             else: self.list_of_guesses.append
                 
    ask_for_input()

            
 