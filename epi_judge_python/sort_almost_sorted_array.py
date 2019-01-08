from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence, k):
    my_heap = []
    count = 0
    while count <= k:
        x = next(sequence, None)
        if x is not None:
            heapq.heappush(my_heap, x)
        count += 1
    result = []
    while my_heap:
        result.append(heapq.heappop(my_heap))
        x = next(sequence, None)
        if x is not None:
            heapq.heappush(my_heap, x)        
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
