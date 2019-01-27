from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    def helper(i, j, k):
        if (i,j,k) in memo:
            return False
        if grid[i][j] == S[k]:
            if k == len(S) - 1:
                return True
            else:
                if i < rows - 1 and helper(i + 1, j, k + 1):
                    return True
                if j < cols - 1 and helper(i, j + 1, k + 1):
                    return True
                if i > 0 and helper(i - 1, j, k + 1):
                    return True
                if j > 0 and helper(i, j - 1, k + 1):
                    return True
        memo[(i,j,k)] = False
        return False
    rows = len(grid)
    cols = len(grid[0])
    memo = {}
    for i in range(rows):
        for j in range(cols):
            if helper(i, j, 0):
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
