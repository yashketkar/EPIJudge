from test_framework import generic_test

# https://leetcode.com/problems/symmetric-tree/
# 9.2
def is_mirror(a, b):
    if not a and not b:
        return True
    if (not a and b) or (not b and a) or (a.data != b.data):
        return False
    return is_mirror(a.left, b.right) and is_mirror(a.right, b.left)


def is_symmetric(tree):
    return not tree or is_mirror(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
