# A. Union (|)
# Returns all unique(non dupliacte) elements from both sets.

s1={1,2,3,4,5,6}
s2={4,2,7,8}
print(f"Union: {s1.union(s2)}")
# or
print(s1 | s2)

# B. Intersection (&)
# Returns only common elements.
print(f"Intersection: {s1.intersection(s2)}")
# or
print(s1 & s2)

# C. Difference (-)
# Returns elements present in the first set but not in the second.
print(f"Difference of S1: {s1.difference(s2)}")   #elements of set A which is not in A
print(f"Difference of S2: {s2.difference(s1)}")   #elements of set B which is not in B

# D. Symmetric Difference (^)
# Returns elements present in either set, but not in both (not common elements)
print(f"Symmetric difference: {s1.symmetric_difference(s2)}")  

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {7, 8, 9}

# Check whether A is a subset of B
print(A.issubset(B))       # True

# Check whether B is a superset of A
print(B.issuperset(A))     # True

# Check whether A and C have no common elements
print(A.isdisjoint(C))    # True


A = {1, 2, 3}
B = {3, 4, 5}

# Update A with the union
A.update(B)

# Keep only common elements in A
A.intersection_update(B)

# Remove elements of B from A
A.difference_update(B)

# Keep elements that are in either set, but not both
A.symmetric_difference_update(B)

# Create a shallow copy
C = A.copy()

# Membership Operators
# Use in and not in to check whether an element exists
fruits={"apple","banana","cherry"}
print("apple" in fruits)
print("avacado" in fruits)

# Frozenset
# A frozenset is an immutable version of a set.
# - You cannot add or remove elements.
# - You can perform operations such as union and intersection.
# - It can be used as a dictionary key because it is immutable.

numbers= frozenset({20,40,60})
print(numbers)