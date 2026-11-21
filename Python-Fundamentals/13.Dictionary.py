# A Dictionary in Python is a built-in collection data type used to store data in the form of
# key-value pairs.

# Unlike lists and tuples, which access elements using indexes,
# dictionaries access elements using unique keys.

# Important characteristics of dictionaries
# Ordered	Maintains insertion order (Python 3.7+)
# Mutable	We can modify after creation
# No duplicate keys	Every key must be unique
# Duplicate values allowed	Multiple keys can have the same value
# Key-value pairs	Every element contains a key and value
# Heterogeneous	Supports different data types
# Dynamic	Can grow or shrink at runtime


# SMART STUDENT PERFORMANCE MANAGEMENT SYSTEM
students={
    101:{"name":"Sakshi","marks":88,"city":"Pune"},
    102: {"name": "Rahul", "marks": 76, "city": "Mumbai"},
    103: {"name": "Neha", "marks": 95, "city": "Pune"},
    104: {"name": "Amit", "marks": 67, "city": "Nashik"},
    105: {"name": "Sneha", "marks": 88, "city": "Mumbai"}
}

# 1. Display all student records
print("\n--- ALL STUDENT RECORDS ---")
for roll, details in students.items():
    print(f"{roll}: {details}")


# 2. Access dictionary elements using get()
print("\n--- SEARCH STUDENT ---")
roll_no = 103
student= students.get(roll_no,"Student not found")
print("Student Detail:", student)

# 3. Display all keys and values
print("\n--- DICTIONARY KEYS ---")
print(students.keys())

print("\n--- DICTIONARY VALUES ---")
print(students.values())

# 4. Add a new student using assignment
students[102]={
    "name":"Yash",
    "marks": 67,
    "city" :"Benguluru"
}

# 5. Update existing student using update()
students[103].update({
    "marks": 97,
    "city": "Delhi"
})

print("\nAfter Adding and Updating:")
print(students)

# 6. Insert a default record using setdefault()
students.setdefault(104, {
    "name": "Riya",
    "marks": 91,
    "city": "Pune"
})

# 7. Calculate total and average marks
print("\n--- PERFORMANCE REPORT ---")

total_marks= sum(
    details["marks"] for details in students.values()
    )

total_students= len(students)

average= total_marks/total_students

print("Total Marks:", total_marks)
print("Total Students:", total_students)
print("Average Marks:", round(average, 2))


# 8. Find highest and lowest scoring students
highest= max(
    details["marks"] for details in students.values()
)


print("Highest Marks:", highest)

for stud_key, values in students.items():
    print(stud_key, values)
