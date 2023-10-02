#%%
import random
#%%
# List 5 favourite fruits

favourite_fruits = ['Pineapple', 'Mango', 'Cherry', 'Apple', 'Strawberry']
print(favourite_fruits)
# %%
# Choose random word from the list

fruit = random.choice(favourite_fruits)
print(fruit)
# %%
# Ask user for input

guess = input('Please enter a single letter here: ')
print(guess)

# Check input is a single character & alphabetical
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
# %%
