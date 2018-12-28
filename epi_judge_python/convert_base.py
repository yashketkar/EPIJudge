from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    hex_mapping = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                   'C': 12, 'D': 13, 'E': 14, 'F': 15}
    inv_map = {v: k for k, v in hex_mapping.items()}
    decimal = 0
    is_negative = False
    if num_as_string[0] == '-':
        num_as_string, is_negative = num_as_string[1:], True
    for c in num_as_string:
        decimal = decimal*b1 + hex_mapping[c]
    if not decimal:
        return '-0' if is_negative else '0'
    power = 1
    value = 1
    powers = []
    while value <= decimal:
        powers.append(value)
        value = b2**power
        power += 1
    new_base = []
    while powers:
        new_base.append(inv_map[decimal//powers[-1]])
        decimal = decimal % powers.pop()
    result = ''.join(str(x) for x in new_base)
    return '-'+result if is_negative else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
