'''Q-57) Write a Python program to find the highest 3 values in a dictionary '''

d = {'a': 100, 'b': 300, 'c': 250, 'd': 400, 'e': 50}

v = list(d.values())       # get all values
v.sort(reverse=True)       # sort values in descending order

print(v[0])   
print(v[1])  
print(v[2])  

