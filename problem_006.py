def sum_of_squares(*nums):
    return sum(n * n for n in nums)


def square_of_sums(*nums):
    return sum(nums) ** 2


r = range(1, 101)
print(square_of_sums(*r) - sum_of_squares(*r))
