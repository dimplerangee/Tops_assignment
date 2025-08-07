'''Q:34 Write a Python function that takes two lists and returns true if they 
have at least one common member.'''

# Sample lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 7]

found_common = False

for item in list1:
    if item in list2:
        found_common = True
        break

if found_common:
    print("True – Lists have at least one common member.")
else:
    print("False – No common members found.")
