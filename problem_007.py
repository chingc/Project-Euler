def is_prime(n):
    """Determine if n is prime."""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True


def nth_prime(n):
    """Determine the nth prime."""
    num = 1
    while n > 0:
        num += 1
        if is_prime(num):
            n -= 1
    return num


print(nth_prime(10001))
