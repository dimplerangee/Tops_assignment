'''Q:41 Write a Python program to check whether a list contains a sub list '''



# Big list
main_list = [1, 2, 3, 4, 5]

# Small list we want to find inside the big list
sub_list = [3, 4]

# Let's say we haven't found it yet
found = False

# Go through the big list one by one
for i in range(len(main_list) - len(sub_list) + 1):
    
    # Get a small part (slice) from the big list
    part = main_list[i:i + len(sub_list)]
    
    # Check if this part is same as sub_list
    if part == sub_list:
        found = True
        break  # Stop the loop if we found it

# Print the result
if found:
    print("Yes, the sublist is in the main list.")
else:
    print("No, the sublist is not in the main list.")
