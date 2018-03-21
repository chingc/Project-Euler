# http://projecteuler.net/problem=8

with open("problem_008.input", "r") as f:
    big_number_str = "".join(line.strip() for line in f.readlines())

fives = []
i = 0
while i + 5 <= len(big_number_str):
    fives.append(sorted(big_number_str[slice(i, i + 5)], reverse=True))
    i += 1

product = 1
for n in sorted(fives).pop():
    product *= int(n)

print(product)
