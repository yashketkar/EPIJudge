from test_framework import generic_test


def search_smallest(A):
    l, r = 0, len(A)-1
    m = 0
    while l < r:
        m = (l+r)//2
        if A[m] < A[r]:
            r = m
        else:
            l = m + 1
    return l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
