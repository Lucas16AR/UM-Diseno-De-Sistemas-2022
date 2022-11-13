def compare_two_numbers(a,b):
    if a > b:
        return a
    return b

def compare(a,b,c=None):
    bigger = b
    if a > b:
        bigger = a
    if c is not None and c > bigger:
        bigger = c
    print(f'el numero mas grande es {bigger}')

compare(a=3, b=40, c=5)