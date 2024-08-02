# counting in a loop 

zork = 0
print ('Before', zork)

for i in [1, 2, 4, 65, 67, 787, 787, 8]:
    zork = zork + 1
    print (zork, i)

print('After,', zork)


# summing in a loop

zork = 0
print ('Before', zork)

for i in [1, 2, 4, 65, 67, 787, 787, 8]:
    zork = zork + i
    print (zork, i)

print('After,', zork)


# finding the average

count = 0
sum = 0

print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)

print('After', count, sum, sum / count)

# filtering in a loop

print('Start')

for i in [1, 34, 455, 65, 76, 87, 87, 45, 3, 2, 5]:
    if i > 20:
        print  (i, 'is bigger then 20')

print('After loop')

# search using boolean variable

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        # after find the 3 and define the found to TRUE, it always gonna bre true now
    print(found, value)
print('After', found)
