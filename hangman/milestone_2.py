import random as rd


word_list = ["apple", "banana", "mango", "orange", "strawberry" ]

def random_fruit():
   for fruits in word_list:
     print(fruits)
     word = rd.choice(word_list)
     print(word)


def guess_alphabet():
      guess = input('Please enter a single letter: ')
      if len(guess) ==1 and guess.isalpha():
       print("Good guess")
      else:
       print("Oops! That is not a valid input.")


random_fruit()
guess_alphabet()