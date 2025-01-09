def solve_n_queens(n):
    result = []  # To store all valid board configurations
    board = [["."] * n for _ in range(n)]  # Initialize an empty chessboard

    def is_safe(row, col):
        # Check column for any queen
        for i in range(row):
            if board[i][col] == "Q":
                return False
        
        # Check top-left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == "Q":
                return False
        
        # Check top-right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == "Q":
                return False
        
        return True

    def backtrack(row):
        # Base case: If all queens are placed, add the board to the result
        if row == n:
            result.append(["".join(r) for r in board])  # Convert rows to strings
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(row, col):  # Check if the position is safe
                board[row][col] = "Q"  # Place the queen
                backtrack(row + 1)  # Recurse to the next row
                board[row][col] = "."  # Backtrack: Remove the queen

    # Start backtracking from the first row
    backtrack(0)
    return result

print(solve_n_queens(4))
# Output: Solutions to 4-Queens problem
