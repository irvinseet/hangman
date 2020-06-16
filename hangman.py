#an assignment on https://www.practicepython.org/
#you can use any dictionary of words you like
#advanced: use sowpods.txt by Peter Norvig - http://norvig.com/ngrams/sowpods.txt
#more friendly: use words.txt - https://github.com/Xethron/Hangman/blob/master/words.txt

import random
import sys

#generate list to store words
l1 = []

#read file
with open('words.txt', 'r') as f:
  fhand = f.readlines()
  f.close()

#remove /n after every element
l1 = [element.strip().upper() for element in fhand]

#select a random word from the dictionary
word = (random.choice(l1))

#print display for user
print('Welcome to Hangman!')
print('{} letters'.format(len(word)))

#use a list for easier manipulation
guesslist = list()
for i in range(len(word)):
  guesslist.append('_')

#converts guesslist into a string for better display
#printing the above guesslist will return ['_', '_' ... etc]
#and we dont want that
guessprint = (' '.join(guesslist))
print(guessprint)

#initialise counter
lives = 6

while True:
  print('You have {} lives left'.format(lives))
  letter = input("Guess a letter: ").upper()

  if letter == 'EXIT': #user can type 'exit' to stop playing
    sys.exit()

  if len(letter) != 1 or letter.isalpha() == False:
    print("Error: Please guess an aphabetical letter.")
    
#iterate through word to see if letter matches
  for i in range(len(word)):
    if letter == word[i]:
      guesslist[i] = letter #update the list
      guessprint = (' '.join(guesslist)) # print the updated list
      print(guessprint)
      lives = lives + 1 #to neutralise the subtraction outside the loop aft every round

  lives = lives - 1 #outside the for loop so it doesnt iterate len(word) times

#user fail to guess word with 6 lives
  if lives == 0:
    print("Game over! The word is " + word)
    sys.exit()

#user guessed the word with <6 mistakes
  if guesslist.count('_') == 0:
    break
  
print("Congratulations, you won!")
sys.exit()
