from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 9.11
def helper(preorder, inorder, dic, pi, pj, ii, ij):
    if pj <= pi or ij <= ii:
        return None
    i = dic[preorder[pi]]
    left_size = i - ii
    root = BinaryTreeNode(preorder[pi])
    root.left = helper(preorder, inorder, dic, pi+1, pi+1+left_size, ii, i)
    root.right = helper(preorder, inorder, dic, pi+1+left_size, pj, i+1, ij)
    return root


def binary_tree_from_preorder_inorder(preorder, inorder):
    dic = {data:i for i, data in enumerate(inorder)}
    root = helper(preorder, inorder, dic, 0, len(preorder), 0, len(inorder))
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
