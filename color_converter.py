from letter_object import LetterObject
from typing import List
from colorama import Fore as edit_color


class Convert:
    """
    This class adds color to each letter within a guess made by the user. The color is
    dependent on whether the letter is in the key word and whether the position of the letter
    is the same as it is in the key word
    """
    def color_append(result: List[LetterObject]):
        """
        Following standard coloring rules for Wordle, a letter is marked yellow
        if the letters are shared between words. A letter is marked green if the
        positions between words are the same.
        """
        
        # Gets back the letters after color is added
        colored_result = []

        for letter in result:

            # If the letter is in the correct position then it is green
            if letter.is_in_position:
                color = edit_color.GREEN

            # If the letter is in the word but not position then it is yellow
            elif letter.is_in_word:
                color = edit_color.YELLOW

            # If the letter is not in the word then is reset to white
            else: 
                color = edit_color.RESET
            
            # This changes the color of text before the letter is printed
            # It resets the color to avoid coloring all future letters
            colored_letter = color + letter.character + edit_color.RESET
            colored_result.append(colored_letter)
        
        # Retunrs the guess made by the user with color is any is appended
        return " ".join(colored_result) 