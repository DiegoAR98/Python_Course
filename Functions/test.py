# Challenge:
# Write a program to prompt the user for the number of items they purchased and the price per item using input.
# Compute the total cost. If the user purchased more than 50 items, they get a 10% discount on the total cost.
# Put the logic to do the computation of the total cost in a function called compute_total_cost() and use the function to do the computation.
# The function should return a value. Use 60 items and a price of 2.50 per item to test the program (the total cost should reflect the discount).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# 135$

itens = input('How many itens did you bought it ?')
price = input ('Whats the price did you pay per item ?')

it = float(itens)
pr  = float(price)

def compute_total_cost():
    if it > 50: 
        tcost = (it * pr)
        discount = (tcost * 0.10)
        fprice = (tcost - discount)
    return (fprice)


total = compute_total_cost()
print(total)
