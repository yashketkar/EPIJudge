from test_framework import generic_test


def levenshtein_distance(A, B):
    def compute(a, b):
        if a<0:
            return b+1
        if b<0:
            return a+1
        if grid[a][b] == -1:
            if A[a] == B[b]:
                grid[a][b] = compute(a-1,b-1)
            else:
                sub_d = compute(a-1,b-1)
                del_d = compute(a,b-1)
                add_d = compute(a-1,b)
                grid[a][b] = 1 + min(sub_d, del_d, add_d)
        return grid[a][b]
    grid = [[-1]*len(B) for _ in range(len(A))]
    return compute(len(A)-1, len(B)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
