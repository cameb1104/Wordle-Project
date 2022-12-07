from wordle import Wordle
from colorama import Fore
from board import Board, Convert
import random

class LoadData:

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


class Results:

    def display_results(wordle: Wordle):
        print("\nYour results so far...\n")
        print(f"you have {wordle.prop_remaining_attempts} attempts remaining.\n")
        
        lines = []
        
        for word in wordle.attempts:
            result = wordle.get_guess(word)
            colored_result_str = Convert.color_result(result)
            lines.append(colored_result_str)
        
        for i in range(wordle.prop_remaining_attempts):
            lines.append(" ".join(["_"] * wordle.MAX_LENGTH))

        Board.draw_boarder_around(lines)


class Main(Results):

    def main():
        """
        main function
        """
        word_set = LoadData.load_word_set("data/wordle_words.txt")
        secret = random.choice(list(word_set))
        wordle = Wordle(secret)

        while wordle.prop_can_guess:
            x = input('\nInput your guess: ')

            if len(x) != wordle.MAX_LENGTH:
                print(
                    Fore.RED 
                    + f"Word must be {wordle.MAX_LENGTH} characters long" 
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

            wordle.get_attempt(x)
            Results.display_results(wordle)
            
        if wordle.prop_solved:
            print(f"You've solved the puzzle with {wordle.prop_remaining_attempts} attempts left!")
        else:
            print("You've failed to solve the puzzle")
            print(f"The secret word was: {wordle.key}")

# End check
if __name__ == "__main__":
    Main.main()
