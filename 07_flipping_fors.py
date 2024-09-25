"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
sentence = "420BlazeIt"
#For loop prints every chracter in sentence
for x in sentence:
    print(x)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
num_list = [16, 7, 91, 34, 21]
total = 0
#For loop stores each value in total through addition
for y in num_list:
    total += y
    print(total)
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

my_sentence = "This is a sentence"
new_sentence = my_sentence.split(" ")
character_sum = 0
#Stores length of each word and prints number of characters
for z in new_sentence:
    character_sum = len(z)
    print(character_sum)

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

ball_inventory = {
        "basketballs": 12,
        "baseballs": 7,
        "tennis balls": 16,
        "golf balls": 23
}
#Prints out each item n dictionary
for b in ball_inventory:
    print(ball_inventory[b])
#The following outcome of the code was what I expected, in that it didnt print the name of 
#each of the itmes in the dictionary, but just their values.