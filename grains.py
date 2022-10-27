# def square(number):
#     if number > 64 or number < 1:
#         raise ValueError('square must be between 1 and 64')
#     elif number == 1:
#         return 1
#     elif number == 2:
#         return 2
#     else:
#         num_of_squares = list(range(3, number + 1))
#         grains_in_squares = [1, 2]
#         g_i_s_indx = 1
#         for square in num_of_squares:
#             grains_in_squares.append(grains_in_squares[g_i_s_indx]*2)
#             g_i_s_indx += 1
#         num_of_squares.insert(0, 1)
#         num_of_squares.insert(1, 2)
#         squares_and_grains = dict(zip(num_of_squares, grains_in_squares))
#         return squares_and_grains.get(number)


# def total():
#     chessboard = list(range(1, 65))
#     total_to_sum = []
#     for each_square in chessboard:
#         total_to_sum.append(square(each_square))
#     return sum(total_to_sum)


def square(number):
    if not 0 < number <= 64:
        raise ValueError('square must be between 1 and 64')

    return 2 ** (number - 1)


def total():
    return 2 ** 64 - 1
