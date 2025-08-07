'''Q-54) Write a Python program to check multiple keys exists in a dictionary '''



dic = {"name": "Dimple", "age": 25, "city": "Ahmedabad"}
#Create a list of keys to check
check = ["name", "age"]

# Check if all keys exist in the dictionary
m1 = all(key in dic for key in check)

if m1:
    print("All keys exist in the dictionary.")
else:
    print("Some keys are missing.")
