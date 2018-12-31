from test_framework import generic_test


def binary_tree_depth_order(tree):
    if not tree:
        return []
    queue = [tree]
    all_levels = []
    while queue:
        current_level = []
        next_level = []
        while queue:
            x = queue.pop(0)
            current_level.append(x.data)
            if x.left:
                next_level.append(x.left)
            if x.right:
                next_level.append(x.right)
        all_levels.append(current_level)
        queue = next_level
    return all_levels


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
