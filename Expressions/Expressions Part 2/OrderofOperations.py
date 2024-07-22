# Without parentheses
result = 1 + 2 ** 3 / 4 * 5
print(result)  # Output: 11.0

# With parentheses for clarity
result = 1 + ((2 ** 3) / 4) * 5
print(result)  # Output: 11.0

# Example showing explicit order of operations with parentheses
result = (5 ** 6) / (4 / (2 * 3))
print(result)  # Output: 390625.0
