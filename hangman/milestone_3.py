from milestone_2 import word_list
from milestone_2 import random_fruit



selected_fruit = random_fruit()

def check_guess(guess):
  guess = input("Guess an alphabet: ")
  lower_case = guess.lower()
  if lower_case in selected_fruit:
      print(lower_case, "is in", selected_fruit)


def ask_for_input():
    while True:
     my_input = input("Guess an alphabet: ")
     if len(my_input) == 1 and my_input.isalpha:
       print(f"{my_input} is a good guess")
     else:
      print("Invalid letter. Please, enter a single alphabetical character.")
     

check_guess("A")
ask_for_input()
 
     
   
