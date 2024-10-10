"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""
#Agrgument takes in name and adds it to print statement
def greet_user(name):
    """
    The gree_user function, as stated by its name, is used to greet the user. 
    When using the function, it usesa string as an argument, and prints it out along with "Hello".
    """

    print("Hello, " + name)

greet_user("Kyle")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

#Takes square root of the argument
def square_num(num1):
    """
    The square_num function, takes in either an integer or a float, and multiplies it by itself.
    It then returns the value of the operation, when you print out the function with an argument.
    """

    return num1 * num1 

    
print(square_num(9))

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
#Uses % operator to test if argument is even or odd
def even_odd(num2):
    """
    The even_odd function takes in an integer or a float, and uses the % operator.
    If it results in 0, it returns true for even. If it results in anything else, it returns false for odd.
    """

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
    """
    The rect_area function takes in two numbers as arguments. One number is the length, while the other is the width.
    It multiplies length times width to find the area of a rectangle, and returns the result.
    """

    return length * width
print(rect_area(3,6))

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
#Takes in degrees in celcius and converts it to fahrenheit
def cel_to_fahr(celcius):
    """
    The cel_to_fahr function takes in a number(celcius). 
    Then it uses it in the equation used to convert celcius to fahrenheit.
    Then, it returns the result.
    """

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
    """
    The average_mean function takes in an argument that is a list of numbers.
    It goes throughout the entire list and finds the mean of all of the numbers.
    """

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
    """
    The store calculator function calculates the price of items. 
    It takes in three arguments: One for the price, one for the quantity, 
    and a 3rd optional argument for a discout. It then multiplies all three 
    numbers together, and returns the total amount.
    """
    return (price * quantity) * discount

print(store_calculator(3,7, 0.8))