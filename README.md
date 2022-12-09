# Worlde-Project
    In this project I designed my own window terminal version of Wordle. The main functionality of the program is to choose a random word form a word set and make that the "Word of the Day" for that game. The user enters in a guess and the guess is checked for validation and then it is compared to the word of the day. If the word is incorrect, the user may guess again using the same clues given as in the real game. If a letter from the guess is within the word of the day but not in the correct position, then is is highlighted as yellow. If a letter is from the user's guess in the correct position then it is highlighted green. If a letter has no correlation then it is kept as white. The standard rules for Wordle indicate that a user has six guesses per game and the length of the word of the day must be five letters long. Once the user has ran out of attempts or has succesfully guessed the word of the day, the game is terminated and prompts either a winning message or a losing message. If the user fails, the word of the day is revealed.
    How to play game? By accessing the word input folder and the Data class from source_wordle, you can generate a new text file containing the
total number of five letter words found in the input file. From here, running the main function in the game_wordle file will prompt the user by asking for a guess. By typing in the command window a user can enter guesses. If a guess is too short or too long or is not a real word then the user will enter a new guess for that attempt. Using a variety of words in a sequence of guesses will likely result in some colored letters that indicate whether a letter is in the correct position of the key word or not. Using this information, a user can make up to six guesses to solve the puzzle. If the user makes all six guesses and does not solve the puzzle, they are prompted with a losing message and the key word of the game. If the user guesses the word correctly before they run out of attempts, they are prompted with a winning message.From here, the game can be restarted and played with varios attempts allowed and various word lengths.
    One of the main classes in this program is the Wordle class which contains all of the logic for the game. This includes all the information
about the number of attempts remaining, whether a user can make a guess, and the properties of the game like word length and attempts allowed.
This information is important for designing the board and evaluating the win conidtions for the game. If there are no more attempts the game is temrinated. The Board class uses the word length to create a game board of an appropriate length for the game. Similarly, the Main class uses the word length and remaining attempts to create rows of empty lines to mimic place holders for guesses. For each attempt made, the number of these rows is decreased to allow for the word to fit on the board.
    Aside from creating the board, the Main class also takes the user inputted guess and checks if the answer fulfills the character count and if
it is a real word. Once verified, the word is then evaluated by another class called Convert. Here each letter is checked against each letter in the key word. The coloring of each letter in the user guess is decided in this class by checking their position and relevancy. Once the word has been checked and assigned color, then it is displayed on the board through another class called Results. This class takes the result of operations performed by other classes and interprets the information. This class places the guess on the line that correlates with the guess number. It also outputs the remaining attempts before asking for another guess if the game is continued.
    
