temperature = 75

#Added = sign to the first elif statement, and changed the second elif statment to an else statement 
if temperature > 80:
    print("It's hot")
elif temperature >= 50:
    print("It's temperate")
else :
    print("It's cold")




text = "Hello, world, my name is"
count = 0

#Change "" to " " so it properly reads spaces
for char in text:
    if char == " ":
       count += 1

print(count)




print("give me a number")
n = int(input())

#Changed less than sign to ==, set n = to int(input()), and had range set to n + 1
for num in range(1, n + 1):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")




num = int(input("Enter an integer: "))
#Changed ranged to num + 1, and add str() to all variables in end print statement
if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num + 1):
    result *= i   

  print("Factorial of " + str(num) + " is " + str(result))




attempts = 1
correct_password = "secret"
#Added a break statement if password is correctly guessed, moved attempts variable to te end of the if statement, set attempts = 1, changed condition to if attempts ==3, and chnged if-statement to have password = correct password
while True:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts == 3:
        print("Too many attempts")
        break
    attempts += 1
