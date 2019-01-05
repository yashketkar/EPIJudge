import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# 9.4
def lca(node0, node1):
    first = node0
    height_of_first = 0
    while first:
        height_of_first += 1
        first = first.parent
    second = node1
    height_of_second = 0
    while second:
        height_of_second += 1
        second = second.parent
    deeper, other = (node0,node1) if height_of_first>height_of_second else (node1,node0)
    for _ in range(abs(height_of_first-height_of_second)):
        deeper = deeper.parent
    while deeper != other:
        deeper = deeper.parent
        other = other.parent
    return deeper


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
