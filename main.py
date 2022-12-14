from typing import List
import check_the_board


class GameBoard:
    def __init__(self) -> None:
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.free_fields = [str(i) + str(j) for i in range(3) for j in range(3)]

    def __str__(self) -> str:
        separator = "\n" + "-" * 9 + "\n"
        return f"{separator.join((' | '.join(line) for line in self.board))}\n\n" \
               f"Free fields -> {', '.join(self.free_fields)}"

    def set_the_mark(self, horizontal_position: str, vertical_position: str, mark: str) -> bool:
        POSITION_OF_FIELDS = {"0", "1", "2"}
        if horizontal_position in POSITION_OF_FIELDS and vertical_position in POSITION_OF_FIELDS:
            horizontal_position = int(horizontal_position)
            vertical_position = int(vertical_position)

        else:
            print("Wrong data! Re-enter the correct data.\n")
            return False

        if self.board[horizontal_position][vertical_position] != " ":
            print("This field is taken. Try again!\n")
            return False

        self.board[horizontal_position][vertical_position] = mark
        self.update_free_fields(horizontal_position, vertical_position)

        return True

    def update_free_fields(self, horizontal_position: int, vertical_position: int) -> None:
        try:
            self.free_fields.remove(str(horizontal_position) + str(vertical_position))
        except ValueError:
            print("The free fields are not synchronized with the board.")


def whose_turn(free_places: List[str]) -> str:
    return "O" if len(free_places) % 2 != 0 else "X"


def is_the_end_of_the_game(board: List[List[str]], mark: str) -> bool:
    board_lines = "".join("".join(line) for line in board)

    if check_the_board.check_horizontal_lines(board_lines) or \
            check_the_board.check_vertical_lines(board_lines) or \
            check_the_board.check_diagonal_lines(board_lines):
        print(f"Player with '{mark}' won!\n")
        return True

    if check_the_board.is_draw(board_lines):
        print("Draw!\n")
        return True

    return False


def game() -> None:

    print("Welcome to the tic-tac-toe game. Good luck!\n")
    game_board = GameBoard()

    while True:
        current_turn = whose_turn(game_board.free_fields)

        while True:
            print(game_board)
            print(f"Now the player with '{current_turn}' chooses the field\n")

            horizontal_position = input("Enter the horizontal position (0, 1 or 2) -> ")
            vertical_position = input("Enter the vertical position (0, 1 or 2) -> ")
            print()

            if game_board.set_the_mark(horizontal_position, vertical_position, current_turn):
                break

        if is_the_end_of_the_game(game_board.board, current_turn):
            print(game_board)

            play_again = input(
                "\nIf you want to play again, type 'y' or "
                "if you want to quit the game, type any character -> "
            )

            if play_again.lower() == "y":
                print("\nNew board!\n")
                game_board = GameBoard()

            else:
                print("Successful exit!")
                break


if __name__ == "__main__":
    game()
