from wordle import Wordle
from colorama import Fore
from letter_state import LetterState
from typing import List
import random

def main():

    word_set = load_word_set("data/wordle_words.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input('\nInput your guess: ')

        if len(x) != wordle.WORD_LENGTH:
            print(
                Fore.RED 
                + f"Word must be {wordle.WORD_LENGTH} characters long" 
                + Fore.RESET
            )
            continue

        if not x in word_set:
            print(
                Fore.RED
                + f"{x} is not a valid word!"
                + Fore.RESET
            )
            continue

        wordle.attempt(x)
        display_results(wordle)
        
    if wordle.is_solved:
        print(f"You've solved the puzzle with {wordle.remaining_attempts} attempts left!")
    else:
        print("You've failed to solve the puzzle")
        print(f"The secret word was: {wordle.secret}")

def display_results(wordle: Wordle):
    print("\nYour results so far...\n")
    print(f"you have {wordle.remaining_attempts} attempts remaining.\n")
    
    lines = []
    
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
    
    for i in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    draw_boarder_around(lines)

def load_word_set(path: str):
    """
    Only keys no values
    """
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set

def convert_result_to_color(result: List[LetterState]):
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

if __name__ == "__main__":
    main()