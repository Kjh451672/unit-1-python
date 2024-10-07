#Importing from datetime 
from datetime import date
from datetime import time
from datetime import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
#Stores current time and date for one instance
current_time = datetime.now()
print(current_time)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

#Formats current time to typical U.S. time
my_string = current_time.strftime("%m/%d/%Y")
print(my_string)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
#Takes two strings and formats them into ddates
date_one = "08/13/2007"
date_two = "11/09/2024"
date_one = datetime.strptime(date_one, "%m/%d/%Y")
date_two = datetime.strptime(date_two, "%m/%d/%Y")
print(date_one)
print(date_two)
#Finds the number of days between both dates
print(date_two - date_one)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

#Aks user for date of birth
print("Please enter your birthdate in mm/dd/yyyy format.")
user_date = input()
user_date = datetime.strptime(user_date, "%m/%d/%Y")
#Calculates age by dividing by 365
age = ((current_time - user_date)/365)
print("You are " + str(age) + " years old.")