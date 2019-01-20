from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    s = []
    def inorder(n):
        if n and len(s) < k:
            inorder(n.right)
            if len(s) < k:
                s.append(n.data)
                inorder(n.left)
    inorder(tree)
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
