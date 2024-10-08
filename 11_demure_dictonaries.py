#Stores contact information
contact_book = dict()

while True:
    #Starts a new line, checks for user input()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Edit Contact")
    print("4. List Contacts")
    print("5. Exit")
    print("Enter the number of your choice:")
    user_choice = int(input())

#Allows user to enter a new contact into contact book
    if user_choice == 1:    
        print("Please type in the name of the contact you'd like to add:")
        new_name = input()
        print("Now enter thier phone number. (Do not use dashes):")
        new_number = input()
        if new_number.isnumeric == False or (len(new_number) >= 11 or len(new_number) <= 9):
            print(" Error: Invalid number. Returning to Menu")
            continue
        contact_book[new_name] = new_number
#Removes contact from contact book
    if user_choice == 2:
        print("Which person's number would you like to remove:")
        remove_name = input()
        if remove_name in contact_book:
            del contact_book[remove_name]
        if remove_name not in contact_book:
            print(" Error: Name not in contact book. Returning to menu")
            continue
#Edits an already existing number from contact book
    if user_choice == 3:
        print("Which person's number would you like to edit:")
        check_name = input()
        if check_name in contact_book:
            print("Please type in the new number. (Do not use dashes):")
            edit_number = input()
            if edit_number.isnumeric == False or (len(edit_number) >= 11 or len(edit_number) <= 9):
                print("Error: Invalid number. Returning to menu.")
                continue
            else:
                contact_book[check_name] = edit_number
        if check_name not in contact_book:
            print(" Error: Name not in contact book. Returning to menu")
            continue

#Prints out entire contact book
    if user_choice == 4:
        num = 1
        for x in contact_book:
            print(f"{num}.{x}")
            num += 1
            
#Closes contact book
    if user_choice == 5:
        break
            