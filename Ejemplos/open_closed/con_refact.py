def compare_two_numbers(a,b):
    if a > b:
        return a
    return b

def compare_two_or_three_numbers(a,b,c=None):
    bigger = b
    if a > b:
        bigger = a
    if c is not None and c > bigger:
        bigger = c

def compare_three_numbers(a, b, c):
    more_bigger = compare_two_numbers(compare_two_numbers(a,b), c)
    print(f'number is {more_bigger}')

compare_three_numbers(a=3, b=40, c=5)