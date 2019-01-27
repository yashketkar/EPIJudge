from test_framework import generic_test
import string


def is_palindrome(s):
    i,j = 0, len(s)-1
    punctuation = set(string.punctuation)
    punctuation.add(' ')
    while i<j:
        while s[i] in punctuation:
            i+=1
        while s[j] in punctuation:
            j-=1
        if s[i].lower() == s[j].lower():
            i+=1
            j-=1
        else:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
