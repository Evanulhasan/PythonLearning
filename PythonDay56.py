# Introduction to OOPs in Python 

# What is Object-Oriented Proramming 

"""Object-Oriented Programming (OOP) in Python is a 
programming paradigm that organizes software design 
around data, or "objects," rather than functions and
logic"""

"""
Core Concepts: Classes and ObjectsOOP relies on two 
primary building blocks:
Class: A user-defined blueprint
or template used to create objects. It defines the 
structure and behavior of the data.
Object: A concrete instance of a class. Every object 
has its own data state and can execute the functions 
defined by its class."""


"""1. Encapsulation (Hiding Data)
The Concept: Bundling data (variables) and methods (functions) inside a single class,
and protecting them from being changed directly from the outside.
Real-World Analogy: A capsule of medicine. The ingredients are hidden and protected inside the shell.

Python"""
class BankAccount:
    def __init__(self):
        # The double underscore '__' makes the variable private
        self.__balance = 0 
        
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. Secret balance updated.")
        
"""2. Abstraction (Hiding Complexity)
The Concept: Showing only the essential features to the user while 
hiding the complex background details. You force child classes to 
implement certain methods.
Real-World Analogy: Driving a car. You know how to use the steering wheel and pedals, but you don't need to know how the engine injects fuel.

Python
from abc import ABC, abstractmethod
"""
from abc import ABC, abstractmethod

class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self):
        pass # The complex logic is hidden/left to the child class

class TVRemote(RemoteControl):
    def turn_on(self):
        print("Sending infrared signal to turn on the TV.")
        
"""3. Inheritance (Reusing Code)
The Concept: Creating a new class that takes on (inherits) the properties
and behaviors of an existing class. It prevents you from writing the 
same code twice.
Real-World Analogy: A child inheriting traits (like eye color) from their parents, but also having their own unique traits.

Python
"""
class Animal:
    def eat(self):
        print("I am eating food.")

# Dog inherits the 'eat' method from Animal
class Dog(Animal): 
    def bark(self):
        print("Woof woof!")

my_dog = Dog()
my_dog.eat()  # Inherited behavior
my_dog.bark() # Unique behavior

"""4. Polymorphism (Many Forms)
The Concept: Different classes can be treated as the same type through 
a common interface. The same method name will do different things 
depending on which class is using it.
Real-World Analogy: The command "Speak!". If you say it to a dog, it barks. If you say it to a duck, it quacks. Same command, different actions.

Python"""
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# The same loop calls .speak() but gets different results
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())





























