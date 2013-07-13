# http://projecteuler.net/problem=5

def is_prime(n):
    """Determine if n is prime."""
    for i in range(2, int(n ** 0.5) + 1):
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


def lcm(*nums):
    """Calculate the least common multiple."""
    lcmf = {}
    for n in nums:
        factors = factor(n)
        for f in factors:
            count = factors.count(f)
            if f not in lcmf or count > lcmf[f]:
                lcmf[f] = count
    ans = 1
    for k, v in lcmf.items():
        ans *= k ** v
    return ans


print(lcm(1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
