#https://www.practicepython.org/
#you can use any dictionary of words you like
#advanced: use sowpods.txt by Peter Norvig - http://norvig.com/ngrams/sowpods.txt
#more friendly: use words.txt - https://github.com/Xethron/Hangman/blob/master/words.txt

import random
import sys

#generate list to store results
l1 = []

#read file
with open('words.txt', 'r') as f:
  l = f.readlines()
  f.close()

#remove /n after every element
l1 = [element.strip().upper() for element in l]
word = (random.choice(l1))

#print display for user
print('Welcome to Hangman!')
print(str(len(word)) + ' letters')

guesslist = []
for i in range(len(word)):
  guesslist.append('_')

guessprint = (' '.join(guesslist))
print(guessprint)

errorcounter = 0

while True:
  print('You have ' + str(int(6 - errorcounter)) + ' lives')
  letter = input("Guess a letter: ").upper()
  if letter == 'EXIT':
    sys.exit()
  if len(letter) != 1 or letter.isalpha() == False:
    print("Error: Type an aphabetical letter.")
  for i in range(len(word)):
    if letter == word[i]:
      guesslist[i] = letter
      errorcounter -= 1

  errorcounter += 1

  guessprint = (' '.join(guesslist))
  print(guessprint)

  if guesslist.count('_') == 0:
    break
  
  if errorcounter == 6:
    print("Game over! The word is " + word)
    sys.exit()

print("Congratulations, you won!")
sys.exit()



