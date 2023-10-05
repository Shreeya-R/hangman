#%%
# Import random module into script
import random
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

        self.word_guessed = [ ]
        self.num_letters = num_letters
        self.list_of_guesses = [ ] 

    def check_guess(self, guess, word):
        '''
        This function takes the guessed letter as an argument and checks if the letter is in the secret word.
        '''
   
        # Convert guess to lowercase
        guess_lowercase = guess.lower()

        # Check if the guess is in the secret word
        word.find(guess_lowercase)

        if word.find(guess_lowercase) >= 0:
            print(f'Good guess! {guess_lowercase} is in the word.')

    def ask_for_input(self, word):
        '''
        This function validates whether or not thes input is a single alphabetical character.
        Also, uses the check_guess(guess) function to validate if the guessed letter is in the secret word.
        '''
        while True:
            guess = input('Please enter a single letter here: ')

            if len(guess) != 1 and guess.isalpha() == False:
                print(f'Invalid letter. Please enter a single alphabetical character.')
            elif list_of_guesses.index(guess) >= 0:
                print(f'You already tried that letter!')
            else:
                list_of_guesses == list_of_guesses.append(guess)
    
    return check_guess(guess, word)
    
    #%%
    # word_guessed
    # A list of the word with _ for each letter not yet guessed.
    def create_word_guessed():
        '''
        This function
        '''
        word_guessed = [ ]
        word_letters = [ ]
        word_lowercase = word.lower()

        for letter in word_lowercase:
            word_guessed == word_guessed.append('_')
            word_letters == word_letters.append(letter)
        print(word_guessed)

        # get guess value using ask_for_input function

        # Now need to replace _ with the letter guessed if it is in the word
        while word_guessed != word_letters: 
            # guess = input('Please enter a single letter here: ')

            guess = input('Please enter a single letter here: ')
            guess_lowercase = guess.lower()

            word_lowercase.find(guess_lowercase)

            if word_lowercase.find(guess_lowercase) >= 0:
                print(f'Good guess! {guess_lowercase} is in the word.')
                letter_position = word_lowercase.index(guess_lowercase)
                word_guessed[letter_position] = guess_lowercase
                print(word_guessed)
            else:
                print(f'Sorry, {guess_lowercase} is not in the word. Try again.')
#%%
# Initialising the following attributes
# word & word_list

word_list = ['Pineapple', 'Mango', 'Cherry', 'Apple', 'Strawberry']
word = random.choice(word_list)
print(word)
# %%
# num_letters
# The number of unique letters in the word that have not been guessed yet.

def create_num_letters():
    word_lowercase = word.lower()
    word_letters = [ ]
    
    for letter in word_lowercase:
        word_letters == word_letters.append(letter)
        num_letters = len(set(word_letters))
    return num_letters
# %%
create_num_letters()
# %%
