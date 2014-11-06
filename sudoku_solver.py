from sys import argv

def csv_to_array(sudoku_file):
    """
    Translates csv file into an array
    """
    row = []
    sudoku_board = []
    for line in sudoku_file:
        for char in line:
            if char != ',' and char != '\n':
                row.append(int(char))
        sudoku_board.append(row)
        row = []
    return sudoku_board

def array_to_csv(sudoku_board):
    """
    Translates array into a csv file
    """
    line = ""
    for row in sudoku_board:
        for item in row:
            cell = str(item) + ","
            line += cell
        line += "\n"
    f =  open('solved_sudoku.csv', 'wb')
    f.write(str(line))
    f.close()
    
def duplicates_present(l):
    """
    Determines whether a list, l, contains any duplicates
    """
    unique_items = set(l)
    unique_items.discard(0)
    for i in unique_items:
        count = l.count(i)
        if count > 1:
            return True
    return False
    
def check_3x3_grid(x, y, board):
    """
    Given an (x,y) index of the upper left corner of the subboard, returns True if no duplicates are present
    """
    items = []
    for i in range(x, x+3):
        for j in range(y, y+3):
            items.append(board[j][i])
    return not duplicates_present(items)

def check_all_3x3_grids(board):
    """
    Given a 9x9 board, returns False if there are duplicates values in any of the 9 subboards
    """
    for i in range(0, len(board), 3):
        for j in range(0,len(board), 3):
            if check_3x3_grid(i, j, board) == False:
                return False
            return True
            
def check_9x9_rows(board):
    """
    Given a 9x9 board, returns False if there are duplicates values in any of 9 rows
    """
    for row in board:
        if duplicates_present(row):
            return False
    return True

def check_9x9_columns(board):
    """
    Given a 9x9 board, returns False if there are duplicates values in any of 9 columns
    """
    for j in range(len(board)):
        if duplicates_present(board[:][j]):
            return False
    return True

def get_valid_items(i, j, board):
    """
    Given a 9x9 board and the indices (i,j) of the upper left corner of a 3x3 subboard,
    returns two lists: a list of indices of the zeros in each subboard and a list of
    valid items not already present on the subboard
    """
    valid_items = range(1,10)
    zeros = []
    for x in range(i, i+3):
        for y in range(j, j+3):
            item = board[y][x]
            if item == 0 and not (y,x) in zeros:
                zeros.append((y,x))
            else:
                valid_items.remove(item)
    return zeros, valid_items

def solve_sudoku(board):
    """
    Given a 9x9 array of numbers 0-9 uses recursive implementation of dfs to test all possible
    combinations of boards. Prints the solved sudoku board to a solved_sudoku.csv
    """
    # check that the current board does not contain duplicates
    if (check_all_3x3_grids(board) and check_9x9_rows(board) and check_9x9_columns(board)):
        board_has_zeros = False
        # for each 3x3 subboard, get the index of its zeros and a list of valid values to try
        # in those empty spaces
        for i in range(0, len(board), 3):
            for j in range(0,len(board), 3):
                zeros, valid_items = get_valid_items(i,j, board)
                if not zeros == []:
                    board_has_zeros = True
                if (i == 6 and j == 6 and not board_has_zeros):
                    # if we've checked the last quadrant and the board has no zeros,
                    # we've found our solution and print to csv
                    array_to_csv(board)

                # try each valid item in the next remaining empty slot
                for v in valid_items:
                    board[zeros[0][0]][zeros[0][1]] = v
                    solve_sudoku(board)
                    board[zeros[0][0]][zeros[0][1]] = 0
                if board_has_zeros:
                    return board_has_zeros
  
  def main():
    sudoku_file  = open(argv[1], 'r+')
    sudoku_board = csv_to_array(sudoku_file)
    solution = solve_sudoku(sudoku_board)

if __name__ == "__main__":
    main()
