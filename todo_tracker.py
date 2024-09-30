#Have these variables outside of list so they are unaffected by each new iteration
with open("my_file.txt") as file:
    to_do_list = file.readlines()

while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(to_do_list)
    print("Would you like to add, remove, edit, display, clear all or exit out of your list?")
    option = input()

#Adds a new item to the list
    if option == "add":
        print("Please type in your next todo.")
        next_todo = input()
        to_do_list.append(next_todo)

#Removes an item from the list
    if option == "remove":
        print(to_do_list)
        print("Please type in the todo # you want to remove")
        next_remove = int(input())
        del to_do_list [next_remove - 1]

#Removes all items from the list
    if option == "clear all":
        to_do_list.clear()

#Allows user to edit an item in the list
    if option  == "edit":
        print(to_do_list)
        print("Please type in the todo # you want to edit")
        next_edit = int(input())
        print("Now please type in the change you want to make.")
        to_do_list[next_edit - 1] = input() 

#Displays the entire list
    if option == "display":
        num = 1
        for x in to_do_list:
            print(f"{num}){x}")
            num += 1
#Exits out of todo list while saving contents of list
    if option == "exit":
        with open("my_file.txt", "w") as file:
            file.writelines(to_do_list)
        break
    
#Corrects the user if they typed in an incorrect option
    if option != "exit" or option != "display" or option != "edit" or option != "clear all" or option != "remove" or option != "add":
        print("Sorry, that doesnt match any of the options. Please try again.")
            

    