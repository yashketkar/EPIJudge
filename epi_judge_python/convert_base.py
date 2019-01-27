from test_framework import generic_test
import string


def convert_base(num_as_string, b1, b2):
    decimal = 0
    is_negative = False
    if num_as_string[0] == '-':
        num_as_string, is_negative = num_as_string[1:], True
    for c in num_as_string:
        decimal = decimal * b1 + string.hexdigits.index(c.lower())
    result = ''
    while decimal > 0:
        val = string.hexdigits[decimal % b2].upper()
        result = val + result
        decimal //= b2
    return ('-' if is_negative else '') + (result if result else '0')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
