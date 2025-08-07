# question16 Write a Python program to count the number of characters
#(character frequency) in a string

# Get input from user
input_string = input("Enter a string: ")

# Create an empty dictionary to store character counts
char_count = {}

# Loop through each character in the string
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Print the character frequencies
print("\nCharacter Frequency:")
for char in char_count:
    print(f"'{char}': {char_count[char]}")
