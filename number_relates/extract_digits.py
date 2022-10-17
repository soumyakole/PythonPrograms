""""It works only for integers"""


def extract_digits(num):
    remaining_number = num
    while remaining_number > 0:
        remaining_number, digit = divmod(remaining_number, 10)
        print(digit, end=' ')
    print()


""""It works for non-integers also"""
def extract_digit_alternate(num):
    for n in str(num)[::-1]:
        if n != '.':
            print(n, end=' ')
    print()


extract_digits(12315)
extract_digit_alternate(12315.9)