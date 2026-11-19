# A list in Python is a changable collection used to store multiple values in a single variable

# 1. Important characteristics of lists
# Python lists have four important characteristics:
# 1. Ordered: Elements maintain their insertion order.
# 2. Mutable: We can modify the list after creating it.
# 3. Allows duplicates: Same values can appear multiple times.
# 4. Different data types: A list can contain strings, integers, floats, booleans, etc.


# 2. Indexing in Lists
# Indexing means accessing individual elements using their position.

# 3. Slicing in Lists
# Slicing means extracting a portion of a list.
# list[start : end : step]


# Smart Canteen Order Manager
orders= ["Burger", "Coffee","Tea", "Fries", "Coke","Momos"]
print("Current orders: ", orders)

#add new order at end
orders.append("Pizza")

#insert order at position 1
orders.insert(0,"Pasta")
print(f"Updated orders: {orders}")

#cancel particular order
orders.remove("Tea")
print(f"Updated orders after cancelling Tea : {orders}")


# Complete and remove the first order
completed = orders.pop(0)
print("Completed order:", completed)

# Display first and last orders
print("First order:", orders[0])
print("Last order:", orders[-1])

# Display orders from second position onwards
print("Pending orders:", orders[1:])

# Display all orders using a loop
print("\nAll pending orders:")
for index, order in enumerate(orders, start=1):
    print(f"{index}.{order}")

# Check whether an order exists
if "Pizza" in orders:
    print("Pizza order is pending")

orders.sort()
print("Alphabetical orders:", orders)



