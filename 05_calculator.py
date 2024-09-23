import math
#Prompts user for two numbers of any value
print("Please enter a number")
number_one = float(input())
print(number_one)
print("Please enter a second number")
number_two = float(input())
print(number_two)
#Asks user what kind of operation they want to perform, by showing them the options and having them type it in
print("How would you like to use these numbers? Please type in one of these methods: Addition, Subtraction, Multiplication, Division, Floor Division, Exponential, or Remainder")
operator_choice = input()
#If statement performs operation chosen by the user
if(operator_choice == "Addition"):
    {
        float(print(number_one + number_two))
    }

elif(operator_choice == "Subtraction"):
    {
    float(print(number_one - number_two))
    }

elif(operator_choice == "Multiplication"):
    {
    float(print(round(number_one * number_two)))
    }

elif(operator_choice == "Division"):
    {
    float(print(number_one / number_two))
    }

elif(operator_choice == "Floor Division"):
    {
       print(math.floor(number_one / number_two))
    }

elif(operator_choice == "Exponential"):
    {
        print(round(pow(number_one, number_two)))
    }

elif(operator_choice == "Remainder"):
    {
        float(print(number_one % number_two))
    }