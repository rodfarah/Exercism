def is_armstrong_number(number):
    num_to_string = str(number)
    num_of_digits = len(num_to_string)
    only_num = [int(num) for num in num_to_string]
    return number == sum([item ** num_of_digits for item in only_num])
