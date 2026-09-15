def add_two_numbers() -> int:
    line = input()
    list_of_strings = line.split(",")
    
    num1 = int(list_of_strings[0])
    num2 = int(list_of_strings[1])

    return num1 + num2


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
