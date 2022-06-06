from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None # keep track of winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self):
        # return []
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

        # above for loop condensed below
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        # return len(self.available_moves()) #or we can count using the line below
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign sqwuare to letter
        # )
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind+3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind+1*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # but only if the square is an even number (0,2,4,6,8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all these fail no winner
        return False

def play(game, x_player, o_player, print_game = True):
    # return the winner of the game(or the letter) or Nne for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting the letter


    while game.empty_squares():
        # Get move from appropirate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print(' ') 

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # switches player

        # tiny break
        time.sleep(1.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

    # has a bug