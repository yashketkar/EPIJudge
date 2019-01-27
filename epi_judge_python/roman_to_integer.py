from test_framework import generic_test


# 6.8 Roman to Integer
def roman_to_integer(s):
    mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,
               'M':1000}
    total, i = 0, 0
    while i < len(s):
        if (i+1)<len(s) and mapping[s[i]] < mapping[s[i+1]]:
            total += mapping[s[i+1]]-mapping[s[i]]
            i += 1
        else:
            total += mapping[s[i]]
        i += 1
    return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
