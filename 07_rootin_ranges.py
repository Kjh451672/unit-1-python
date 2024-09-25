"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

#Prints number 1-10
for x in range (1, 11):
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
#Skip counts by 10 from 900-1000
for x in range(900, 1001, 10):
    print(x)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
#Skip counts by 9 from 1-100
for x in range(1, 101, 9):
    print(x)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
numbers_sum = 0
for x in range (1, 11):
    numbers_sum += x
print(numbers_sum)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()


#The output of the code print an asteric once more than the previous line, for the number of rows.
#The reason for ths iterative proces has to do with the "i+1" as that determines the amount of asterics printed out on each line