import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    size = int(size)
    if size < len(s):
        s = s[0:size]
    i = 0
    while i < len(s):
        if s[i] == 'b':
            del s[i]
            i-=1
        if s[i] == 'a':
            s[i] = 'd'
            s.insert(i, 'd')
            i+=1
        i+=1
    return len(s)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    # replace_and_remove(24, ["b", "d", "c", "a", "b", "a", "d", "b", "d", "b", "b", "a", "d", "c", "c", "a", "d", "a", "d", "d", "d", "b", "c", "c", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
