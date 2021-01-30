def kangaroo(x1, v1, x2, v2):
    while x1 <= x2:
        if x1 == x2:
            return 'YES'
        if v2 >= v1:
            return 'NO'
        x1 += v1
        x2 += v2

    return 'NO'

print(kangaroo(0, 3, 4, 2)) # YES
print(kangaroo(0, 2, 5, 3)) # NO