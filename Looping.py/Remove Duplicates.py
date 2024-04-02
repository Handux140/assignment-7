original_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]

# Convert the list to a set to remove duplicates
unique_elements = set(original_list)

# Convert the set back to a list if necessary
unique_list = list(unique_elements)

print("Original list:", original_list)
print("List after removing duplicates:", unique_list)