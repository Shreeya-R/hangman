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

        self.word = random.choice(word_list)

        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.list_of_guesses = list_of_guesses 

    def check_guess(guess, word):
        '''
        This function takes the guessed letter as an argument and checks if the letter is in the secret word.
        '''
   
        # Convert guess to lowercase
        guess_lowercase = guess.lower()

        # Check if the guess is in the secret word
        word.find(guess_lowercase)

        if word.find(guess_lowercase) >= 0:
            print(f'Good guess! {guess_lowercase} is in the word.')
        else:
            print(f'Sorry, {guess_lowercase} is not in the word. Try again.')

    def ask_for_input(word):
        '''
        This function validates whether or not thes input is a single alphabetical character.
        Also, uses the check_guess(guess) function to validate if the guessed letter is in the secret word.
        '''
        while True:
            guess = input('Please enter a single letter here: ')

            if len(guess) == 1 and guess.isalpha():
                print(f'You have guessed the letter: {guess}.')
                break
            else:
                print('Invalid letter. Please, enter a single alphabetical character.')

        return check_guess(guess, word)
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
def create_word_guessed():
    word_guessed = [ ]

    for letter in word:
        word_guessed == word_guessed.append('_')
    print(word_guessed)

    # get guess value using ask_for_input function

# Now need to replace _ with the letter guessed if it is in the word
    while True: 
        # guess = input('Please enter a single letter here: ')

        ask_for_input(word)

        for letter in word:
            if guess_lowercase == letter:
                letter_position = word.index(guess_lowercase)
                print(letter_position)
                word_guessed[letter_position] = guess_lowercase
            else: 
                print(f'{guess_lowercase} is not in the word. Try again')
# %%
# num_letters
# The number of unique letters in the word that have not been guessed yet.
# %%
create_word_guessed()
# %%
print(word)
# %%
