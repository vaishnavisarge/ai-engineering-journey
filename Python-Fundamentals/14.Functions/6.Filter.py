# It filters a sequence of elements based on given predicate( a function that returns a boolen 
# value) and returns new squence containing elements that meet the predicate

# syntax:
#     filter(function, iterable)
# function: A condition that returns True or False.
# iterable: The list or collection you want to filter.

list_num=[22,10,3,5,4]

def check_num(x):
    return x>5

print(list(filter(check_num,list_num)))


