#%%
# Write code that constantly asks user for a letter & validate it

while True:
    guess = input('Please enter a single letter here: ')

    if len(guess) == 1 and guess.isalpha():
        print(f'You have guessed the letter: {guess}.')
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
# %%
# Check if the letter guessed is in the secret word

# Secret word
secret_word = 'apple'
secret_word.find(guess)

if secret_word.find(guess) >= 0:
    print(f'Good guess! {guess} is in the word.')
else:
    print(f'Sorry, {guess} is not in the word. Try again.')
# %%
# check_guess function
def check_guess(guess):
    '''This function will take the guessed letter as an argument and check if the letter is in the word.'''
   
    # Convert guess to lowercase
    guess_lowercase = guess.lower()
    print(guess_lowercase)


    secret_word.find(guess)

    if secret_word.find(guess) >= 0:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

# %%
check_guess(guess)
# %%
