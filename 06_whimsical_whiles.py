"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
#Continues printing until x becomes greater than 10
x = 1
while x <= 10:
    print(x)
    x += 1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
#Continues printing until y becomes equal than 0
y = 10
while y > 0:
    print(y)
    y -= 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
#Prompts user to enter a number
print("Enter a whole number")
integer = int(input())
#Checks for factorals by storing result and multiplying the previous number
z = 1
result = 1
while z <= integer:
    result *= z
    z += 1
print(result)

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = 23
password_guessed = False
#Prompts useer to enter a number, and gives hint depending if it's higher or lower
while password_guessed == False:
    print("Type in a two digit number and try to guess the password.")
    user_number = int(input())
    if(user_number == password):
        print("Correct!")
        password_guessed = True
    if(user_number > password):
        print("Incorrect! Try a lower number.")
    if(user_number < password):
        print("Incorrect! Try a higher number.")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""
stop = 1
previous_number = 0
next_number = 1
placeholder = 0
#Promts user for a number
print("Give me a whole number")
n = int(input())
while stop <= n:
    print(next_number)
    next_number += previous_number
    placeholder = next_number
    stop +=1