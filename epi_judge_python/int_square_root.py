from test_framework import generic_test


def square_root(k):
    if not k:
        return 0
    l, r = 0, k
    while l <= r:
        m = (l+r)//2
        if m**2 <= k:
            l = m + 1
        else:
            r = m - 1
    return l-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
