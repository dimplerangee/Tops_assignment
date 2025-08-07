# using with temp variable change values
x = 13
y = 12
temp = x
print (" the value of temp varible is:",temp)
x = y
print(" the value of x is:",x)
y = temp
print("the value of y is:",y)


# using without temp varibable change values
x = 13
y = 12
x , y = y , x
print("the  value of x is :", x)
print("the  value of  y is:",y)
