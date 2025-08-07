'''Q:22 Write a Python function to reverses a string if its length is a multiple 
of 4.'''

text = input("Enter a string: ")

# Check if the length is a multiple of 4
if len(text) % 4 == 0:
    result = text[::-1]  # Reverse the string
else:
    result = text  # Leave it unchanged

# Print the result
print("Result:", result)