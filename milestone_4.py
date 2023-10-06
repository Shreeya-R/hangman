#%%
# Import random module into script
import random
#%%
# Create Hangman class

class Hangman:
    '''
    This class is used to represent the game Hangman.

    Attributes:
        word (str): the word to be guessed, which is picked randomly from word_list.
        word_guessed (list): a list of the letters of the word, with _ for each letter not guessed yet.
        num_letters (int): the number of unique letters in the word that have not been guessed yet.
        num_lives (int): the number of lives a player has at the start of the game.
        word_list (list): a list of words that the guessed word will be chosen from.
        list_of_guesses (list): a list of guesses that have already been tried.
        
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)
        self.num_letters = len(set(self.word))

        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = [ ] 

    def check_guess(self, guess):
        '''
        This function checks if a letter is contained in the word.
        
        Returns:
            str: a string stating that the guess is in the word
        The purpose of this function is to take the guessed letter and word as arguments and check if the letter is in the word provided.
        '''
   
        # Convert guess to lowercase
        guess_lowercase = guess.lower()
        word_lowercase = self.word.lower()

        # Use find function as will return -1 if the letter is not in the word
        if word_lowercase.find(guess_lowercase) >= 0:
            print(f'Good guess! {guess_lowercase} is in the word.')

            for letter in word_lowercase:
                if letter == guess:
                    letter_position = word_lowercase.find(guess_lowercase)
                    self.word_guessed[letter_position] = guess_lowercase
                print(self.word_guessed)
            
            self.num_letters -= 1
            return self.num_letters
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess_lowercase} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        '''
        This function validates whether or not the input is a single alphabetical character.

        Returns:

        Also, uses the check_guess(guess) function to validate if the guessed letter is in the secret word.
        '''
        while True:
            guess = input('Please enter a single letter here: ')

            if len(guess) != 1 and guess.isalpha() == False:
                print(f'Invalid letter. Please enter a single alphabetical character.')
            elif self.list_of_guesses.count(guess) > 0:
                print(f'You already tried that letter!')
            else:
               self.list_of_guesses == self.list_of_guesses.append(guess)
               print(self.list_of_guesses)
               return self.check_guess(guess)
#%%
# Checking if the Hangman class attributes and methods work:
example = Hangman(['Pineapple', 'Mango', 'Cherry', 'Apple', 'Strawberry'])
# %%
example.word
# %%
example.list_of_guesses
# %%
example.num_letters
# %%
example.word_guessed
# %%
example.num_lives
#%%
example.ask_for_input()
# %%
