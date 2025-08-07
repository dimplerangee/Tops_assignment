'''Q35 Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30. '''

# Generate list of squares from 1 to 30
squares = []

for i in range(1, 31):
    squares.append(i * i)

# Print first 5 elements
print("First 5 elements:", squares[:5])

# Print last 5 elements
print("Last 5 elements:", squares[-5:])
