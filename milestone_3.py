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
