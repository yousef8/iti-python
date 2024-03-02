def squareList(*args):
    return [i * i for i in args if isinstance(i, int)]


print(squareList("ahmed", 2, 3))
