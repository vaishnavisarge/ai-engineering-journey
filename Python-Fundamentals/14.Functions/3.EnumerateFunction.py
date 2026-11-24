
# It is a built-in function in python that allows you to loop over a sequence (such as list,
# tuple,or string) and get the index and values of each elements in sequence at same time

marks=[12,56,32,98,13]
for index, mark in enumerate(marks):
    print(mark)
    if(index==0):
        print("Great!")