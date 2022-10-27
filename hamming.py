def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')

    num_of_letters = len(strand_a)
    indx = 0
    different_letters = []
    while indx <= num_of_letters - 1:
        if strand_a[indx] != strand_b[indx]:
            different_letters.append(strand_a[indx])
        indx += 1

    return len(different_letters)
