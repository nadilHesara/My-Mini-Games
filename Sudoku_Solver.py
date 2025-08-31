def find_next_empty_cell(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    
    return None, None  # puzzle is fully filled

def is_valid_number(puzzle, guess, row, col):
    #checking in the horizontal and the vertical lines
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    for i in range(9):
        if puzzle[i][col] == guess:
            return False
    
    #checking in the 3x3 square
    row_start_idx = (row//3)*3
    col_start_idx = (col//3)*3

    for r in range(row_start_idx, row_start_idx+3):
        for c in range(col_start_idx, col_start_idx+3):
            if puzzle[r][c] == guess:
                return False
    

    return True
    


def solve_sudoku(puzzle):
    row, col = find_next_empty_cell(puzzle)

    if row == None:
        return True     #Finished solving
    
    for guess in range(1,10):
        if is_valid_number(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True


    
