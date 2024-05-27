from milestone_2 import random_fruit



selected_fruit = random_fruit()

def check_guess(guess):
  guess = input("Guess an alphabet: ")
  lower_case = guess.lower()
  if lower_case in selected_fruit:
      print(lower_case, "is in", selected_fruit)
  else:
    print(lower_case, "is not in", selected_fruit)


def ask_for_input():
    while True:
     new_input = input("Guess an alphabet: ")
     if len(new_input) == 1 and new_input.isalpha:
       print(f"{new_input} is a good guess")
     else:
      print("Invalid letter. Please, enter a single alphabetical character.")
     

check_guess("A")
ask_for_input()
 
     
   
