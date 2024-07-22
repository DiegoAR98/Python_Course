# Task 1: Basic Arithmetic Operations
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Exponentiation:", a ** b)
print("Modulo:", a % b)

# Task 2: Order of Operations
result = 1 + 2 ** 3 / 4 * 5
print("Result without parentheses:", result)

result = 1 + ((2 ** 3) / 4) * 5
print("Result with parentheses:", result)

# Task 3: Type Conversions
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)

print("Type of num_int:", type(num_int))
print("Type of num_float:", type(num_float))

try:
    print("Adding string and integer:", num_str + 1)
except TypeError:
    print("Cannot add string and integer directly")
    print("Adding after conversion:", int(num_str) + 1)

# Task 4: Using Input Function
name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
print(f"Hello {name}, you are {age} years old.")

# Task 5: Working with Floating Point and Integer Division
x = 10
y = 3

print("Integer division:", x // y)
print("Floating point division:", x / y)

# Task 6: Checking Even or Odd
def is_even(number):
    return number % 2 == 0

user_number = int(input("Enter a number to check if it is even or odd: "))
if is_even(user_number):
    print(f"{user_number} is even.")
else:
    print(f"{user_number} is odd.")
