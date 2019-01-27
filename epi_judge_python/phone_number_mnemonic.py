from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    if not phone_number:
        return []
    keypad = { '0': '0', '*': '', '#': '', '1': '1', '2':['A', 'B', 'C'],
               '3':['D', 'E', 'F'], '4':['G', 'H', 'I'], '5':['J', 'K', 'L'],
               '6':['M', 'N', 'O'], '7':['P', 'Q', 'R', 'S'],
               '8':['T', 'U', 'V'], '9':['W', 'X', 'Y', 'Z']}
    current = list(keypad[phone_number[0]])
    for i in range(1, len(phone_number)):
        successor = []
        for s in current:
            for l in keypad[phone_number[i]]:
                successor.append(s+l)
        current = successor
    return current


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
