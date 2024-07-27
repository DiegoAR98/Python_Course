
#functions

def fname ():
    print('Hello')
    print('Diego')

fname()

def fmaxvalue (numbers):
    return max(numbers)

# max use

numbers = [1, 2, 10, 20, 50]
biggervalue =  fmaxvalue(numbers)

print(biggervalue)


# type conversions 

print (float(99) / 100)

# NOT.E FOR SELf (ALWAYS REMEMBER TO INVOKE A FUNCTION)

# Parameters

def thebest (player):
    if player == 'Ronaldinho':
        print('Ronadinho is the best')
    elif player == 'Messi':
        print('Second GOAT')
    elif player == 'CR7':
        print('No skills at all')

thebest('Ronaldinho')     

# Return Values

def greet():
    return "Hello"

print(greet(), "Alex")

# Multiple parameters

def addition (a, b):
    add = a + b
    return add
x = addition(5, 5)
print(x)