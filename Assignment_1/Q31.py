''' Q-31 Write a Python program to count the number of strings where the string  
length is 2 or more and the first and last character are same from a given list 
of strings.''' 

# Sample list of strings
words = ['abc', 'xyz', 'aba', '1221', 'aa', 'a', 'x']

# Initialize counter
count = 0

# Loop through each word in the list
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

# Print the result
print("Number of matching strings:", count)
