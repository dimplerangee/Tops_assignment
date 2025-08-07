#user input
num = int(input("enter a number:"))

#cheak if number is not possible for negative number

if num < 0:
    print("factorial is not possible for negative number.")
elif num == 0:
    print("the factorial of 0 is 1.")

#if number is positive , find factorial using loop

else:
    fact = 1
    # start with  1
    for i in range(1,num+1):
        # loop from 1 to num
        fact = fact * i
    print(f" The factorial of {num} is {fact}.")
