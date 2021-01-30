# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    '''
    n : the number of prisoners
    m : the number of sweets
    s : the seat number that started to give sweets
    '''

    result = ((m - abs(n - s + 1)) % n)
    if result == 0:
        result = n
        
    return result

print(saveThePrisoner(5, 2, 1))
print(saveThePrisoner(5, 2, 2))
print(saveThePrisoner(7, 19, 2))
print(saveThePrisoner(3, 7, 3))
print(saveThePrisoner(3, 394274638, 3))
print(saveThePrisoner(654809340, 204894365, 472730208))
