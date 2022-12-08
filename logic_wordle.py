from letter_object import LetterObject

class Wordle:
    """
    This class contains all of the logic for the Wordle game. It contains the function that contain the key word for
    each given game. It also contains the functions that record the words guessed and the number of attempts. Based on
    the guesses and attempts, it checks if the conditions for playing the game are satisfied. If the key word has been 
    guessed or if the number of attempts left is zero, then the game is over.
    """
    # Possible attempts for a given game
    MAX_ATTEMPTS = 6

    # Length of the word used in game
    WORD_LENGTH = 5

    def __init__(self, key: str):
        """
        Constructor for an instance of the game. Creates the key value which becomes
        the word of the game. Also creates a list to store attempts made by the user.
        """
        self.key = key
        key: str = key.upper()
        self.attempts = []

    def get_attempt(self, word: str):
        """
        Adds the word guessed by the user to a list of attempts. These attempts are
        displayed on the game board until the game is over and reset.
        """
        self.word = word
        word = word.upper()
        self.attempts.append(word)

    def get_guess(self, word: str):
        """
        Compares a character against all letters in the key word to see if it is in the word. The letter is known to be in position 
        if the index of a character is the same as the index of the letter it shares the word with. Returns a list of letter positions. 
        """
        self.word = word
        word = word.upper()
        result = []

        # Loops through the letters of the key word and user input
        # Compares each index of the guessed word against each index of key word
        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = LetterObject(character)
            letter.is_in_word = character in self.key
            letter.is_in_position = character == self.key[i]
            result.append(letter)
        
        return result

    @property
    def prop_solved(self):
        """
        Fucction that is true if the last attempt is equal to the key word.
        It is checked in the main function of the game to see if the game is solved or not.
        """
        return len(self.attempts) > 0 and self.attempts[-1] == self.key

    @property
    def prop_remaining_attempts(self):
        """
        This function get the number of attempts remaining by subtracting the amount of 
        attempts from the maximum amount set for the game. This is 6 for most games of Wordle.
        """
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def prop_can_guess(self):
        """
        Function that is true if the number of guesses is not 0 or if the key word has not been solved.
        """
        return self.prop_remaining_attempts > 0 and self.prop_solved == False