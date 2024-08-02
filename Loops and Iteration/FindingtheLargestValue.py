# finding the biggest number

number = -1 
print('Before', number)

for i in [9, 41, 12, 3, 74, 15, 124, 565, 66, 43, 345]:
    if i > number:
        number = i
    print(number, i)
print('After', number)

# finding the smallest number

# Initialize the variable smallest to None, which will hold the smallest value found
smallest = None

# Print the initial statement before the loop starts
print('Before')

# Iterate over each value in the list
for value in [9, 41, 12, 3, 74, 15]:
    # If smallest is None (i.e., this is the first iteration), set smallest to the current value
    if smallest is None:
        smallest = value
    # If the current value is less than the current smallest value, update smallest to the current value
    elif value < smallest:
        smallest = value
    # Print the current smallest value and the current value from the list
    print(smallest, value)

# Print the final smallest value after the loop has completed
print('After', smallest)
