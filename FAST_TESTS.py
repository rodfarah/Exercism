l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c']

result = [None]*(len(l1)+len(l2))
result[::2] = l1
result[1::2] = l2

print(result)