n = 5
while n > 0:
    print(n)
    n = n -1

print(n)


# Break statments

while True:
    line = input('>')
    if line == 'done':
        break
    # it only gonna break when the input is "done"
    print(line)
print('done!')

# Finishing iteration with Continue

while True:
    line = input('>')  # Prompt the user for input and assign it to the variable 'line'
    if line[0] == '#':  # Check if the first character of the input line is '#'
        continue  # If it is, skip the rest of the loop and prompt for input again
    if line == 'done':  # Check if the input line is exactly 'done'
        break  # If it is, exit the loop
    print(line)  # Print the input line
print('Done!')  # Print 'Done!' after exiting the loop
