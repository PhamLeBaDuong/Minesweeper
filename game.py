import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def initialize_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]

    # Place mines randomly
    mine_positions = random.sample(range(rows * cols), mines)
    for position in mine_positions:
        row = position // cols
        col = position % cols
        board[row][col] = '*'

    return board

def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
            if board[i][j] == '*':
                count += 1
    return count

def reveal(board, revealed, row, col):
    if revealed[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == ' ':
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
                reveal(board, revealed, i, j)

def minesweeper(rows, cols, mines):
    board = initialize_board(rows, cols, mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]

    while True:
        print_board(revealed)

        row = int(input("Enter row: "))
        col = int(input("Enter column: "))

        if not (0 <= row < rows and 0 <= col < cols):
            print("Invalid input. Please enter valid row and column.")
            continue

        if board[row][col] == '*':
            print_board(board)
            print("Game Over! You hit a mine.")
            break
        else:
            num_adjacent_mines = count_adjacent_mines(board, row, col)
            board[row][col] = str(num_adjacent_mines) if num_adjacent_mines > 0 else ' '
            reveal(board, revealed, row, col)

            if all(all(revealed[i][j] or board[i][j] == ' ' for j in range(cols)) for i in range(rows)):
                print_board(board)
                print("Congratulations! You win!")
                break

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    mines = int(input("Enter number of mines: "))

    minesweeper(rows, cols, mines)