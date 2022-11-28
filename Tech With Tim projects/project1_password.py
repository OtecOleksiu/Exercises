import random
import string

digits = string.digits
letters_lower = string.ascii_lowercase
letters_upper = string.ascii_uppercase
spec_symbols = string.punctuation

lgc_dct = {
    1: digits,
    2: letters_lower,
    3: letters_upper,
    4: spec_symbols
}


def main():
    print(f'result:{logic()}')


def inpt():
    pass_len = input('enter password length: ')
    pass_symbols = input(
        'which symbols do you wanna use?\nDigits - 1\nLowercase letters - 2\nUppercase letters - 3\nSpecial symbols - 4\n').strip().replace(
        ',', '').replace(' ', '')
    if not pass_len.isdigit() or not pass_symbols.isdigit():
        print('only shown numbers allowed')
        main()
        quit()
    return pass_len, pass_symbols


def logic():
    x = inpt()
    result_lst = []
    tmp = ''
    try:
        for j in set(x[1]):
            tmp += f'{lgc_dct[int(j)]}'
    except Exception as _ex:
        tmp = ''
        print('enter valid numbers')
        main()
        quit()
    for i in range(int(x[0])):
        result_lst.append(random.choice(tmp))
    return ''.join(result_lst)


if __name__ == '__main__':
    main()
