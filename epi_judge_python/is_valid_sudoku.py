from test_framework import generic_test

def contains_duplicates(pa):
    no_zero = [y for y in pa if y != 0]
    if len(set(no_zero)) != len(no_zero):
        return True
    return False

# 36. https://leetcode.com/problems/valid-sudoku/
# 5.17
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    pa = partial_assignment
    for row in pa:
        if contains_duplicates(row):
            return False
    for i in range(len(pa[0])):
        col = [x[i] for x in pa]
        if contains_duplicates(col):
            return False
    for i in [0,3,6]:
        for j in [0,3,6]:
            sub = [pa[i+0][j+0], pa[i+0][j+1], pa[i+0][j+2], pa[i+1][j+0], pa[i+1][j+1], pa[i+1][j+2], pa[i+2][j+0], pa[i+2][j+1], pa[i+2][j+2]]
            if contains_duplicates(sub):
                return False    
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
