#Author:Wilson Ma
#Date:11/28/2019
#Description:Creates a board game class where x must move diagonally to reach the final row and the o pieces
#must stop x from reaching the goal


class FBoard:
    """creates an 8x8 board game where x needs to reach the last row to win
    and o needs to prevent that to win """

    def __init__(self):
        """initializes game board and tracking data"""
        self._board = [

            ['', '', '', "x", '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ["o", '', "o", '', "o", '', "o", ''],
        ]
        self._game_state = "UNFINISHED"  # default game state
        self._current_row = 0  #helper used to enforce moving one row at a time
        self._current_x_row = 0  # tracks x's row coordinate
        self._current_x_column = 3  # tracks x's column coordinate

        #four coordinates tracking the available diagonal spaces of x
        self._lower_right = (self._current_x_row + 1, self._current_x_column + 1)
        self._lower_left = (self._current_x_row + 1, self._current_x_column - 1)
        self._upper_right = (self._current_x_row - 1, self._current_x_column + 1)
        self._upper_left = (self._current_x_row - 1, self._current_x_column - 1)

        #helper used to check if x is in the first column
        self._row1 = (
            self._board[0][0],
            self._board[1][0],
            self._board[2][0],
            self._board[3][0],
            self._board[4][0],
            self._board[5][0],
            self._board[6][0],
            self._board[7][0])
        #helper used to check if x is in the last column
        self._row7 = (
            self._board[0][7],
            self._board[1][7],
            self._board[2][7],
            self._board[3][7],
            self._board[4][7],
            self._board[5][7],
            self._board[6][7],
            self._board[7][7])

    def get_game_state(self):
        """returns current game state status"""
        return self._game_state

    def move_x(self, row, column):
        """function to move x piece in the game board by row and column"""

        #returns false if game has already been won
        if self._game_state != "UNFINISHED":
            return False

        # checks if x tries to move out of bounds
        if row not in range(8) or column not in range(8):
            return False

        # returns false/invalid move if x tries to move more than one row at a time or
        # non diagonal
        if (row - self._current_x_row) > 1 or (column - self._current_x_column) > 1 or (
                self._current_x_row - row) > 1 or (self._current_x_column - column) > 1:
            return False

        if self._current_x_column == column:
            return False

        if self._current_x_row == row:
            return False

        if "o" in self._board[row][column]:
            return False

        #places x in the specified row and column if the move is legal
        else:
            self._board[self._current_x_row].remove("x")
            self._board[self._current_x_row].append("")
            self._board[row][column] = "x"
            self._current_x_row = row
            self._current_x_column = column
            self._current_row += 1
            self._lower_right = (self._current_x_row + 1, self._current_x_column + 1)
            self._lower_left = (self._current_x_row + 1, self._current_x_column - 1)
            self._upper_right = (self._current_x_row - 1, self._current_x_column + 1)
            self._upper_left = (self._current_x_row - 1, self._current_x_column - 1)
            self._row1 = (
                self._board[0][0],
                self._board[1][0],
                self._board[2][0],
                self._board[3][0],
                self._board[4][0],
                self._board[5][0],
                self._board[6][0],
                self._board[7][0])

            self._row7 = (
                self._board[0][7],
                self._board[1][7],
                self._board[2][7],
                self._board[3][7],
                self._board[4][7],
                self._board[5][7],
                self._board[6][7],
                self._board[7][7])


            # checks if four "o" pieces surrounds x, if so, then x has no more moves and o wins
            if "x" not in self._board[7]:
                if "o" in self._board[self._lower_right[0]][self._lower_right[1]] and "o" in \
                    self._board[self._lower_left[0]][
                    self._lower_left[1]] and "o" in self._board[self._upper_right[0]][
                    self._upper_right[1]] and "o" in \
                    self._board[self._upper_left[0]][self._upper_left[1]]:
                        self._game_state = "O_WON"

            # checks if x is in the last column and o pieces surrounds x, x loses
            if "x" in self._row7 and "o" in self._board[self._lower_left[0]][self._lower_left[1]] and "o" in \
                    self._board[self._upper_left[0]][self._upper_left[1]]:
                self._game_state = "O_WON"

            # checks if x is in the first row and o surrounds x, x loses
            if "x" in self._board[0] and "o" in self._board[self._lower_right[0]][self._lower_right[1]] and "o" in \
                    self._board[self._lower_left[0]][self._lower_left[1]]:
                self._game_state = "O_WON"

            # checks if x is in the first column and o pieces surrounds x, x loses
            if "x" in self._row1 and "o" in self._board[self._lower_right[0]][self._lower_right[1]] and "o" in \
                    self._board[self._upper_right[0]][self._upper_right[1]]:
                self._game_state = "O_WON"

                # winning condition for "x" piece upon reaching last row
            if "x" in self._board[7]:
                    self._game_state = "X_WON"

            return True
    def move_o(self, row_from, column_from, row_to, column_to):
        """function that moves the 4 o pieces"""

        # returns false if game has already been won
        if self._game_state != "UNFINISHED":
            return False
        # returns false if move is out of bounds
        if row_to not in range(8) or column_to not in range(8):
            return False

        # returns false if piece is not moving diagonal maximum one row and column
        if row_to - row_from > 1 or column_to - column_from > 1 or column_from - column_to > 1:
            return False

        # returns false/invalid move if o tries to move to an  occupied space or
        #non-diagonal
        if self._board[row_to][column_to] == "o" or self._board[row_to][column_to] == "x":
            return False

        if column_from == column_to:
            return False
        if row_from == row_to:
            return False

        #moves o piece if legal and in correct starting coordinates
        if self._board[row_from][column_from] == "o":
            if row_to - row_from == -1:
                self._board[row_to][column_to] = "o"
                self._board[row_from][column_from] = ' '

            if "x" not in self._board[7]:
                if "o" in self._board[self._lower_right[0]][self._lower_right[1]] and "o" in self._board[self._lower_left[0]][
            self._lower_left[1]] and "o" in self._board[self._upper_right[0]][self._upper_right[1]] and "o" in \
            self._board[self._upper_left[0]][self._upper_left[1]]:
                    self._game_state = "O_WON"


        # if x is in the last column and o pieces surrounds x, x loses
            if "x" in self._row7 and "o" in self._board[self._lower_left[0]][self._lower_left[1]] and "o" in \
                self._board[self._upper_left[0]][self._upper_left[1]]:
                self._game_state = "O_WON"

        # if x is in the first row and o surrounds x, x loses
            if "x" in self._board[0] and "o" in self._board[self._lower_right[0]][self._lower_right[1]] and "o" in \
                self._board[self._lower_left[0]][self._lower_left[1]]:
                self._game_state = "O_WON"

        # checks if x is in the first column and o pieces surrounds x, x loses
            if "x" in self._row1 and "o" in self._board[self._lower_right[0]][self._lower_right[1]] and "o" in \
                self._board[self._upper_right[0]][self._upper_right[1]]:
                self._game_state = "O_WON"

        # winning condition for "x" piece upon reaching last row
            if "x" in self._board[7]:
                self._game_state = "X_WON"
            return True














