class LetterObject:
    """
    This class compares the key word to the user attempt and checks if the letters in the word guessed
    are in the key word. It also checks if the letter is in the correct position of the word.
    """
    def __init__(self, character: str):
        """
        Creates instances for whether the letter is in the key word 
        and if the letter is in the correct position of the key word.
        """
        self.character: str = character
        self.is_in_word: bool = False
        self.is_in_position: bool = False

    def __repr__(self):
        """
        Override to return a string. This string returned a boolean value for if a character is in the key word.
        It also returns a boolean value for if it is in the correct position of the word. This logic is similar to
        how colors are assigned to letters. This specific constructor was implemented for testing purposes.
        """
        return f"[{self.character} is in word: {self.is_in_word} is in position: {self.is_in_position}]"