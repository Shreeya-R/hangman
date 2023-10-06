#%%
import random
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
# create_word_guessed()
# %%
word_list = ['Pineapple', 'Mango', 'Cherry', 'Apple', 'Strawberry']
word = random.choice(word_list)