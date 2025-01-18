def saddle_points(matrix:list) -> list:
    """
    Given a list of lists that simulate a matrix, return a list 
    containing the index of the largest number in its row and the
    index of the smallest number in its column.
    """

    # return empty list if empty matrix
    if not matrix:
        return []

    num_of_columns = len(matrix[0])
    # check if lists inside matrix have the same length
    for lst in matrix:
        if len(lst) != num_of_columns:
            raise ValueError("irregular matrix")
        
    possible_by_row = [] # [row index, highest number in row, index of highest number in row]
    idx_a = 0
    for lst in matrix:
        # check for highest number in each row (list)
        highest_in_row = max(lst)
        idx_b = 0
        for num in lst:
            if num == highest_in_row:
                possible_by_row.append([matrix.index(lst, idx_a), num, lst.index(num,idx_b)])
            idx_b += 1
        idx_a += 1
    perfect_spot = []
    for possibility in possible_by_row:
        check = []
        for lst in matrix:
            if matrix.index(lst) != possibility[0]:
                check.append(lst[possibility[2]] >= possibility[1])
            continue
        if all(check):
            perfect_spot.append({"row":possibility[0]+1, "column":possibility[2]+1})
    return perfect_spot
