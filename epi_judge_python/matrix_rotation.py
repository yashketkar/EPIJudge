from test_framework import generic_test


def rotate_matrix(square_matrix):
    n = len(square_matrix)
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = square_matrix[i][j]
            square_matrix[i][j] = square_matrix[n-j-1][i]
            square_matrix[n-j-1][i] = square_matrix[n-i-1][n-j-1]
            square_matrix[n-i-1][n-j-1] = square_matrix[j][n-i-1]
            square_matrix[j][n-i-1] = temp
    return square_matrix


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
