# Challenge:
# Write a program to prompt the user for their hourly wage and the number of hours they work per week.
# Compute their annual salary. If they work more than 40 hours per week, calculate the overtime pay at 1.5 times 
# their regular hourly rate for the hours worked above 40. The program should also compare their annual salary 
# to someone earning a specified salary and determine who earns more and by how much. 
# Put the logic to do the computation of the annual salary in a function called compute_annual_salary() 
# and use the function to do the computation. The function should return the annual salary. 
# Use the function to compare the salaries and print the results. Assume there are 52 weeks in a year.



# 1. Prompt the user for their hourly wage.
# 2. Prompt the user for the number of hours they work per week.
# 3. Compute the annual salary, considering overtime pay for hours worked above 40 per week.
# 4. Use a function called compute_annual_salary() to perform the computation.
# 5. Compare the user's annual salary to a specified salary (e.g., $50,000) and determine who earns more and by how much.
# 6. Print the results.

hrs = input("Enter Hours:")
 
rate = input("Rate per hour:")
rt = float(rate)
hr = float(hrs)

def computepay(hr, rt):
    if hr > 40:
        hrs =  hr - 40
        extrapay = (rt* 1.5)
        overtimepay = (hrs* extrapay)
        regularpay = 40 * rt
        payment = (regularpay + overtimepay)
        anualp = payment * 52
        anualpay = anualp - 43620
        
    return(anualpay)

# total for 21$ per hour and 40 hours is 43,680

        
p = computepay(hr, rt)
print("Difference on Pay for someone making 43620 is", p)

