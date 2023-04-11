def factors(value: int) -> list[int]:
    """Compute the prime factors of a given natural number."""
    result = []
    num = 2
    base_num = value
    while num <= base_num:
        while base_num % num == 0:
            base_num = base_num / num
            result.append(num)
        num += 1
    return result
