from test_framework import generic_test

# 54. https://leetcode.com/problems/spiral-matrix/
# 5.18
def matrix_in_spiral_order(square_matrix):
    sm = square_matrix
    if not sm:
        return []
    result = []
    c = 0
    count = len(sm) * len(sm[0])
    i = 0
    while c < count:
        for j in range(i, len(sm[i])-i):
            result.append(sm[i][j])
            c += 1
        i += 1
        for j in range(i, len(sm)+1-i):
            result.append(sm[j][len(sm[0])-i])
            c += 1
        if c == count:
            break
        for j in range(len(sm[-i])-1-i, i-1, -1):
            result.append(sm[-i][j])
            c += 1
        for j in range(len(sm)-i, i-1, -1):
            result.append(sm[j][i-1])
            c += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
