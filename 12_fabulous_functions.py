import math 
"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""
#Agrgument takes in name and adds it to print statement
def greet_user(name):
    print("Hello, " + name)

greet_user("Kyle")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

#Takes square root of the argument
def square_root(num1):
    return math.sqrt(num1)
    
print(square_root(9))

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
#Uses % operator to test if argument is even or odd
def even_odd(num2):
    if num2 % 2 == 0:
        return True
    else:
        return False
    
print(even_odd(20))

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
#Takes in two arguments and ultiplies them for area
def rect_area(length, width):
    return length * width
print(rect_area(3,6))

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
#Takes in degrees in celcius and converts it to fahrenheit
def cel_to_fahr(celcius):
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit
print(cel_to_fahr(45))

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
#Creating a pre-made list for the arguemnt to work properly
num_list = [23, 13, 7, 58, 48]
#Function uses a for-loop to count number of items in list, and stores values to find average
def average_mean(the_list):
    my_sum = 0
    for x in the_list:
        my_sum += x
    return my_sum/len(the_list)
print(average_mean(num_list))

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""

#Takes in price and quantity of items, and decides on discount based on quantity of items
def store_calculator(price, quantity, discount = 1.0):
    return (price * quantity) * discount

print(store_calculator(3,7, 0.8))