from milestone_2 import random_fruit



random_word = random_fruit()

def check_guess(guess):
  guess = input("Guess an alphabet: ")
  lower_case = guess.lower()
  if lower_case in random_word:
      print(lower_case, "is in", random_word)
  else:
    print(lower_case, "is not in", random_word)


def ask_for_input():
    while True:
     new_input = input("Guess an alphabet: ")
     if len(new_input) == 1 and new_input.isalpha:
       print(f"{new_input} is a good guess")
     else:
      print("Invalid letter. Please, enter a single alphabetical character.")
     

check_guess("A")
ask_for_input()
 
     
   
