# Map, Filter, Reduce are built-in functions that allows to apply a function to 
# sequence of elements and return a new sequence

# Map():
# In simple words, instead of using a for loop to perform the same 
# operation on every element, you can use map().
# syntax :
#     map(function, iterable)
# There are two parameters:
# - function: The operation you want to perform on each element.
# - iterable: The collection whose elements you want to process.

def cube(x):
    return x*x*x
numbers=[1,2,3,4,5]
new_list=list(map(cube,numbers))
print(new_list)


def calculate_square(num):
    return num ** 2

numbers = [2, 3, 4, 5, 6]

result = map(calculate_square, numbers)

print(list(result))