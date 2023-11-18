

ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
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

teens = {
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


def number_name(no):
    remainder = ''
    if no < 1:
        raise NotImplementedError()
    elif no < 10:
        return ones[no]
    elif no < 20:
        return teens[no]
    elif no < 100:
        if no % 10:
            remainder = '-' + number_name(no % 10)
        return tens[no // 10] + remainder
    elif no < 1_000:
        if no % 100:
            remainder = ' and ' + number_name(no % 100)
        return ones[no // 100] + ' hundred' + remainder
    elif no < 1_000_000:
        if no % 1000:
            remainder = ', ' + number_name(no % 1000)
        return number_name(no // 1000) + ' thousand' + remainder
    else:
        raise NotImplementedError()


if __name__ == '__main__':
    for i in range(1, 1_000_000):
        print(number_name(i))
