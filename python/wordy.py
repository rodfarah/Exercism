def answer(question):
    question = question.replace('?', ' ?')
    question_list = question.rsplit()

    # Creating a only number list:
    num_list = [int(num)
                for num in question_list if num[0] == '-' or num.isdigit()]

    # Creating a only operator list:
    total_oper_list = ['plus', 'minus', 'multiplied', 'divided']
    question_opers = [
        oper for oper in question_list if oper in total_oper_list]

    # Checking Errors:
    if question_list[-1] != '?':
        raise ValueError('syntax error')
    elif len(num_list) == 0:
        if question_list[0] == 'What':
            raise ValueError('syntax error')
        elif question_list[0] != 'What':
            raise ValueError('unknown operation')
    elif len(num_list) - len(question_opers) != 1:
        raise ValueError('syntax error')
    elif 'cubed' in question_list:
        raise ValueError('unknown operation')
    idx = 0
    while idx < len(question_list) - 1:
        if question_list[idx].isdigit() and question_list[idx+1].isdigit():
            raise ValueError('syntax error')
        idx += 1

    # Merging numbers and operators in order of appearence:
    nums_and_ops = [None] * (len(num_list) + len(question_opers))
    nums_and_ops[::2] = num_list
    nums_and_ops[1::2] = question_opers

    # Checking one Special Condition and calculating the answer:
    if len(num_list) == 1:
        only_one = num_list.pop()
        return only_one
    else:
        indx = 0
        while len(nums_and_ops) != 1:
            if nums_and_ops[indx + 1] == 'plus':
                nums_and_ops.insert(
                    3, nums_and_ops[indx] + nums_and_ops[indx + 2])
                nums_and_ops.pop(0)
                nums_and_ops.pop(0)
                nums_and_ops.pop(0)
            elif nums_and_ops[indx + 1] == 'minus':
                nums_and_ops.insert(
                    3, nums_and_ops[indx] - nums_and_ops[indx + 2])
                nums_and_ops.pop(0)
                nums_and_ops.pop(0)
                nums_and_ops.pop(0)
            elif nums_and_ops[indx + 1] == 'multiplied':
                nums_and_ops.insert(
                    3, nums_and_ops[indx] * nums_and_ops[indx + 2])
                nums_and_ops.pop(0)
                nums_and_ops.pop(0)
                nums_and_ops.pop(0)
            elif nums_and_ops[indx + 1] == 'divided':
                nums_and_ops.insert(
                    3, nums_and_ops[indx] / nums_and_ops[indx + 2])
                nums_and_ops.pop(0)
                nums_and_ops.pop(0)
                nums_and_ops.pop(0)
        result = nums_and_ops.pop()
    return result
