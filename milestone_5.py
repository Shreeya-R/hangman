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
        self.num_letters = len(set(self.word.lower()))

        self.word_guessed = ['_']*len(self.word)
        self.list_of_guesses = [ ] 

    def check_guess(self, guess):
        '''
        This function checks if a letter is contained in the word.

        The purpose of this function is to take the guessed letter as an argument and check if the letter is in the randomly chosen word.
        There are two options for the output of this function:
        1. Tells the user the guess is good.
        2. Tells the user the guess is not in the word. Provides the number of lives the user has left.

        Parameters:
            guess
        
        Returns:
            str: a string for whether or not the guess in contained in the word.
        '''
   
        # Convert guess to lowercase
        guess_lowercase = guess.lower()
        word_lowercase = self.word.lower()

        # Use find function as will return -1 if the letter is not in the word
        if word_lowercase.find(guess_lowercase) >= 0:
            print(f'Good guess! {guess_lowercase} is in the word.')

            for i,j in enumerate(word_lowercase):
                if j == guess_lowercase:
                    # letter_position = word_lowercase.index(guess_lowercase)
                    letter_position = i
                    self.word_guessed[letter_position] = guess_lowercase
            print(self.word_guessed)

            self.num_letters -= 1
            print(f'You have {self.num_letters} more unique letters left to guess!')
            return self.num_letters
        else:
            print(self.word_guessed)
            self.num_lives -= 1
            print(f'Sorry, {guess_lowercase} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        '''
        This function validates whether or not the input is a single alphabetical character.

        The purpose of this function is to ensure that the value of the input is valid for the Hangman class.
        The check_guess() function in used within this function to validate if the guessed letter is in the secret word. 
        Therefore, there is not need to run both these functions, the ask_for_input() function encompasses both.

        Returns:
            str: a string for whether or not the guess in contained in the word.
        '''
        while True:
            guess = input('Please enter a single letter here: ')

            if len(guess) != 1 and guess.isalpha() == False:
                print(f'Invalid letter. Please enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print(f'You already tried that letter!')
            else:
                print(f'You have guessed the letters {self.list_of_guesses} so far!')
                self.check_guess(guess)
                self.list_of_guesses == self.list_of_guesses.append(guess)
            break
#%%
# Create a function called play_game
def play_game(word_list):
    '''
    This function allows you to play the game Hangman using the Hangman class.

    The purpose...

    Parameters:

    '''
    num_lives = 5

    # Create instance for Hangman class called game
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            # Means game has ended and the user has lost
            print('You lost!')
            # tried to add break, but it doesn't seem to stop the code running
            break
        elif game.num_lives > 0 and game.num_letters > 0:
            # We want to continue the game in this case
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters == 0:
            # This means user has won the game
            print('Congratulations. You won the game!')
            break
# %%
word_list = ['Pineapple', 'Mango', 'Cherry', 'Apple', 'Strawberry']
play_game(word_list)
# %%
