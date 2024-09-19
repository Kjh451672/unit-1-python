"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive
"""

#Created custom password
password = "forlenza23"
#Promting user to enter password
print("Please enter the password. (Lowercase letters only)")
user_input= input()
#Checks if user inputed correct password
if user_input == password:
    {print("Password Accepted.")}
else:{
    print("Inccorect Password")
}

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

#Prompts user to type anything
print("Hey there. Type anything you want!")
any_string = input()
#Check if user typed anything or not
if any_string == "":
    {print("Invalid")}
else:
    {print("Valid")}

"""
TASK 3:
Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""

#Made a placeholder sentence
my_sentence = "I love cats. I love playing fetch with my cat."
print(my_sentence)
#Replaces all instances of "cat" with "dog"
new_sentence = my_sentence.replace("cat","dog")
print(new_sentence)

"""
TASK 4:
Write a program that takes a person's name and age as input and prints it
"""

#Ask user for their name and age
print("Please input your name")
user_name = input()
print("Now enter your age")
user_age = int(input())
#Takes in name and age and prints it out
text = f"Your name is {user_name} and you are {user_age} years old."
print(text)

"""
TASK 5:
Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
#Ask user for two deimal numbers
print("Please enter a decimal number")
first_float = float(input())
print("Now enter a second decimal number")
second_float = float(input())
#Prints quotient with 1 decimal point
quotient = (first_float/second_float)
text_two = f"Result:{quotient:.1f}"
print(text_two)