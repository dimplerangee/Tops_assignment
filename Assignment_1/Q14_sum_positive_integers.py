# 14) Write a python program to sum of the first n positive integers.
n = int(input("enter a positive number:"))

# initialize sum to 0
total = 0

#use a loop to add number from 1 to n 
for i in range(1,n + 1):
    total = total + i 

# display result
print("sum of first", n, "positive integer is:", total)15) Write a Python program to calculate the length of a string. 