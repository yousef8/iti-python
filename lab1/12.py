def squareOdds(ls):
    return [n * n for n in ls if isinstance(n, int) and n % 2 != 0]


#                 1  _   9  _  25  _    _      _  49
print(squareOdds([1, 2, 3, 4, 5, 6, "yousef", 3.4, 7]))
