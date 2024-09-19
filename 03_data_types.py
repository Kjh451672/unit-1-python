"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

elements = [1, "two", False,"Lies"]
print(elements)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

#Appending item into elements list
elements.append(420)
print(elements)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

#Removing element from list
elements.remove("two")
print(elements)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

#Changes the value of the element at specified index
elements[0] = "One"
print(elements)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
#Appending new elements to the end of the list
elements.append(True)
elements.append("Sonic")
elements.append(70)
print(elements)
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
#Deleting an elemet from specific index
del elements[5]
print(elements)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
#Setting variable to first two elements
two_elements = [elements[0],elements[1]]
print(two_elements)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
#Adding two_elements to original list
updated_list = elements + two_elements
print(updated_list)