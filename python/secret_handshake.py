def commands(binary_str):
    '''
    00001 = wink
    00010 = double blink
    00100 = close your eyes
    01000 = jump
    10000 = Reverse the order of the operations in the secret handshake.
    '''

    int_list = [int(character) for character in binary_str]

    result_list = []

    for code in range(int_list[-1]):
        result_list.append('wink')
    for code in range(int_list[-2]):
        result_list.append('double blink')
    for code in range(int_list[-3]):
        result_list.append('close your eyes')
    for code in range(int_list[-4]):
        result_list.append('jump')
    if int_list[-5] == 1:
        result_list.reverse()
    return result_list


print(commands("12043"))
