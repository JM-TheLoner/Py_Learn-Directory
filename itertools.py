import itertools

nums = list(itertools.accumulate(range(8)))
print(nums)
print(list(itertools.takewhile(lambda x: x <= 2, nums)))

a = ("a", "B")
b = ("S", "R")
print(list(itertools.product(a, b)))