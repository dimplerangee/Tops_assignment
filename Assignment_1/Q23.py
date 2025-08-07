''' Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string.'''

text = input("enter string:")

if len(text) < 2:
    # result1 ="the string is eiter empty or lenght is not enough "
        result1 = [len(text)] +["is less than required"]
else:
    result1 = text[:2] + text[-2:]

print("result:",result1)