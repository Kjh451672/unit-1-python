"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.
"""
#Created float variable
my_float = 13.1
print(my_float)
#Converting float variable into an integer, and printing out the new value
my_float = int(my_float)
print(my_float)

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

#Prompting user to input a numerical value
print("Give me any number")
num = int(input())
#Created if-staement defining wheteher num is positive, zero, or negative
if num > 0:
    {print("This number is positive!")}
elif num < 0:
    {print("This number is negative!")}
elif num == 0:
    {print("This number is zero!")}

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

#Promted user to input a whole and a decimal number
print("Give me a whole number")
first_num = int(input())
print("Now give me a decimal number")
second_num = float(input())
#Prints out sum, difference, product, and quotient
print((first_num + second_num))
print((first_num - second_num))
print((first_num * second_num))
print((first_num / second_num))

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

#Created dictionary with different fruits
fruit_stock ={
    'apples':4,
    'bananas':7,
    'pears':9
}
#Returns value of that fruit's stock
print(fruit_stock["bananas"])

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
#Variable with set of numbers
num_set = "2,4,6,8,10,12"
print(num_set)
#Converted string into list
num_list = num_set.split(",")
print(num_list)