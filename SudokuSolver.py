# -------------------
#
#   Date : 2025-01-09
#   Auteur : Lodjo28
#   Nom du fichier : main
#   Version : 0.1
#
# -------------------

sudoku = [
    [8, 4, 7, 2, 9, 3, 1, 0, 0],
    [1, 2, 5, 6, 8, 7, 3, 4, 9],
    [3, 9, 6, 5, 1, 4, 8, 0, 0],
    [5, 8, 4, 7, 2, 6, 0, 0, 1],
    [6, 1, 2, 9, 3, 5, 7, 8, 4],
    [7, 3, 9, 1, 4, 8, 0, 6, 0],
    [2, 0, 1, 0, 0, 9, 4, 0, 8],
    [4, 0, 3, 8, 0, 1, 0, 0, 0],
    [9, 0, 8, 4, 6, 2, 0, 1, 0]
]

def print_sudoku(sudoku):
    count_row = 0
    for row in sudoku:
        if count_row % 3 == 0:
            print("---------------------")

        count_col = 0
        for num in row:
            if count_col % 3 == 0 and count_col != 0:
                print("|", end=" ")
            if num == 0:
                print("_", end=" ")
            else:
                print(num, end=" ")
            count_col += 1
        
        count_row += 1
        print()
    print("---------------------")

def check(sudoku, row, col, num):

    sud = [row[:] for row in sudoku]
    
    if num in sud[row]:
        return False

    for i in range(9):
        if sud[i][col] == num:
            return False
    
    row = row // 3
    col = col // 3

    count = 0
    for i in range(9):
        if i < row * 3 or i >= (row + 1) * 3:
            sud.pop(i - count)
            count += 1
    
    count = 0
    for i in range(9):
        if i < col * 3 or i >= (col + 1) * 3:
            for j in range(len(sud)):
                sud[j].pop(i - count)
            count += 1

    for i in sud:
        for j in i:
            if num == j:
                return False

    return True

def recSolver(sudoku, Liste_cases):

    if not Liste_cases:
        return sudoku

    row, col = Liste_cases[0]

    for num in range(1, 10):
        if check(sudoku, row, col, num):
            sudoku[row][col] = num

            result = recSolver(sudoku, Liste_cases[1:])
            if result:
                return result

            sudoku[row][col] = 0

    return False
            

def solver(sudoku):

    Liste_case_vide = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                Liste_case_vide.append((i, j))
    
    return recSolver(sudoku, Liste_case_vide)

print_sudoku(sudoku)

print()
print()

print_sudoku(solver(sudoku))
