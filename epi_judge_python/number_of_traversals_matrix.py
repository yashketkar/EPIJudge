from test_framework import generic_test


def number_of_ways(n, m):
    grid = [[1]*m] + [([1]+[0]*(m-1)) for _ in range(n-1)]
    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
