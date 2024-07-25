x = 5
if x < 10:
    print('Smaller')
if x < 6: print('testing')
if x > 20:
    print('Bigger')
print('Finis')

# Comparison Operators in Python

# <  : Less than
# <= : Less than or equal to
# == : Equal to
# >= : Greater than or equal to
# >  : Greater than
# != : Not equal

# one way decisions 

x = 5
print('Before 5')
if x == 5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')

print('Before 6')
if x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')                      


# nesting 

x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
        print('Done with i', i)
print('All Done')
