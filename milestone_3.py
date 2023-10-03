#%%
# ask_for_input function
# Constantly asks user for a letter & validates it

def ask_for_input():
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

    return check_guess(guess)
# %%
ask_for_input()
# %%
# check_guess function
# Check if the letter guessed is in the secret word

def check_guess(guess):
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

# %%
check_guess(guess)
# %%
