from test_framework import generic_test

# 66. https://leetcode.com/problems/plus-one/
# 5.2
def plus_one(A):
    A[-1]+=1
    for i in range(len(A)-1, 0, -1):
        if A[i] >= 10:
            A[i]-=10
            A[i-1]+=1
    if A[0]>= 10:
        A[0]-=10
        A = [1] + A
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
