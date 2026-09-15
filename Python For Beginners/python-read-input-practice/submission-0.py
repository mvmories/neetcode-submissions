def add_two_numbers() -> int:
    line = input()
    list_of_strings = line.split(",")
    sum = 0

    for element in list_of_strings:
        sum += int(element)
    return sum 



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
