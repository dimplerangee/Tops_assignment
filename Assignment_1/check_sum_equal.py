# cget  number from user
a = int(input("enter frist number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

# check if any two values are equal
if a == b or b == c or a == c:
    total = 0
else:
    total = a + b + c
# print the result
print("the result is:",total)