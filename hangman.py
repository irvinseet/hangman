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
  l = f.readlines()
  f.close()

#remove /n after every element
l1 = [element.strip().upper() for element in l]

#select a random word from the dictionary
word = (random.choice(l1))

#print display for user
print('Welcome to Hangman!')
print(str(len(word)) + ' letters')

#generate a list to letters
guesslist = [] 
for i in range(len(word)):
  guesslist.append('_')

#guessprint converts guesslist into a string for better display
guessprint = (' '.join(guesslist))
print(guessprint)

#initialise counter
errorcounter = 0

while True:
  print('You have ' + str(int(6 - errorcounter)) + ' lives')
  letter = input("Guess a letter: ").upper()

  if letter == 'EXIT': #user can type 'exit' to stop playing
    sys.exit()

  if len(letter) != 1 or letter.isalpha() == False:
    print("Error: Type an aphabetical letter.")
    
#iterate through word to see if letter matches
  for i in range(len(word)):
    if letter == word[i]:
      guesslist[i] = letter #update the list
      errorcounter -= 1 # to neutralise the line below
      
  errorcounter += 1

  guessprint = (' '.join(guesslist)) # print the updated list
  print(guessprint)

#user fail to guess word with 6 lives
  if errorcounter == 6:
    print("Game over! The word is " + word)
    sys.exit()

#user guessed all the letters
  if guesslist.count('_') == 0:
    break
  
print("Congratulations, you won!")
sys.exit()
