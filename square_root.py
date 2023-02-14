def square_root(number):
    for num in range(number):
        if num * num == number:
            return num
        elif number == 1:
            return 1

print(square_root(22))