"""
Task 0: Class We-Do
"""

class Character:
    health = 20

    def __init__(self, name):
        self.name = name

    def damage(self,dmg = 1):
        self.health = self.health - dmg

enemy1 = Character("Balthazar") 
enemy1.damage(3)
print(enemy1.health)


class Player(Character):
    health = 50

    def heal(self):
        if self.health < 50:
            self.health = self.health + 1

player1 = Player("Kyle")
player1.heal()
print(player1.health)

"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

#Created a Person class that takes in a person's name and age, and prints it out introducing them
class Person:
    species = 'Human'
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def introduce(self):
        print("Hello " + self.name +", you are " + str(self.age) + " years old.")
#Executes functions in Person class
kyle = Person("Kyle", 17)
print(kyle.species)
kyle.introduce()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("This animal's name is " + self.name +". They are " + str(self.age) + " years old.")
#Subclasses of the Animal class
class Dog(Animal):
    def speak(self):
        print("Bark, Woof!")

class Cat(Animal):
    
    def speak(self):
        print("Meow, Hsss!")

#Executes functions in Animal, Dog, and Cat classes
sparky = Dog("Sparky", 3)
sparky.introduce()
sparky.speak()
misty = Cat("Misty", 5)
misty.introduce()
misty.speak()
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
#Class handles bank accounts with withdrawls and deposits
class BankAccount:
    def __init__(self, owner, balance = 2000):
        self.owner = owner
        self.balance = balance
#Widthdrawl substracted from balance
    def widthdraw(self, widthdrawl):
        self.widthdrawl = widthdrawl
        self.balance = self.balance - self.widthdrawl
#Deposit added to balance
    def deposit(self, depositing):
        self.depositing = depositing
        self.balance = self.balance + self.depositing

jake = BankAccount("Jake")
jake.widthdraw(20)
print(jake.balance)
jake.deposit(50)
print(jake.balance)