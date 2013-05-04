def even_fibs(n):
    """All even fibs less than n."""
    fibs = []
    a, b = 1, 2
    while a < n:
        if a % 2 == 0:
            fibs.append(a)
        a, b = b, a + b
    return fibs


print(sum(even_fibs(4000000)))
