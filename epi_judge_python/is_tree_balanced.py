from test_framework import generic_test


# 9.1
# 110. https://leetcode.com/problems/balanced-binary-tree/
def is_balanced(node):
    if not node:
        return 0
    left_height = is_balanced(node.left)
    if left_height == -1:
        return -1
    right_height = is_balanced(node.right)
    if right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return (1 + max(left_height, right_height))


def is_balanced_binary_tree(tree):
    return is_balanced(tree) > -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
