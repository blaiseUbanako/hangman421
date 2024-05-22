import random as rd


word_list = ["apple", "banana", "mango", "orange", "strawberry" ]

for fruits in word_list:
    print(fruits)

word = rd.choice(word_list)
print(word)


guess = input('Please enter a single letter: ')
if len(guess) ==1 and guess.isalpha():
 print("Good guess")
else:
 print("Oops! That is not a valid input.")
