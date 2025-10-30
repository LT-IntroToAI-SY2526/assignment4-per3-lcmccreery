
class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self):
        """Initialize an empty 3x3 board"""
        self.board = ["*"] * 9

    def __str__(self):
        """Return a human-readable string of the board"""
        rows = []
        for i in range(0, 9, 3):
            rows.append(" ".join(self.board[i:i+3]))
        return "\n".join(rows)

    def make_move(self, player: str, pos: int) -> bool:
        """Place a move for `player` in position `pos`, if valid.

        Args:
            player: "X" or "O"
            pos: int position 0–8

        Returns:
            True if move successful, False otherwise
        """
        if player not in ["X", "O"]:
            return False
        if not isinstance(pos, int) or pos < 0 or pos >= 9:
            return False
        if self.board[pos] != "*":
            return False
        self.board[pos] = player
        return True

    def has_won(self, player: str) -> bool:
        """Check if given player has won"""
        b = self.board
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(b[i] == player for i in combo) for combo in win_conditions)

    def game_over(self) -> bool:
        """Return True if someone has won or board is full"""
        if self.has_won("X") or self.has_won("O"):
            return True
        if "*" not in self.board:
            return True
        return False

    def clear(self):
        """Reset the board"""
        self.board = ["*"] * 9


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise"""
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn
        else:
            print("Invalid move, try again.")

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print("Board full, cat's game!")


if __name__ == "__main__":
    # Tests
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    # Uncomment to play interactively
    play_tic_tac_toe()