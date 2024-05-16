elements = ['1', '+', '2', '(', '3', '+', '4',')','(', '5', '+', '3', ')', '', '-', '4']

# List to store the indices of ')' followed by '('
indices = []

# Iterate through the list and check for ')' followed by '('
for i in range(len(elements) - 1):
    if elements[i] == ')' and elements[i + 1] == '(':
        indices.append((i, i + 1))
        print(type(indices))

# Print the results
if indices:
    for index_pair in indices:
        print(f"')' followed by '(' found at index {index_pair[0]} and {index_pair[1]}")
else:
    print("No ')' followed by '(' found")