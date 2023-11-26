

ones = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

big = [
    'thousand',
    'million',
    'billion',
    'trillion',
    'quadrillion',
    'quintillion',
    'sextillion',
    'septillion',
    'octillion',
    'nonillion',
    'decillion'
]


def number_name(no: int):
    remainder = ''
    if no < 0:
        return f'minus {number_name(-no)}'
    elif no < 20:
        return ones[no]
    elif no < 100:
        if no % 10:
            remainder = f'-{ones[no % 10]}'
        return f'{tens[no // 10]}{remainder}'
    elif no < 1000:
        if no % 100:
            remainder = f' and {number_name(no % 100)}'
        return f'{ones[no // 100]} hundred{remainder}'
    else:
        for exponent, name in enumerate(big, start=1):
            if no < 1000 ** (exponent + 1):
                if no % (1000 ** exponent):
                    remainder = f', {number_name(no % (1000 ** exponent))}'
                return f'{number_name(no // (1000 ** exponent))} {name}{remainder}'
        else:
            raise NotImplementedError()


if __name__ == '__main__':
    total_chars = 0
    for i in range(1, 1_000_001):
        print(number_name(i))
