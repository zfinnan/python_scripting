def multiply_by_two(num):
    return num * 2

with open('prime_numbers.txt') as prime_numbers_file:
    prime_numbers = prime_numbers_file.readlines()
    for num in prime_numbers:
        print(multiply_by_two(int(num)))

with open('one_to_hundred.txt') as numbers_file:
    list_of_numbers = numbers_file.readlines()
    result = []

    for num_txt in list_of_numbers:
        if 'Five' in num_txt:
            remove_newline_txt = num_txt[:-1]
            result.append(remove_newline_txt)
        elif 'Fifteen' in num_txt:
            remove_newline_txt = num_txt[:-1]
            result.append(remove_newline_txt)
    print(result)
