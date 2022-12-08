class Board:
    """
    This class contains the function that designs and draws the board for the game.
    This is done by using special box drawing characters for the edges of the box.
    """
    def design_border(lines: list[str], dim: int = 9, wall: int = 1):
        """
        This function uses the length of a word to create a top and bottom edge for the box.
        It creates the side edges by adding a verticle line to the beginning and end of each line.
        """
        
        # Creates a varible for the box dimensions
        # Takes into account spacing between words and the side edges
        word_length = dim + wall * 2
        upper_border = "╭" + "─" * word_length + "╮"
        lower_border = "╰" + "─" * word_length + "╯"
        space = " " * wall

        # Start from top to bottom
        # Prints the top edge
        print(upper_border)

        # Adds a verticle line on either side of the line to create a box without hard coding
        # This prints the side edges
        for line in lines:
            print("│" + space + line + space + "│")
        
        # Prints the bottem edge
        print(lower_border)