'''Q32 Write a Python program to remove duplicates from a list.'''

# Sample list with duplicates
numbers = [1, 2, 2, 3, 4, 4, 5, 1]

# Empty list to store unique elements
unique = []

# Loop through each item
for num in numbers:
    if num not in unique:
        unique.append(num)

# Print result
print("List without duplicates:", unique)
