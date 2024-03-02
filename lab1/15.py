def listOperations(ls):
    return [min(ls), max(ls), sum(ls), [i * i for i in ls]]


print(listOperations([5, 4, 3, 2, 1]))
