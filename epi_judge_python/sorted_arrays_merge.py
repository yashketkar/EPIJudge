from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    iterators = [ iter(x) for x in sorted_arrays ]
    my_heap = []
    for i, it in enumerate(iterators):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush( my_heap, (first_element, i) )
    result = []
    while my_heap:
        x, i = heapq.heappop( my_heap )
        result.append(x)
        it = iterators[i]
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush( my_heap, (first_element, i) )
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
