def numbers(list_of_items):
    list_of_numbers = []

    #create a list of only numbers
    for item in list_of_items:
        if isinstance(item, int):
            list_of_numbers.append(item)
    print(list_of_numbers)

    #find bigger number
def get_max(list_of_numbers):
    bigger_number = max(list_of_numbers)
    print(bigger_number)

def main(list_of_items):
    #get list of only numbers
    list_of_numbers = numbers(list_of_items)
    #get bigger number
    bigger_number = get_max(list_of_numbers)
    print(bigger_number)

numbers([1, 4, 7, 3, 2])