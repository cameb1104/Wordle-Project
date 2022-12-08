from logic_wordle import Wordle

class Data:
    """
    Creates an output file of words to be used for the Wordle game.
    """
    def main():
        """
        Takes in a text file of words and checks if the words within the file
        are five letter long or not. For the words that are, they are added to a 
        list and then written into a new file. This file is used for randomly
        selecting a five letter word to be the key word of the game.
        """
        input_file = "data/word_input.txt"
        output_file = "data/word_output.txt"
        max_letter_words = []

        # Opens the file containing medium sized words and checks the length
        # Appends all five letter words to a list
        with open(input_file, "r") as f:
            for line in f.readlines():
                word = line.strip()
                if len(word) == Wordle.WORD_LENGTH:
                    max_letter_words.append(word)

        # Records the list of five letter words taken form the input file
        # Store in a new output file
        with open(output_file,  "w") as f:
            for word in max_letter_words:
                f.write(word + "\n")

        # Prints the number of five letter words with formatting
        print("-" * 59)
        print(f"There are {len(max_letter_words)} {(Wordle.WORD_LENGTH)} letter words found within the input file.")
        print("-" * 59)

    # Runs the function
    if __name__ == "__main__":
        main()