class XiangqiGame:
    """Represents the board for the game Xiangqi along with all of the movements and checks that are made during the game"""

    def __init__(self):
        """
        Initializes an empty game board and sets up a new game
            - Set up the initial turn to be player red's (so player red will make the first move
            - Set up the initial game state to be "UNFINISHED"
            - Set up the game pieces on the game board in their default positions
        Parameters: N/A
        Returns: N/A
        """

        self._board = [[""] * 9 for i in range(10)]
        self._turn = "red"
        self._game_state = "UNFINISHED"
        self._red_pieces = []
        self._black_pieces = []
        self.setup_board()

    def play_game(self):
        self.print_board()
        print("Player ", self._turn, "'s turn")
        print("Input the location of the piece that you wish to move: ")
        move1 = input()
        print("Input the new location of the piece: ")
        move2 = input()

        if self.make_move(move1, move2) is False:
            print("ERROR - Try again!")


    def setup_board(self):
        """
        Initializes all of thegame pieces for player red and player black in their default positions by calling on the instance of the game class
        Parameters: N/A
        Returns: N/A
        """
        self._board[0][0] = Chariot("red", "R")
        self._board[0][1] = Horse("red", "H")
        self._board[0][2] = Elephant("red", "E")
        self._board[0][3] = Advisor("red", "A")
        self._board[0][4] = General("red", "G")
        self._board[0][5] = Advisor("red", "A")
        self._board[0][6] = Elephant("red", "E")
        self._board[0][7] = Horse("red", "H")
        self._board[0][8] = Chariot("red", "R")
        self._board[2][1] = Cannon("red", "C")
        self._board[2][7] = Cannon("red", "C")
        self._board[3][0] = Soldier("red", "S")
        self._board[3][2] = Soldier("red", "S")
        self._board[3][4] = Soldier("red", "S")
        self._board[3][6] = Soldier("red", "S")
        self._board[3][8] = Soldier("red", "S")
        self._board[9][0] = Chariot("black", "R")
        self._board[9][1] = Horse("black", "H")
        self._board[9][2] = Elephant("black", "E")
        self._board[9][3] = Advisor("black", "A")
        self._board[9][4] = General("black", "G")
        self._board[9][5] = Advisor("black", "A")
        self._board[9][6] = Elephant("black", "E")
        self._board[9][7] = Horse("black", "H")
        self._board[9][8] = Chariot("black", "R")
        self._board[7][1] = Cannon("black", "C")
        self._board[7][7] = Cannon("black", "C")
        self._board[6][0] = Soldier("black", "S")
        self._board[6][2] = Soldier("black", "S")
        self._board[6][4] = Soldier("black", "S")
        self._board[6][6] = Soldier("black", "S")
        self._board[6][8] = Soldier("black", "S")


    def print_board(self, row1 = 5, row2 = 10, col1 = 9):
        """
        Prints a visualization of the game board with the game pieces
        Parameters:
            Default parameters (row1 / row2 / col1) to help with conciseness
        Returns:
            Visualization of the game board for testing purposes
        """

        print("   a", "    b", "    c", "    d", "    e", "    f", "    g", "    h", "    i")
        print("-------------------------------------------------------")

        for x in range(0, row1):
            for y in range(0, col1):
                space = self._board[x][y]
                if self._board[x][y] == "":
                    print("[ ", space, " ]", end="")
                else:
                    print("[", space.get_ID(), "]", end="")
            print(" ¦", x + 1, end = " ")
            print()

        river = "~~~~~~~~~~~~~~~~~~~~~~~~~RIVER~~~~~~~~~~~~~~~~~~~~~~~~~"
        print(river)

        for a in range(row1, row2):
            for b in range(0, col1):
                space = self._board[a][b]
                if self._board[a][b] == "":
                    print("[ ", space, " ]", end="")
                else:
                    print("[", space.get_ID(), "]", end="")

            print(" ¦", a + 1, end = " ")
            print()
        print("-------------------------------------------------------")


    def add_piece(self, piece_type, color, location):
        """
        Adds the game piece onto the game board and in their respective player's inventory
        The given location of the game piece can be alpha-numerical or only numerical
        Parameters:
            piece_type - Object type; denotes the game piece's type (ex. "General")
            color - color of the game piece
            location - can be alpha-numerical (ex. "F1") or a tuple (ex. (0, 5) for row 0, column 5)
        Returns: N/A
        """
        if type(location) == str:
            converted_loc = self.convert_alg(location)
            row = converted_loc[0]
            col = converted_loc[1]

        else:
            row = location[0]
            col = location[1]

        game_piece = piece_type(color, row, col)

        self._board[row][col] = game_piece

        if color == "red":
            self._red_pieces.append(game_piece)

        else:
            self._black_pieces.append(game_piece)


    def convert_alg(self, position):
        """
        Converts the letter from the algebraic notation into a number that reflects the game board's index by utilizing a dictionary with the key as the letter and the value as the index
        Parameters:
            position (str) - letter of the position in algebraic notation
        Returns:
            converted_value
        """

        alg_convert_dict = {
            "a" : 0,
            "b" : 1,
            "c" : 2,
            "d" : 3,
            "e" : 4,
            "f" : 5,
            "g" : 6,
            "h" : 7,
            "i" : 8
        }
        converted_value = alg_convert_dict[position[0]]
        return converted_value


    def get_opposite_color(self, color):
        """
        Returns the opposite color given as a parameter - used for getting the color of the opponent player
        Parameters:
            color (str) - color of the current player
        Returns:
            "black" / "red" - the opposite color from the parameter color
        """

        if color == "red":
            return "black"
        else:
            return "red"


    def end_turn(self):
        """
        Changes self._turn from one color to the other to indicate that it is now the other player's turn; used at the end of a successful move
        Parameters: N/A
        Returns: N/A
        """

        if self._turn == "red":
            self._turn = "black"
        else:
            self._turn = "red"


    def get_game_state(self):
        """
        Returns the current game state of the board ("UNFINISHED" / "RED_WON" / "BLACK_WON")
        Parameters: N/A
        Returns: self._game_state
        """

        return self._game_state


    def general_location(self, color):
        """
        Find the location of the specific color general
        Called By: check_flying_general() / is_in_check() / is_move_incheck()
        Parameters:
            color (str) - color of the general that will be located
        Returns:
            (x, y) - location of the general as a tuple; x is the row index, y is the column index
        """

        # find the location of the general by iterating through the board
        if color == "red":
            for x in range(10):
                for y in range(9):
                    piece = self._board[x][y]
                    if piece != "":
                        if piece.get_type() == "G" and piece.get_color() == "red":
                            return (x,y)

        if color == "black":
            for x in range(10):
                for y in range(9):
                    piece = self._board[x][y]
                    if piece != "":
                        if piece.get_type() == "G" and piece.get_color() == "black":
                            return (x,y)


    def check_available_moves(self, color):
        """
        Returns all the available moves that the specific color player can make, without causing the player to activate flying general or to become in-check status, by checking each piece of that color
        Utilized to check if player has any moves available - if none are available, then the player is in checkmate/stalemate and the game is over
        Parameters:
            color (str) - color of the player/game pieces that are checked
        Returns:
            available_moves (set) - a set of tuples that contains the movements available for the player in the form of (curr_row, curr_col, new_row, new_col) to designate the game piece's current position and allowed new position
        """

        # setup an empty set
        available_moves = set()

        # iterate through the game board and find a game piece that matches the given color
        for x in range(10):
            for y in range(9):
                space = self._board[x][y]

                # call on the game piece's get_all_possible_moves() to get a list of possible moves that have NOT been filtered for flying general or causing in-check status
                # filter the list of possible move with the two methods
                if space != "" and space.get_color() == color:
                    allowed_move = space.get_all_possible_moves(x, y, self._board)

                    for move in allowed_move:
                        new_row = move[0]
                        new_col = move[1]

                        # after getting the allowed moves, filter through to ensure that they are legal
                        if self.check_flying_general(space.get_type(), x, y, new_row, new_col) is False:
                            if self.is_move_incheck(x, y, new_row, new_col) is False:

                                # add the tuple representing the valid move into the set
                                allowed_movement = (x, y, new_row, new_col)
                                available_moves.add(allowed_movement)

        return available_moves


    def is_move_incheck(self, curr_row, curr_col, new_row, new_col):
        """
        Checks whether moving a player's game piece from its current location to a new location will cause/continue the player to be in-check status
        Utilizes is_in_check()
        Parameters:
            curr_row (str) - current row of the game piece on the game board
            curr_col (str) - current column of the game piece on the game board
            new_row (str) - possible new row of the game piece
            new_col (str) - possible new column of the game piece
        Returns:
            True - if moving of the game piece causes/continues the player to be in-check status
            False - if moving the game piece does not cause the player to be in-check status and/or stops the player from being in-check status
        """

        curr_space = self._board[curr_row][curr_col]
        new_space = self._board[new_row][new_col]
        player = curr_space.get_color()

        # move the piece into the new location to check if this causes an in-check
        self._board[new_row][new_col] = curr_space
        self._board[curr_row][curr_col] = ""

        # if movement caused the player to become in-check, return True
        if self.is_in_check(player) is True:
            # put the game pieces back in their previous position
            self._board[curr_row][curr_col] = curr_space
            self._board[new_row][new_col] = new_space

            return True

        else:
            # put the game pieces back in their previous position, even if the movement doesn't cause the player to become in-check
            self._board[curr_row][curr_col] = curr_space
            self._board[new_row][new_col] = new_space

            return False


    def is_in_check(self, color):
        """
        Checks whether the specified color player is in-check status due to their general being open to being captured by an opponent's game piece
        Parameters:
            color (str) - color of the specified player that we're checking the in-check status for
        Returns:
            True - if player is in-check status (general is threatened)
            False - if player is not in-check status (general is not threatened)
        """

        player = color
        opponent = self.get_opposite_color(color)

        # find the player's general's location on the game board
        general_location = self.general_location(color)
        gen_row = general_location[0]
        gen_col = general_location[1]

        # initialize a counter to count how many of the opponent's game pieces can capture the player's general
        # if the counter != 0, then the player is in check because at least 1 of the opponent's game pieces can capture the player's general and end the game
        counter = 0

        # iterate through the board and find pieces that belong to the opponent of that color player
        for x in range(10):
            for y in range(9):
                space = self._board[x][y]

                if space != "" and space.get_color() == opponent:

                    # check whether the opponent's game piece can reach the player's general and whether the move is valid
                    if space.is_move_valid(x, y, gen_row, gen_col, self._board) is True:
                        if self.check_flying_general(space.get_type(), x, y, gen_row, gen_col) is False:

                            counter += 1

        if counter != 0:
            return True

        else:
            return False


    def check_flying_general(self, piece_type, curr_row, curr_col, new_row, new_col):
        """
        Check whether flying general occurs if the game piece in the current location is moved to the new location (making the move invalid)
        Flying general will occur if...
            1.) The red and black generals are in the same column
            2.) There are no game pieces (of any color) in-between the two generals
        Parameters:
            curr_row (str) - current row of the game piece on the game board
            curr_col (str) - current column of the game piece on the game board
            new_row (str) - possible new row of the game piece
            new_col (str) - possible new column of the game piece
        Returns:
            True - if moving the piece causes flying general
            False - if moving the piece does NOT cause flying general
            """

        # counter will be used to count how many game pieces are in-between the set ranges
        pieces_counter = 0

        moving_piece = self._board[curr_row][curr_col]
        piece_color = moving_piece.get_color()

        # find location of the piece's same color general
        player = piece_color
        player_gen = self.general_location(piece_color)
        player_row = player_gen[0]
        player_col = player_gen[1]

        # find location of the opponent's general
        opponent = self.get_opposite_color(player)
        opponent_gen = self.general_location(opponent)
        opponent_row = opponent_gen[0]
        opponent_col = opponent_gen[1]


        # check for flying general if the piece being moved is a General type
        if piece_type == "G":

            # check if the new column of the General piece will the same as the opponent's General
            # if the General is being moved to a different column than the opponent's General, then flying general cannot occur
            if new_col != opponent_col:
                return False

            # check if there are any pieces that will be between the newly moved General and the opponent General
            if new_row > opponent_row:
                for x in range(opponent_row + 1, new_row):
                    board_space = self._board[x][new_col]

                    if board_space != "":
                        pieces_counter += 1

                # if there's at least 1 game piece between the two, then flying general will be avoided
                if pieces_counter > 0:
                    return False

                else:
                    return True

            if opponent_row > new_row:
                for x in range(new_row + 1, opponent_row):
                    board_space = self._board[x][new_col]

                    if board_space != "":
                        pieces_counter += 1

                # if there's at least 1 game piece between the two, then flying general will be avoided
                if pieces_counter > 0:
                    return False

                else:
                    return True

        # check for flying general if the piece being moved is NOT a General type
        if piece_type != "G":

            # check if the two generals are on the same column - if not, then flying general cannot occur
            if player_col != opponent_col:
                return False

            # check if the game piece is currently in the same column as the player's general
            if curr_col != player_col:
                return False

            # check if the piece is between the red and black generals - if not, then moving the piece should have no effect on flying general
            if player_row < curr_row < opponent_row or player_row > curr_row > opponent_row:

                if player_row > opponent_row:
                    for x in range(opponent_row + 1, player_row):
                        board_space = self._board[x][curr_col]

                        if board_space != "":
                            pieces_counter += 1

                    # if there are at least 2 game pieces in-between the two generals (including the game piece being moved), then flying general will not occur since there will be at least 1 game piece still keeping the generals out of sight from each other
                    if pieces_counter > 1:
                        return False

                    else:
                        return True

                if opponent_row > player_row:

                    for x in range(player_row + 1, opponent_row):
                        board_space = self._board[x][curr_col]

                        if board_space != "":
                            pieces_counter += 1

                    # if there are at least 2 game pieces in-between the two generals (including the game piece being moved), then flying general will not occur since there will be at least 1 game piece still keeping the generals out of sight from each other
                    if pieces_counter > 1:
                        return False

                    else:
                        return True

            else:
                # game piece is NOT between the two generals, so flying general cannot occur
                return False


    def is_move_valid(self, curr_row, curr_col):
        """
        Checks whether the player is making a valid move regarding the current game piece (or lack of) on the given board location
        Parameters:
            curr_row (str) - current row of the game piece on the game board
            curr_col (str) - current column of the game piece on the game board
        Returns:
            True - if the given location contains a game piece that belongs to the player
            False - if the given location DOES NOT contain a game piece (i.e. empty space) or if the game piece DOES NOT belong to the player
        """

        curr_space = self._board[curr_row][curr_col]

        # check if the current board location contains a game piece - if it's empty, return False
        if curr_space == "":
            return False

        # check if the curr_space's piece is the same color as the player's - cannot move a piece that's a different color than the player
        if curr_space.get_color() == self._turn:
            return True

        else:
            return False


    def get_out_incheck(self, curr_row, curr_col, new_row, new_col):
        """
        Check whether the in-check player is making a move that gets themselves out of check
        Parameters:
            curr_row (str) - current row of the game piece on the game board
            curr_col (str) - current column of the game piece on the game board
            new_row (str) - possible new row of the game piece
            new_col (str) - possible new column of the game piece
        Returns:
             True - if the in-check player's move gets them out of in-check status
             False - if the in-check player's move DOES NOT get them out of in-check status (invalid move)
        """

        curr_space = self._board[curr_row][curr_col]
        new_space = self._board[new_row][new_col]

        # find all of the player's available moves that will get it out of in-check status
        out_incheck_moves = self.check_available_moves(self._turn)

        # initialize a counter that will increment by +1 each time the program finds that the player's move is not within the out_incheck_moves
        counter = 0

        # iterate through all the moves to see if the player's move matches any of the out_incheck_moves
        for move in out_incheck_moves:

            # if the player's move matches one of the moves in out_incheck_moves, then the player will get out of in-check status
            if curr_row == move[0] and curr_col == move[1] and new_row == move[2] and new_col == move[3]:
                return True

            else:
                counter += 1

        if counter > 0:
            return False


    def make_move(self, pos1, pos2):
        """
        Moves the player's game piece from pos1 to pos2 during their turn; will check whether the movement from pos1 to pos2 is an invalid move
        Parameters:
            pos1 (str) - current position of the game piece in algebraic notation
            pos2 (str) - new position of the game piece in algebraic notation
        Returns:
            True - if the move is valid
            False - if the move is invalid (due to being out of bounds, etc.)
        """

        # convert algebraic notation into row/col indices
        curr_col = self.convert_alg(pos1)
        curr_row = int(pos1[1:]) - 1

        new_col = self.convert_alg(pos2)
        new_row = int(pos2[1:]) - 1

        # find the game pieces/empty space on the board positions at the current location and new location
        curr_space = self._board[curr_row][curr_col]
        new_space = self._board[new_row][new_col]

        player = self._turn
        opponent = self.get_opposite_color(self._turn)

        # check if game is already won
        if self._game_state != "UNFINISHED":
            return False

        # check if there is actually movement of the game piece
        if (new_row == curr_row) and (new_col == curr_col):
            return False

        # check if current player is in-check - if so, then go through another pathway where the player's movement must be one that can get it out of check
        if self.is_in_check(player) is True:
            if self.get_out_incheck(curr_row, curr_col, new_row, new_col) is False:
                return False

        # check if curr_space.. 1.) contains a game piece    2.) if the game piece is the same color as the player
        if self.is_move_valid(curr_row, curr_col) is False:
            return False

        # check if moving the piece from pos1 -> pos2 is valid
        # make_move function will also check what is contained in the new_space along with whether the new location is out of bounds
        if curr_space.is_move_valid(curr_row, curr_col, new_row, new_col, self._board) is False:
            return False

        # check if moving the piece causes a flying general
        if self.check_flying_general(curr_space.get_type(), curr_row, curr_col, new_row, new_col) is True:
            return False

        #check if move causes current player's general to be in-check
        if self.is_move_incheck(curr_row, curr_col, new_row, new_col) is True:
            return False

        # if all of these checks are passed, then the move is valid
        # move the game piece from pos1 -> pos2 and update the board
        self._board[new_row][new_col] = curr_space
        self._board[curr_row][curr_col] = ""


        ### END GAME CALCULATIONS
        # assess whether the player's move caused any changes to the status of the game along with the opponent's possible future moves and/or opponent's in-check status

        # check if the opponent player has any available moves
        opp_moves = self.check_available_moves(opponent)

        # if the opponent has at least 1 available move, check whether the opponent is in-check status from the player's move
        if len(opp_moves) != 0:

            # if the opponent has at least 1 available move and is in-check status, then the opponent must move to ensure that they get out of in-check status in the next turn
            # game remains unfinished
            if self.is_in_check(opponent) is True:
                self.end_turn()
                return True

            # if the opponent has at least 1 available move and is NOT in-check status, then the game continues without any changes to the game state
            # game remains unfinished
            else:
                self.end_turn()
                return True


        # if opponent does not have any available moves, then the game has been won by the current player
        # checkmate vs. stalemate will not be differentiated since they both lead to a player winning the game

        else:

            if player == "red":
                    self._game_state = "RED_WON"
                    self.end_turn()
                    return True


            elif player == "black":
                    self._game_state = "BLACK_WON"
                    self.end_turn()
                    return True



class Piece:
    """Parent Class for all of the pieces on the board"""

    def __init__(self, color, p_type):
        """Initializes the game piece with a color ("red"/"black") and type (based on the seven game pieces in Xiangqi)"""
        self._color = color
        self._type = p_type

    def get_ID(self):
        """Create an ID data member which is solely used for printing purposes"""
        if self._color == "red":
            self._ID = "r" + self._type
        else:
            self._ID = "b" + self._type
        return self._ID

    def get_type(self):
        """Returns the type of the piece"""
        return self._type

    def get_color(self):
        """Returns the color of the piece"""
        return self._color

    def get_curr_row(self):
        """Returns the row location of the piece"""
        return self._curr_row

    def get_curr_col(self):
        """Returns the column location of the piece"""
        return self._curr_col



class General(Piece):
    """
    A child class of parent class Piece - represents a General game piece
    The General moves 1 space orthogonally and cannot leave the "palace"
    """

    def is_move_valid(self, curr_row, curr_col, new_row, new_col, board):
        """
        Returns True if the game piece can be moved from the current position to the new position
        Does not take into account whether flying general activates or if the move puts the player in-check status
        """

        # check if new locations is out of the board
        if new_row < 0 or new_row > 9 or new_col < 0 or new_col > 8:
            return False

        curr_space = board[curr_row][curr_col]
        new_space = board[new_row][new_col]

        row_diff = abs(curr_row - new_row)
        col_diff = abs(curr_col - new_col)

        # check if new location contains an empty space / enemy / ally
        if new_space == "":
            enemy = False

        elif new_space.get_color() != self._color:
            enemy = True

        else:
            # cannot make a move to a new space if the new location has an ally piece
            return False

        # check if new movement is within the palace
        if self._color == "red":

            if new_row > 2 or new_row < 0 or new_col > 5 or new_col < 3:
                return False

        if self._color == "black":

            if new_row > 9 or new_row < 7 or new_col > 5 or new_col < 3:
                return False


        possible_moves = self.possible_movements()
        for move in possible_moves:
            x = new_row - curr_row
            y = new_col - curr_col

            if move == (x, y):
                return True

        return False


    def possible_movements(self):
        """Returns the possible movements of the General piece"""

        m1 = (1, 0)
        m2 = (-1, 0)
        m3 = (0, 1)
        m4 = (0, -1)
        moves_list = [m1, m2, m3, m4]

        return moves_list

    def get_all_possible_moves(self, curr_row, curr_col, board):
        """Returns all of the possible moves that the game piece can make while at the current position"""
        curr_space = board[curr_row][curr_col]
        all_possible_moves = []

        possible_moves = self.possible_movements()

        for move in possible_moves:
            new_row = move[0] + curr_row
            new_col = move[1] + curr_col
            if self.is_move_valid(curr_row, curr_col, new_row, new_col, board) is True:
                all_possible_moves.append((new_row, new_col))

        return all_possible_moves


class Advisor(Piece):
    """
    A child class of parent class Piece - represents an Advisor game piece
    The Advisor moves 1 space diagonally and cannot leave the "palace"
    """

    def is_move_valid(self, curr_row, curr_col, new_row, new_col, board):
        """
        Returns True if the game piece can be moved from the current position to the new position
        Does not take into account whether flying general activates or if the move puts the player in-check status
        """

        # check if new locations is out of the board
        if new_row < 0 or new_row > 9 or new_col < 0 or new_col > 8:
            return False

        curr_space = board[curr_row][curr_col]
        new_space = board[new_row][new_col]

        row_diff = abs(curr_row - new_row)
        col_diff = abs(curr_col - new_col)

        # check if new location contains an empty space / enemy / ally
        if new_space == "":
            enemy = False

        elif new_space.get_color() != self._color:
            enemy = True

        else:
            # cannot make a move to a new space if the new location has an ally piece
            return False

        # check if new movement is within the palace
        if self._color == "red":

            if new_row > 2 or new_row < 0 or new_col > 5 or new_col < 3:
                return False

        if self._color == "black":

            if new_row > 9 or new_row < 7 or new_col > 5 or new_col < 3:
                return False

        possible_moves = self.possible_movements()
        for move in possible_moves:
            x = new_row - curr_row
            y = new_col - curr_col

            if move == (x, y):
                return True

        return False


    def possible_movements(self):
        """Returns the possible movements of the Advisor piece"""
        m1 = (1, 1)
        m2 = (-1, -1)
        m3 = (-1, 1)
        m4 = (1, -1)
        moves_list = [m1, m2, m3, m4]

        return moves_list

    def get_all_possible_moves(self, curr_row, curr_col, board):
        """Returns all of the possible moves that the game piece can make while at the current position"""
        curr_space = board[curr_row][curr_col]
        all_possible_moves = []

        possible_moves = self.possible_movements()

        for move in possible_moves:
            new_row = move[0] + curr_row
            new_col = move[1] + curr_col
            if self.is_move_valid(curr_row, curr_col, new_row, new_col, board) is True:
                all_possible_moves.append((new_row, new_col))

        return all_possible_moves


class Elephant(Piece):
    """
    A child class of parent class Piece - represents an Elephant game piece
    The Elephant moves 2 space diagonally and cannot cross the "river"
    """

    def is_move_valid(self, curr_row, curr_col, new_row, new_col, board):
        """
        Returns True if the game piece can be moved from the current position to the new position
        Does not take into account whether flying general activates or if the move puts the player in-check status
        """

        # check if new locations is out of the board
        if new_row < 0 or new_row > 9 or new_col < 0 or new_col > 8:
            return False

        curr_space = board[curr_row][curr_col]
        new_space = board[new_row][new_col]

        # check if new location contains an empty space / enemy / ally
        if new_space == "":
            enemy = False

        elif new_space.get_color() != self._color:
            enemy = True

        else:
            # cannot make a move to a new space if the new location has an ally piece
            return False

        # check if new location causes Elephant to move past the river - which is not a valid move
        if self._color == "red":
            if new_row > 4:
                return False

        if self._color == "black":
            if new_row < 5:
                return False

        row_mid = (new_row + curr_row) // 2
        col_mid = (new_col + curr_col) // 2

        possible_moves = self.possible_movements()
        for move in possible_moves:
            x = new_row - curr_row
            y = new_col - curr_col

            if move == (x, y):

                # check if there's any pieces blocking the Elephants movement
                if board[row_mid][col_mid] != "":
                    return False

                return True

        return False

    def possible_movements(self):
        """Returns the possible movements of the Elephant piece"""
        m1 = (2, 2)
        m2 = (-2, -2)
        m3 = (2, -2)
        m4 = (-2, 2)
        moves_list = [m1, m2, m3, m4]
        return moves_list

    def get_all_possible_moves(self, curr_row, curr_col, board):
        """Returns all of the possible moves that the game piece can make while at the current position"""
        curr_space = board[curr_row][curr_col]
        all_possible_moves = []

        possible_moves = self.possible_movements()

        for move in possible_moves:
            new_row = move[0] + curr_row
            new_col = move[1] + curr_col
            if self.is_move_valid(curr_row, curr_col, new_row, new_col, board) is True:
                all_possible_moves.append((new_row, new_col))

        return all_possible_moves


class Horse(Piece):
    """
    A child class of parent class Piece - represents a Horse game piece
    The Horse moves 1 space orthogonally and then 1 space diagonally away from the previous space
    The Horse can be blocked
    """

    def is_move_valid(self, curr_row, curr_col, new_row, new_col, board):
        """
        Returns True if the game piece can be moved from the current position to the new position
        Does not take into account whether flying general activates or if the move puts the player in-check status
        """
        # check if new locations is out of the board
        if new_row < 0 or new_row > 9 or new_col < 0 or new_col > 8:
            return False

        curr_space = board[curr_row][curr_col]
        new_space = board[new_row][new_col]

        # check if new location contains an empty space / enemy / ally
        if new_space == "":
            enemy = False

        elif new_space.get_color() != self._color:
            enemy = True

        else:
            # cannot make a move to a new space if the new location has an ally piece
            return False

        # check if movement from current to new location is possible based on the the piece's movement characteristics

        row_mid = (new_row + curr_row) // 2
        col_mid = (new_col + curr_col) // 2

        possible_moves = self.possible_movements()
        for move in possible_moves:
            x = new_row - curr_row
            y = new_col - curr_col

            # if the movement is allowed, check if the Horse is blocked
            if move == (x, y):

                if abs(x) > abs(y):
                    if board[row_mid][curr_col] == "":
                        return True
                    else:
                        return False

                else:
                    if board[curr_row][col_mid] == "":
                        return True

                    else:
                        return False

        return False

    def possible_movements(self):
        """Returns the possible movements of the Horse piece"""
        m1 = (2, 1)
        m2 = (2, -1)
        m3 = (-2, 1)
        m4 = (-2, -1)
        m5 = (1, 2)
        m6 = (1, -2)
        m7 = (-1, 2)
        m8 = (-1, -2)
        moves_list = [m1, m2, m3, m4, m5, m6, m7, m8]
        return moves_list

    def get_all_possible_moves(self, curr_row, curr_col, board):
        """Returns all of the possible moves that the game piece can make while at the current position"""
        curr_space = board[curr_row][curr_col]
        all_possible_moves = []

        possible_moves = self.possible_movements()

        for move in possible_moves:
            new_row = move[0] + curr_row
            new_col = move[1] + curr_col
            if self.is_move_valid(curr_row, curr_col, new_row, new_col, board) is True:
                all_possible_moves.append((new_row, new_col))

        return all_possible_moves


class Chariot(Piece):
    """
    A child class of parent class Piece - represents a Chariot game piece
    The Chariot can move any space orthogonally but cannot jump over any pieces between it's original position and it's ending position
    The Chariot stops once it has reached the borders of the board or has reaches another piece (ally or enemy)
    """

    def is_move_valid(self, curr_row, curr_col, new_row, new_col, board):
        """
        Returns True if the game piece can be moved from the current position to the new position
        Does not take into account whether flying general activates or if the move puts the player in-check status
        """

        # check if new locations is out of the board
        if new_row < 0 or new_row > 9 or new_col < 0 or new_col > 8:
            return False

        curr_space = board[curr_row][curr_col]
        new_space = board[new_row][new_col]

        # check if new location contains an empty space / enemy / ally
        if new_space == "":
            enemy = False

        elif new_space.get_color() != self._color:
            enemy = True

        else:
            # cannot make a move to a new space if the new location has an ally piece
            return False

        # check if movement from current to new location is possible based on the the piece's movement characteristics

        # chariot cannot "jump" over any pieces that stands between its current location and new location
        allowed_jump = 0
        jump_counter = 0

        row_diff = new_row - curr_row
        col_diff = new_col - curr_col

        # check movement for when chariot is moving horizontally with at least 1 movement in column
        if curr_row == new_row and abs(col_diff) > 0:

            # if chariot is moving to the right
            if new_col > curr_col:
                for y in range(curr_col + 1, new_col):
                    if board[new_row][y] != "":
                        jump_counter += 1

            # if chariot is moving to the left
            if curr_col > new_col:

                for y in range(new_col + 1, curr_col):
                    if board[new_row][y] != "":
                        jump_counter += 1

        # check movement for when chariot is moving vertically with at least 1 movement in row
        elif curr_col == new_col and abs(row_diff) > 0:

            # if chariot is moving downwards
            if new_row > curr_row:
                for x in range(curr_row + 1, new_row):
                    if board[x][new_col] != "":
                        jump_counter += 1

            # if chariot is moving upwards
            if curr_row > new_row:
                for x in range(new_row + 1, curr_row):
                    if board[x][new_col] != "":
                        jump_counter += 1

        else:
            return False

        if jump_counter == allowed_jump:
            return True

        else:
            return False

    def possible_movements(self):
        """Returns the possible movements of the Chariot piece"""
        moves_list = []

        for x in range(1, 10):
            moves_list.append((x, 0))
        for x in range(-9, 0):
            moves_list.append((x, 0))
        for y in range(1, 9):
            moves_list.append((0, y))
        for y in range(-8, 0):
            moves_list.append((0, y))
        return moves_list

    def get_all_possible_moves(self, curr_row, curr_col, board):
        """Returns all of the possible moves that the game piece can make while at the current position"""
        curr_space = board[curr_row][curr_col]
        all_possible_moves = []

        possible_moves = self.possible_movements()

        for move in possible_moves:
            new_row = move[0] + curr_row
            new_col = move[1] + curr_col
            if self.is_move_valid(curr_row, curr_col, new_row, new_col, board) is True:
                all_possible_moves.append((new_row, new_col))

        return all_possible_moves


class Cannon(Piece):
    """
    A child class of parent class Piece - represents a Cannon game piece
    The Cannon can move any space orthogonally (like the Chariot)
    The Cannon captures an enemy by "jumping" over a single piece that is along the path of attack - there can be any number of unoccupied spaces between the cannon / jumping piece / enemy piece
    """

    def is_move_valid(self, curr_row, curr_col, new_row, new_col, board):
        """
        Returns True if the game piece can be moved from the current position to the new position
        Does not take into account whether flying general activates or if the move puts the player in-check status
        """

        # check if new locations is out of the board
        if new_row < 0 or new_row > 9 or new_col < 0 or new_col > 8:
            return False

        curr_space = board[curr_row][curr_col]
        new_space = board[new_row][new_col]


        # check if new location contains an empty space / enemy / ally
        if new_space == "":
            enemy = False

        elif new_space.get_color() != self._color:
            enemy = True

        else:
            # cannot make a move to a new space if the new location has an ally piece
            return False

        # check if movement from current to new location is possible based on the the piece's movement characteristics
        # cannon might need to jump over an ally/enemy piece, depending on what's at the new location - thus, use a jump counter

        jump_counter = 0

        row_diff = new_row - curr_row
        col_diff = new_col - curr_col


        # check movement for when chariot is moving horizontally with at least 1 movement in column
        if curr_row == new_row and abs(col_diff) > 0:

            # if chariot is moving to the right
            if new_col > curr_col:
                for y in range(curr_col + 1, new_col):
                    if board[new_row][y] != "":
                        jump_counter += 1

            # if chariot is moving to the left
            if curr_col > new_col:
                for y in range(new_col + 1, curr_col):
                    if board[new_row][y] != "":
                        jump_counter += 1

        # check movement for when chariot is moving vertically with at least 1 movement in row
        elif curr_col == new_col and abs(row_diff) > 0:

            # if chariot is moving downwards
            if new_row > curr_row:
                for x in range(curr_row + 1, new_row):
                    if board[x][new_col] != "":
                        jump_counter += 1

            # if chariot is moving upwards
            if curr_row > new_row:
                for x in range(new_row + 1, curr_row):
                    if board[x][new_col] != "":
                        jump_counter += 1

        else:
            return False

        # if the Cannon's new location contains an enemy piece, then the enemy must be captured which is only doable if there's only 1 piece standing between the Cannon and the enemy
        if enemy == True:
            if jump_counter == 1:
                return True
            else:
                return False

        # if the Cannon's new location does not contain an enemy piece, it cannot make any jumps over game pieces
        if enemy == False:
            if jump_counter == 0:
                return True

            else:
                return False


    def possible_movements(self):
        """Returns the possible movements of the Cannon piece"""
        moves_list = []

        for x in range(1, 10):
            moves_list.append((x, 0))
        for x in range(-9, 0):
            moves_list.append((x, 0))
        for y in range(1, 9):
            moves_list.append((0, y))
        for y in range(-8, 0):
            moves_list.append((0, y))
        return moves_list

    def get_all_possible_moves(self, curr_row, curr_col, board):
        """Returns all of the possible moves that the game piece can make while at the current position"""
        curr_space = board[curr_row][curr_col]
        all_possible_moves = []

        possible_moves = self.possible_movements()

        for move in possible_moves:
            new_row = move[0] + curr_row
            new_col = move[1] + curr_col
            if self.is_move_valid(curr_row, curr_col, new_row, new_col, board) is True:
                all_possible_moves.append((new_row, new_col))

        return all_possible_moves


class Soldier(Piece):
    """
    A child class of parent class Piece - represents a Soldier game piece
    The Soldier can move 1 space forward before having crossed the river
     After the Solider has crossed the river, it can move 1 space forward/left/right but not backward
    """

    def is_move_valid(self, curr_row, curr_col, new_row, new_col, board):
        """
        Returns True if the game piece can be moved from the current position to the new position
        Does not take into account whether flying general activates or if the move puts the player in-check status
        """
        # check if new locations is out of the board
        if new_row < 0 or new_row > 9 or new_col < 0 or new_col > 8:
            return False

        curr_space = board[curr_row][curr_col]
        new_space = board[new_row][new_col]


        # check if new location contains an empty space / enemy / ally
        if new_space == "":
            enemy = False

        elif new_space.get_color() != self._color:
            enemy = True

        else:
            # cannot make a move to a new space if the new location has an ally piece
            return False

        # check if movement from current to new location is possible based on the the piece's movement characteristics

        row_diff = new_row - curr_row
        col_diff = new_col - curr_col
        counter = 0

        possible_moves = self.possible_movements()
        for move in possible_moves:
            x = new_row - curr_row
            y = new_col - curr_col

            if move != (x, y):
                counter += 1

        if counter == 4:
            return False

        # check whether the Soldier is red or black, since that determines where they cross the river

        # check movement for Red Soldier
        if self._color == "red":
            # check if Soldier has crossed the river
            # didn't cross river
            if curr_row < 5:
                if row_diff == 1 and col_diff == 0:
                    return True
                else:
                    return False

            # did cross river
            else:
                # check if movement is only forward/left/right 1 space
                if row_diff == -1 and col_diff == 0:
                    return False

                else:
                    return True

        # check movement for Black Soldier
        if self._color == "black":
            # check if Soldier has crossed the river
            # didn't cross river
            if curr_row > 4:
                if row_diff == -1 and col_diff == 0:
                    return True
                else:
                    return False

            # did cross river
            else:
                # check if movement is only forward/left/right 1 space
                if row_diff == 1 and col_diff == 0:
                    return False

                else:
                    return True

    def possible_movements(self):
        """Returns the possible movements of the Soldier piece"""
        m1 = (1, 0)
        m2 = (-1, 0)
        m3 = (0, 1)
        m4 = (0, -1)
        moves_list = [m1, m2, m3, m4]
        return moves_list

    def get_all_possible_moves(self, curr_row, curr_col, board):
        """Returns all of the possible moves that the game piece can make while at the current position"""
        curr_space = board[curr_row][curr_col]
        all_possible_moves = []

        possible_moves = self.possible_movements()

        for move in possible_moves:
            new_row = move[0] + curr_row
            new_col = move[1] + curr_col

            if self.is_move_valid(curr_row, curr_col, new_row, new_col, board) is True:
                all_possible_moves.append((new_row, new_col))

        return all_possible_moves


### Created a game loop, where the players take turns and the game is played correctly until there's a winner :)

if __name__ == '__main__':

    my_game = XiangqiGame()
    while my_game.get_game_state() == "UNFINISHED":
        my_game.play_game()

    print("GAME HAS ENDED!")