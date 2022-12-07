from letter_state import LetterState
from typing import List
from colorama import Fore


class Convert:
    def color_result(result: List[LetterState]):
        """
        
        """
        result_with_color = []
        for letter in result:
            if letter.is_in_position:
                color = Fore.GREEN
            elif letter.is_in_word:
                color = Fore.YELLOW
            else: 
                color = Fore.WHITE
            colored_letter = color + letter.character + Fore.RESET
            result_with_color.append(colored_letter)
        return " ".join(result_with_color)  

class Board:
    
    def draw_boarder_around(lines: list[str], size: int = 9, pad: int = 1):
        """
        
        """
        content_length = size + pad * 2
        top_border = "┌" + "─" * content_length + "┐"
        bottom_border = "└" + "─" * content_length + "┘"
        space = " " * pad

        print(top_border)

        for line in lines:
            print("│" + space + line + space + "│")
        
        print(bottom_border)