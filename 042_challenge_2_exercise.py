# Video alternative: https://vimeo.com/954334009/67af9910fc#t=1054

# ✅ CHALLENGE: Improving the Tic Tac Toe Game

# So far, you’ve spent a lot of time writing new programs — which is great for
# learning. But in reality, most developers spend time improving or fixing
# existing programs.

# In this challenge, you’ll improve the existing tic tac toe game.

# TASKS:
# 1. Prevent players from placing a tile over another player’s tile ❌
# 2. Make the game end in a draw if no more free spaces are left 🔚
# 3. (Optional) Make a 5x5 board 🧩
# 4. (Optional) Make board size dynamic using a board_size parameter 🧠

# For now, we’ll do tasks 1 and 2.

# ✅ TIC TAC TOE GAME

def play_game():
  board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
  ]
  player = "X"

  while not is_game_over(board) and not is_board_full(board):
    print(print_board(board))
    print(f"It's {player}'s turn.")

    # Keep asking until the move is valid
    valid_move = False
    while not valid_move:
      row = int(input("Enter a row (0 to 2): "))
      column = int(input("Enter a column (0 to 2): "))

      if board[row][column] == ".":
        valid_move = True
      else:
        print("That space is taken. Please try again.")

    board = make_move(board, row, column, player)

    # Switch player
    player = "O" if player == "X" else "X"

  print(print_board(board))
  if is_game_over(board):
    print(f"Game over! Player {'O' if player == 'X' else 'X'} wins!")
  else:
    print("It's a draw!")


def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  return "\n".join(formatted_rows)


def make_move(board, row, column, player):
  board[row][column] = player
  return board


def get_cells(board, coord_1, coord_2, coord_3):
  return [
    board[coord_1[0]][coord_1[1]],
    board[coord_2[0]][coord_2[1]],
    board[coord_3[0]][coord_3[1]]
  ]


def is_group_complete(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return "." not in cells


def are_all_cells_the_same(board, coord_1, coord_2, coord_3):
  cells = get_cells(board, coord_1, coord_2, coord_3)
  return cells[0] == cells[1] and cells[1] == cells[2]


groups_to_check = [
  # Rows
  [(0, 0), (0, 1), (0, 2)],
  [(1, 0), (1, 1), (1, 2)],
  [(2, 0), (2, 1), (2, 2)],
  # Columns
  [(0, 0), (1, 0), (2, 0)],
  [(0, 1), (1, 1), (2, 1)],
  [(0, 2), (1, 2), (2, 2)],
  # Diagonals
  [(0, 0), (1, 1), (2, 2)],
  [(0, 2), (1, 1), (2, 0)]
]


def is_game_over(board):
  for group in groups_to_check:
    if is_group_complete(board, group[0], group[1], group[2]):
      if are_all_cells_the_same(board, group[0], group[1], group[2]):
        return True
  return False


def is_board_full(board):
  for row in board:
    if "." in row:
      return False
  return True


# ✅ LET'S PLAY
print("Game time!")
play_game()
