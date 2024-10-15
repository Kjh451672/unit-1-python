"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    #Accounting for when num2 is 0
    try:
        result = num1 / num2
        print("Result:", result)
    except:
        print("Your second number is 0, which you cant devide by.")
    finally:
        print("End of example #1")
# Example usage:
divide_numbers(10, 0)


"""
Example 2: Opening Files
"""

def read_file(filename):
    #Accounting for when the txt file does not exist
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
        file.close()
    except:
        print("The file you used does not exist")
    finally:
        print("End of example #2")

# Example usage:
read_file("nonexistent.txt")

"""
Example 3: List Items
"""

def get_item(lst, index):
    #Accounting for when it tries to call an index outside of list ragne
    try:
        item = lst[index]
        print("Item:", item)
    except:
        print("The index you inputed is out of range")
    finally:
        print("End of example #3")
# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)


"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    #Accounting for when key is not in dictionary
    try:
        value = dictionary[key]
        print("Value:", value)
    except:
        print("Key is not found in dictionary")
    finally:
        print("End of example #4")


# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")


"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    #Accounts for if the file does exist
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        print("File accessed successfully")
    finally:
        print("End of example #5")

# Example usage:
process_file("example.txt")



