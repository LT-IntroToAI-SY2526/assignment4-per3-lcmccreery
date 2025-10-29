
class TTTBoard:
    def __init__(self):
        """Initialize a 3x3 tic tac toe board as a flat list of 9 '*' characters."""
        self.board = ['*'] * 9

    def __str__(self):
        """Return a string representation of the board in a 3x3 grid format."""
        rows = []
        for i in range(0, 9, 3):
            rows.append(' '.join(self.board[i:i+3]))
        return '\n'.join(rows)

    def make_move(self, player, pos):
        """
        Place a move for player ('X' or 'O') in position pos (0–8).
        Return True if the move was made, False otherwise.
        """
        if player not in ['X', 'O']:
            return False
        if pos < 0 or pos >= 9:
            return False
        if self.board[pos] != '*':
            return False
        self.board[pos] = player
        return True

    def has_won(self, player):
        """Return True if the given player ('X' or 'O') has won."""
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in wins:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def game_over(self):
        """Return True if the game is over (win or full board)."""
        if self.has_won('X') or self.has_won('O'):
            return True
        if '*' not in self.board:
            return True
        return False

    def clear(self):
        """Reset the board to start a new game."""
        self.board = ['*'] * 9


# ---------------------------------------------------------
# Helper function to play the game interactively
# ---------------------------------------------------------
def play_tic_tac_toe():
    game = TTTBoard()
    current_player = 'X'
    while not game.game_over():
        print(game)
        try:
            pos = int(input(f"Player {current_player}, choose a position (0-8): "))
        except ValueError:
            print("Invalid input. Please enter a number 0-8.")
            continue

        if not game.make_move(current_player, pos):
            print("Invalid move, try again.")
            continue

        if game.has_won(current_player):
            print(game)
            print(f"Player {current_player} wins!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

    if not game.has_won('X') and not game.has_won('O'):
        print(game)
        print("It's a draw!")


# ---------------------------------------------------------
# Some asserts for basic testing
# ---------------------------------------------------------
if __name__ == "__main__":
    b = TTTBoard()

    # Test initialization
    assert b.board == ['*'] * 9

    # Test moves
    assert b.make_move('X', 0)
    assert not b.make_move('O', 0)  # spot already taken
    assert not b.make_move('O', 9)  # out of range
    assert not b.make_move('Z', 1)  # invalid player

    # Test winning rows
    b.clear()
    b.make_move('X', 0)
    b.make_move('X', 1)
    b.make_move('X', 2)
    assert b.has_won('X')
    assert not b.has_won('O')

    # Test columns
    b.clear()
    b.make_move('O', 0)
    b.make_move('O', 3)
    b.make_move('O', 6)
    assert b.has_won('O')

    # Test diagonal
    b.clear()
    b.make_move('X', 0)
    b.make_move('X', 4)
    b.make_move('X', 8)
    assert b.has_won('X')

    # Test game_over when board full
    b.clear()
    moves = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
    for i, p in enumerate(moves):
        b.make_move(p, i)
    assert b.game_over()

    print("All tests passed successfully!")
