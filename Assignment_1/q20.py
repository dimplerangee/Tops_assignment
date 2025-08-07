#q:20 Write a Python program to get a single string from two given strings, 
#separated by a space and swap the first two characters of each string.

string1 = input("enter string1:")
string2 = input("enter string1:")

new_str1 = string2[ :2] + string1[2:]
new_str2 = string1[ :2] + string2[2:]

result = new_str1 + " "+ new_str2
print("resultt:",result)