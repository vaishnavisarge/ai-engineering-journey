# A set in Python is an unordered collection of unique elements. 
# It is used to store multiple values in a single variable without allowing duplicates.

# Important characteristics of Sets
# 1. Unordered: Elements do not maintain a fixed insertion order.
# 2. Mutable: We can add or remove elements after creating a set.
# 3. No duplicates: Duplicate values are automatically removed.
# 4. Heterogeneous: Can store different data types.
# 5. Unindexed: We cannot access elements using indexes.
# 6. Unchangeable elements: A set cannot contain mutable elements like lists or dictionaries. 
# It can contain immutable values such as strings, integers, and tuples.

# Set is created using {} brackets

numbers= {100, 45,24,89,43,29,30}
print(f"Set {numbers}")

#Duplicate values are automatically removed
numbers= {100, 45,24,89,43,29,30,45,89}
print(f"Set {numbers}")

# Creating an empty set
empty_set = set()

# This creates an empty dictionary, NOT a set
empty_dict = {}

# Remember: Use set() to create an empty set. {} creates an empty dictionary.

languages = {"Python", "Java"}

# Add one element
languages.add("JavaScript")
print(languages)

# Add multiple elements
languages.update(["C", "C++", "React"])
print(languages)

numbers = {10, 20, 30, 40}

numbers.remove(20)
print(numbers)

numbers.discard(50)  # No error

removed = numbers.pop()
print("Removed element:", removed) #pop removed the last element

numbers.clear()
print(numbers)

numbers = {10, 20, 30}

numbers.remove(50)   # KeyError
numbers.discard(50)  # No error


