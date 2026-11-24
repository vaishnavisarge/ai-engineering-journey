# An important point: reduce() is not a built-in function directly available in Python. 
# You need to import it from the functools module.

# The reduce() function in Python is used to combine all elements of an iterable into a single value
# by repeatedly applying a function.

# For example:
# - Find the sum of all numbers.
# - Find the product of all numbers.
# - Find the maximum or minimum value.
# - Combine strings into one string.
# Unlike map() and filter(), reduce() keeps processing elements until it produces one final result.

# Syntax:
#     reduce(function, iterable, initializer)

from functools import reduce

numbers = [10, 20, 30, 40]

result = reduce(lambda x, y: x + y, numbers)

print(result)

from functools import reduce
num=[2,4,6,2]
def total(x,y):
    return x+y
print((reduce(total,num,0)))
    