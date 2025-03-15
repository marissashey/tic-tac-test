import pytest

class TicTacToe:
    """
    attributes:
        move_log (dict): stores game moves.
            keys are strings "1" to "9" to represent board positions
            values are either "x", "o", or None (open spot) 

        token (str): either "x" or "o" to reflect whose turn it is
        game_over (bool): reflects whether game has ended
        outcome (dict): maps "x", "o", "tie" to all False initially, updated when game over
    """

    def __init__(self):
        self.move_log = {str(val): None for val in range(1,10)}
        self.token = "x"
        self.game_over = False
        self.outcome = {val: False for val in ("x", "o", "tie")}

        print(">welcome to a game of tic-tac-toe!")
        print(">when it's your turn, make a move by entering an int from 1 to 9.")

    def print_board(self):
        board_str = ""
        for i in range(1,10):
            if i in {1,4,7}: # row-starters 
                board_str += "\n|" 
            key_str = str(i)
            if self.move_log[key_str] is None:
                board_str += key_str # if spot is vacant, print spot number
            else:
                board_str += self.move_log[key_str] # else print contents
            board_str += "|"
        
        print(board_str)
        
    def update_turn(self):
        self.token = "o" if self.token == "x" else "x"
        return
    
    def make_player_move(self):
        """ make the player enter a valid move """
        while True:  # enforce retry if invalid input 
            print("\n")
            move_str = input(f">player {self.token}, your move:  ")
            
            if move_str in self.move_log.keys() and self.move_log[move_str] is None: # untaken int from 1 to 9 
                self.place_valid_move(move_str)
                break
            else:
                print("\n")
                print(">invalid move. please enter an untaken int from 1 to 9.")


    def place_valid_move(self, move_str):
        """ 
        a function that updates the move_log. 
        constraints to check for prior (so assumed to be true if entering this function)
            - move is an int from 1 to 9, inclusive 
            - that int corresponds to an open position in the move_log 
        """
        self.move_log[move_str] = self.token
        return
            
    def check_game_over(self):
        """ returns True if game is over after checking for a win or a tie. returns False if game isn't over yet """

        move_log = self.move_log

        win_combos = [
            [1,2,3],[4,5,6],[7,8,9],
            [1,4,7],[2,5,8],[3,6,9],
            [1,5,9],[3,5,7]
        ]
        
        for combo in win_combos: # check each win combo 
            pos_0, pos_1, pos_2 = str(combo[0]), str(combo[1]), str(combo[2])
            if move_log[pos_0] is not None and move_log[pos_0] == move_log[pos_1] == move_log[pos_2]:
                self.print_board()
                print(f">game over!\n>player {self.token} has won the game.")
                self.game_over=True
                self.outcome[self.token] = True
                return
            
        open_spot_not_found = True
        for value in move_log.values(): # check if board is full 
            if value is None:
                open_spot_not_found = False

        if open_spot_not_found: 
            self.print_board()
            print(">game over!\n>it's a tie.")
            self.game_over = True
            self.outcome["tie"] = True
            return 

        print(">continuing...")
        self.game_over = False
        return 


    def play(self):
        """ function to execute the gameflow in a sequential loop """

        while self.game_over is False:
            
            self.print_board()
            self.make_player_move()
            self.check_game_over()
            self.update_turn()


if __name__ == "__main__":
    bookend = "_____________________________________________________________________________________________________________________"
    print(bookend)
    game = TicTacToe()
    game.play()
    print(bookend)

