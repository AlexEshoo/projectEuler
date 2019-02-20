import re

ROMAN_NUMERAL_REGEX = r"(M*)(CM)?(D|CD)?(C*)(XC)?(L|XL)?(X*)(IX)?(V|IV)?(I*)"
ROMAN_NUMERAL_PATTERN = re.compile(ROMAN_NUMERAL_REGEX)

NUMERAL_VALUE = {'M':  1000,
                 'CM': 900,
                 'D':  500,
                 'CD': 400,
                 'C':  100,
                 'XC': 90,
                 'L':  50,
                 'XL': 40,
                 'X':  10,
                 'IX': 9,
                 'V':  5,
                 'IV': 4,
                 'I':  1}


def construct_roman_numeral(n):
    numeral = ""
    rem = n
    for num, val in NUMERAL_VALUE.items():
        q, rem = divmod(rem, val)
        numeral += num * q

    return numeral


def read_roman_numeral(numeral):
    value = 0

    match = re.match(ROMAN_NUMERAL_PATTERN, numeral)
    for group in match.groups():
        if group:
            if is_homogeneous(group):
                value += NUMERAL_VALUE[group[0]] * len(group)
            else:
                value += NUMERAL_VALUE[group]

    return int(value)


def is_homogeneous(s):
    if s == len(s) * s[0]:
        return True

    return False


if __name__ == '__main__':

    savings = 0

    with open("resources/p089_roman.txt", 'r') as f:
        for line in f:
            num_string = line.strip()
            numeral_value = read_roman_numeral(num_string)
            compact = construct_roman_numeral(numeral_value)
            diff = len(num_string) - len(compact)
            savings += diff

            print(num_string, numeral_value, compact, diff)

    print(savings)
