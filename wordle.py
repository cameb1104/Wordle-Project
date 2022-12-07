from letter_state import LetterState

class Wordle:

    # Possible attempts for a given game
    MAX_ATTEMPTS = 6

    # Character length of word
    MAX_LENGTH = 5

    def __init__(self, key: str):
        """
        
        """
        self.key = key
        key: str = key.upper()
        self.attempts = []

    def get_attempt(self, word: str):
        """
        
        """
        self.word = word
        word = word.upper()
        self.attempts.append(word)

    def get_guess(self, word: str):
        """
        
        """
        self.word = word
        word = word.upper()
        result = []

        for i in range(self.MAX_LENGTH):
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in self.key
            letter.is_in_position = character == self.key[i]
            result.append(letter)
        
        return result

    @property
    def prop_solved(self):
        """

        """
        return len(self.attempts) > 0 and self.attempts[-1] == self.key

    @property
    def prop_remaining_attempts(self):
        """

        """
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def prop_can_guess(self):
        """

        """
        return self.prop_remaining_attempts > 0 and self.prop_solved == False
