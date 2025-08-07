'''Q:44) Write a Python program to create a tuple with different data types. '''

# Create a tuple with different data types
my_tuple = ("Hello", 25, 3.14, True, [1, 2, 3], {'a': 10, 'b': 20}, (4, 5))

print("Tuple:", my_tuple)

# Print data types of each element
print("\n each element in the tuple:")
for item in my_tuple:
    print(item, "----→", type(item))

