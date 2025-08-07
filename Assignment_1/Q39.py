'''Q:39) Write a Python program to find the second smallest number in a list.''' 

numbers = [12, 4, 5, 1, 9, 2]

unique_numbers = list(set(numbers))

unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second smallest number is:", unique_numbers[1])
else:
    print("There is no second smallest number.")
