def is_prime(n):
    """Determine if n is prime."""
    for i in range(2, n // 2 + 1):
        if n % i == 0: return False
    return True


def factor(n):
    """Prime factors of n."""
    factors = []
    i = 2
    while i <= n:
        q, r = divmod(n, i)
        if r == 0 and is_prime(i):
            factors.append(i)
            i, n = 2, q
        else:
            i += 1
    return factors


print(factor(600851475143)[-1])
