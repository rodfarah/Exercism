def proverb(*input_data, qualifier=None):
    '''Given a list of inputs, generate the relevant proverb.'''
    if len(input_data) == 0:
        return []
    elif qualifier == None:
        qualifier = input_data[0]
    idx = 0
    result = []
    while idx <= len(input_data) - 2:
        result.append(
            f"For want of a {input_data[idx]} the {input_data[idx+1]} was lost.")
        idx += 1
    if qualifier in input_data:
        result.append(f"And all for the want of a {qualifier}.")
    else:
        result.append(
            f'And all for the want of a {qualifier} {input_data[0]}.')
    return result


print(proverb('Scisors', 'Paper'))
