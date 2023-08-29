def is_safe(board, row, col, N):
    # Check if the current position is safe for a queen
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check the lower diagonal on the left side
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solve_n_queens_util(board, col, N, solutions):
    # Base case: If all queens are placed, add the solution
    if col == N:
        solution = []
        for i in range(N):
            row = []
            for j in range(N):
                row.append(board[i][j])
            solution.append(row)
        solutions.append(solution)
        return

    # Try placing the queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen and recur for the next column
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, N, solutions)
            # Backtrack and remove the queen
            board[i][col] = 0

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)

    # print(solutions)
    if len(solutions) == 0:
        print("Not possible")
    else:
        for solution in solutions:
            for row in solution:
                for cell in row:
                    print("Q" if cell == 1 else ".", end=" ")
                print()
            print()

# Test the implementation
N = 4  # Change N to any desired value
solve_n_queens(N)
