
# learning try and

age = input('Whats your age?')
try: 
    age = int(age)
except: 
    print("Please use numbers")
if age < 20:
    print('I`m under 20 ' + str(age))


