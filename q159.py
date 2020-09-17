l = [1, 2, 3, 4, 5]

def doubleIt(x):
    return 2 * x
l1 = list(map(doubleIt, l))
=print(l1)  # [2, 4, 6, 8, 10]