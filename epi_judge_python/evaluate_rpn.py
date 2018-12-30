from test_framework import generic_test


def calculate(a, b, o):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        return a // b
    else:
        print('error occured: {0} is not an operation'.format(o))
        return 0


def evaluate(expression):
    if not expression:
        return 0
    intermediate_results = []
    for x in expression.split(','):
        if x in '+-*/':
            b = intermediate_results.pop()
            a = intermediate_results.pop()
            intermediate_results.append(calculate(a, b, x))
        else:
            intermediate_results.append(int(x))
    return intermediate_results[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
