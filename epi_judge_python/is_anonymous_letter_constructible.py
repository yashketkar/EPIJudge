import collections
from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    ld = collections.Counter(letter_text)
    md = collections.Counter(magazine_text)
    
    for k, v in ld.items():
        if k in md:
            if (md[k] - v) < 0:
                return False
        else:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
