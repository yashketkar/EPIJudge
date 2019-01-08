from test_framework import generic_test


def search_first_of_k(A, k):
    l, r, result = 0 , len(A)-1, -1
    while l<=r:
        mid = (l+r)//2
        if A[mid] > k:
            r = mid - 1
        elif A[mid] == k:
            result = mid
            r = mid - 1
        else:
            l = mid + 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
