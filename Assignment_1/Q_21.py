'''Q_21 Write a Python program to add 'in' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then 
add 'ly' instead if the string length of the given string is less than 3, 
leave it unchanged.'''

text = input("enter the text:")

if len(text) < 3:
    result = text

elif text.endswith("ing"):
    result = text + "ly"

else:
    result = text + "ing"

print("result:",result)