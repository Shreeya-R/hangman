# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Contents
1. [The Project](https://github.com/shhrreeyyaa/hangman#1-the-project)
2. [Installation Instructions](https://github.com/shhrreeyyaa/hangman#2-installation-instructions)
3. [Usage Instructions](https://github.com/shhrreeyyaa/hangman#3-usage-instructions)
4. [File Structure of the Project](https://github.com/shhrreeyyaa/hangman#4-file-structure-of-the-project)
5. [License Information](https://github.com/shhrreeyyaa/hangman#5-license-information)

## 1. The Project
### Description
The concept of this project is to create a game, which allows users to guess a random word using single letter guesses. The game will stop once the word has been guessed correctly or when the the user has run out of lives.

In order to achieve this, the Hangman Project required the construction of a class called Hangman and a function called play_game. The purpose of the Hangman class is to ensure that various attributes and methods are created and can be implemented into the final function play_game. The play_game function encompasses all the code required for the Hangman game to work, so that it can be played by a user through this single function. The game continues until the user guesses the word correctly or runs out of lives.

### What I've Learned
This Hangman Project has enabled me to nurture many skills in coding as well as deepen my overall Python knowledge.

Through this project my knowledge of classes and how to manipulate functions has strengthened. The success of this project has been due to the thorough knowledge of how to use control loops and understanding python data types and their attributes. As a whole, I enjoyed compiling the code to ensure the functionality of the Hangman game and solving solutions to errors that occurred along the way.

I can confidently say that this project has been a pleasure to work on and it has been a great starting point for my first ever github project.

## 2. Installation Instructions
To install the Hangman game, simply import the module **milestone_5.py**. By importing this module, one imports the random module, Hangman class and the play_game function. Additonally, if the module is called directly then the play_gmae function will automatically run upon importing.

![carbon](https://github.com/shhrreeyyaa/hangman/assets/141368354/ec3ee877-bf07-45fb-a785-5b035294c377)


Alternatively, one can import the entire **hangman folder** and import milestone_5.py separately. However, **milestone_5.py** does include if __name__ == '__main__', so the play_game function will not automatically run if the module is imported this way ie indirectly. In this case, the play_game function will need to be run after importing the module milestone_5.py.

![carbon1](https://github.com/shhrreeyyaa/hangman/assets/141368354/0eec3d4f-fe67-48d8-8cfa-890667881bcd)

## 3. Usage Instructions
### play_game
To play the Hangman game, simply run the function **play_game**. This will ask the user to continuously guess a single letter until the correct word is guessed or the user runs out of lives.

### Hangman class
This function requires the **Hangman class**, which contains the necessary attributes and methods that are vital for the play_game function to run. These methods include check_guess and ask_for_input, which we will look into in further detail below. 

For further information on the **Hangman class**, use help(Hangman) after importing the class.

### check_guess
The **check_guess** method is vital to check if a single letter that has been guessed is contained within the word to be guessed. Moreover, it is important to note that this method alters the values of the Hangman attributes num_lives and num_letters based on the given input. 

This method will not run unless the ask_for_input function is run first.

For further information on the **check_guess**, use help(Hangman) after importing the Hangman class.

### ask_for_input
The **ask_for_input** method is key for the play_game function to run due to the parameter 'guess' being defined in this method. Furthermore, this method checks that the guess is a single alphabetial character and adds the guess value to the list_of_guesses Hangman attribute.

For further information on the **ask_for_input**, use help(Hangman) after importing the Hangman class.

## 4. File Structure of the Project
The only file of interest to the user in this project is the milesstone_5.py file. The rest of the files are simply for trial and error of functions and methods.

## 5. License Information
Unfortunately, I could not find details for this information.
