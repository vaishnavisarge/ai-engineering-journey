# Tuple are ordered collection of data, we cannot tuple once created 

# If we want to do modification tuple then first we need to convert tuple into list, set etc
# It is created using () brackets


# Empty tuple
t1 = ()

# Tuple containing integers
t2 = (10, 20, 30, 40)

# Tuple containing strings
t3 = ("Python", "Java", "JavaScript")

# Tuple containing different data types
t4 = ("Vaishnavi", 23, 8.99, True)

print(t2)
print(t4)

# Important: Even without parentheses, Python can create a tuple using comma-separated values.
data = 10, 20, 30
print(type(data))  # <class 'tuple'>

# Important characteristics of tuples:
# Ordered	Maintains insertion order
# Immutable	Cannot modify existing elements
# Allows duplicates	Same values can appear multiple times
# Different data types	Can store int, string, float, etc.
# Indexed	Supports positive and negative indexing
# Iterable	Can use loops to access elements

# Example 1: Student result management
# Store student details and marks in tuples. Calculate the total and average.
# will use nested tuple for storing marks

student=("Abhii", 101,(80,100,67,59,74,61))
name= student[0]
roll_no= student[1]
marks= student[2]
print(f"Student name: {name}")
print(f"Student roll no: {roll_no}")
print(f"Student marks: {marks}")

total= sum(marks)
print (f"Total: {total}")

average= total/len(marks)
print(f"Average marks: {average}")

print(f"Highest marks: {max(marks)}")

print(f"Lowest marks: {min(marks)}")


# Tuple packing and unpacking:-

# Tuple packing: Combining multiple values into a single tuple.
stud= "Sayali", 102, "C"
print("Packing tuple into single variable", stud)

# Tuple unpacking: Assigning tuple elements to separate variables.
stud= "Sayali", 102, "C"
stud_name, stud_roll, div=stud
print("Unpacking tuple into separate variable:")
print(f"{stud_name}\n{stud_roll}\n{div}")

# One important detail: A tuple is immutable, but if it contains a mutable object such as a 
# list, that inner list can still be modified.