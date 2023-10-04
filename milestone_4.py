#%%
# Import random module & functions from milestone_3.py into script
import random
from milestone_3 import check_guess
from milestone_3 import ask_for_input
#%%
# Create Hangman class

class Hangman:
    '''
    This class

    Attributes:
        
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

#%%
# Initialising the following attributes
# word & word_list

word_list = ['Pineapple', 'Mango', 'Cherry', 'Apple', 'Strawberry']
word = random.choice(word_list)
print(word)
#%%
ask_for_input(word)
#%%
# word_guessed
# A list of the word with _ for each letter not yet guessed.

word_guessed = [ ]

for letter in word:
    word_guessed == word_guessed.append('_')
print(word_guessed)

# Now need to replace _ with the letter guessed if it is in the word
for letter in word:
    while True:
        guess = input('Please enter a single letter here: ')

        if guess == letter:
            letter_position = word.index(guess)
            print(letter_position)
            word_guessed[letter_position] = guess
        else: 
            print(f'{guess} is not in the word. Try again')
# %%
# num_letters
# The number of unique letters in the word that have not been guessed yet.
# %%
