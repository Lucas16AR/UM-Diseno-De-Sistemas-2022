def numbers(list_of_items):
    list_of_numbers = []

    #create a list of only numbers
    for item in list_of_items:
        if isinstance(item, int):
            list_of_numbers.append(item)
    print(list_of_numbers)

    #find bigger number
    bigger_number = max(list_of_numbers)
    print(bigger_number)

numbers([1, 4, 7, 3, 2])