from test_framework import generic_test


def generate_pascal_triangle(n):
    if not n:
        return []
    if n == 1:
        return [[1]]
    result = [[1], [1,1]]
    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(result[i-1][j] + result[i-1][j-1])
        row.append(1)
        result.append(row)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
