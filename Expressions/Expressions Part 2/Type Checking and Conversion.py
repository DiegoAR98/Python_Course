# Checking types
x = "Hello"
y = 10
print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'int'>

# Converting types
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print(num_int)   # Output: 123
print(num_float) # Output: 123.0

# Handling type errors
try:
    result = x + 1
except TypeError as e:
    print(f"Type error occurred: {e}")

# Output: Type error occurred: can only concatenate str (not "int") to str
