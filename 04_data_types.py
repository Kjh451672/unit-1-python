'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

y = 10
#Conditional checking if variable is even and equal to 10 
print(y == 10 and y % 2 == 0)

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

age = 16
student = False
#Checks age and status to decide price for ticket
if (age < 18 or student == True):
    {
    print("Pay $10 for a ticket")
    } 
else:
    {
    print("Pay $20 for a ticket")
    }

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

fruits = ["apple", "orange", "banana"]
#Asks user to input a fruit name
print("please enter a fruit name")
user_fruit = input()
#Determines whether the fruit entered is in list
if (user_fruit in fruits):
    {
        print("Yes, that fruit is in the list")
    }
else:
    {
        print("No, that fruit is not in the list.")
    }

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
#promtps user to enter a year
print("Enter a year number")
year = int(input())
#Checks if year is divissable by 100 and divissible by 4
if (year % 100 == 0 and year % 4 == 0):
    {
        print("This year is a leap year, and a century year.")
    }

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

package_weight = 18
destination_zone = "Zone B"
#If statement checks for zone destination and mulitplies by weight. If weight is 0, returns "ERROR"
if (destination_zone == "Zone A"):
    {
        print("Shipping Cost: $" + str(package_weight * 5))
    }
elif (destination_zone == "Zone B"):
    {
        print("Shipping Cost: $" + str(package_weight * 7))
    }
elif(package_weight == 0):
    {
        print("ERROR")
    }

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
side_a = 15
side_b = 14
side_c = 14
#If statement determines whether the triangle is Equilateral, Isosceles, Scalene, or not a triangle
if(side_a == side_b and side_a == side_c):
    {
        print("This is an equilateral triangle.")
    }
elif(side_a == side_b and side_c != side_a and side_c != side_b):
    {
        print("This is an isosceles triangle.")
    }
elif(side_a != side_b and side_c != side_a and side_c != side_b):
    {
        print("This is a scalene triangle.")
    }
elif(side_a <= 0 or side_b <= 0 or side_c <= 0):
    {
        print("This is not a triagle")
    }