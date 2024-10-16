"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    return None
  else:
    return a / b
#Checking for if a is properly divided by b
assert divide(8,2) == 4
assert divide(6,3) == 2
assert divide(4,0) == None
"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

#Cheking for if n is multiplied by itself from 1 to n
assert factorial(5) == 120
assert factorial(3) == 6
assert factorial(0) == 1

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

#Checking for if all charecters in a string are flipped
assert reverse_string("12345") == "54321"
assert reverse_string("ABCDE") == "EDCBA"
"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
#Checks for fibonacci sequence up to number n
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(5) == 5

"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None

#Checks for if a email is in proper format
assert is_valid_email("myexample@gmai.com") == True
assert is_valid_email("h3llogmail.com") == False