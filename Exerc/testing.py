# Write a program to prompt the user for the number of items sold and the price per item using input to compute the total sales amount.
# Use 20 items and a price of 15.50 per item to test the program (the total sales amount should be 310.00).
# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

# Total Sales Amount: 310.00

sold = input('how many itens sold?')
price = input('Whats the price per item?')

sold = int(sold)
price = float(price)

total = sold * price

print('Total Sales Amount:',+ total)