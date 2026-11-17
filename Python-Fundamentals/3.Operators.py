
# Python Operators - Combined Practice Program

a = 15
b = 4

# 1. Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# 2. Comparison Operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Less:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

# 3. Logical Operators
x = 20
y = 30

print("AND:", x > 10 and y > 20)
print("OR:", x > 25 or y > 20)
print("NOT:", not(x > 10))

# 4. Assignment Operators
num = 10

num += 5
print("After +=:", num)

num -= 3
print("After -=:", num)

num *= 2
print("After *=:", num)

num //= 4
print("After //=:", num)

num %= 3
print("After %=:", num)

num **= 2
print("After **=:", num)

# 5. Membership Operators
numbers = [10, 20, 30, 40, 50]

print("20 in list:", 20 in numbers)
print("60 not in list:", 60 not in numbers)

# 6. Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 == list3:", list1 == list3)
print("list1 is not list3:", list1 is not list3)



# 7. Ternary Operator
age = 22

result = "Eligible" if age >= 18 else "Not Eligible"
print("Voting Status:", result)

# 8. Operator Precedence
result = 10 + 5 * 2 ** 2
print("Precedence Result:", result)
