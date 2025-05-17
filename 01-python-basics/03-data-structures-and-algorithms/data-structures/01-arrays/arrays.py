import array as arr

# Create an array
a = arr.array("i", [1, 2, 3, 4])

# iterating each element in the array
for i in range(0, len(a)):
    print(f"{i}: {a[i]}")

# Adding elements into the array
a.insert(4, 5)
a.insert(5, 6)
a.insert(6, 7)
a.insert(7, 8)

# After insertion
for i in range(0, len(a)):
    print(f"{i}: {a[i]}")

# Accessing array items
print(a[0])
print(a[2])
print(a[6])

# array slicing
print(f"Sliced array between indexes 3:8 {a[3:8]}")

print(f"Sliced array after index 5 {a[5:]}")

print(f"Sliced array from start to end {a[:]}")

# Searching Element in an Array
# index of 1st occurrence of 2
print(a.index(2))

# index of 1st occurrence of 1
print(a.index(1))

# Updating Elements in an Array
# update item at index 2
a[2] = 6
print(a)

# update item at index 4
a[4] = 8
print(a)
