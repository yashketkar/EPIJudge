from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    i, j, write = m-1, n-1, m + n -1
    while i>=0 and j>=0:
        if A[i] > B[j]:
            A[write] = A[i]
            i -= 1
        else:
            A[write] = B[j]
            j -= 1
        write -= 1
    while j >= 0:
        A[write] = B[j]
        write -= 1
        j-=1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
