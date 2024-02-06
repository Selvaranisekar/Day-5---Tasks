# Using the python Lambda Function create a Fibonacci series from 1 to 50 elements'''
from functools import reduce

fib_series = lambda x: reduce(lambda x, _: x+[x[-1]+x[-2]], range(x-2), [0, 1])
print(fib_series(11))

#output --[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


