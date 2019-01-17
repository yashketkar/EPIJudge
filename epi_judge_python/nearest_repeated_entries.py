import collections

from test_framework import generic_test


def find_nearest_repetition(paragraph):
    min_dist, idx_dict = float('inf'), {}
    for idx, word in enumerate(paragraph):
        if word not in idx_dict:
            idx_dict[word] = [idx]
        else:
            min_dist = idx - idx_dict[word][-1] if idx-idx_dict[word][-1] < min_dist else min_dist
            idx_dict[word].append(idx)
    return -1 if min_dist==float('inf') else min_dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
