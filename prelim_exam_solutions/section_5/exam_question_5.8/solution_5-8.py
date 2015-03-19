#!/usr/bin/env python

""" Solution to midterm exam question on
    class object-oriented programming and composition"""

# Simulate a fast-food ordering scenario by defining four classes:
#       * Lunch: A container and controller class
#       * Customer: The actor who buys food
#       * Employee: The actor from whom a customer order
#       * Food: What the customer buys

class Lunch(object):
    def __init__(self, name):
        self.customer = Customer(name)
        self.employee = Employee('Rani')
    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)
    def result(self):
        self.customer.printFood()

class Customer(object):
    def __init__(self, name):
        self.name = name
        self.food = None
    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)
        # Implicit instance creation of Employee class object
    def printFood(self):
        print "%s ordered %s." %(self.name, self.food.name)

class Employee(object):
    def __init__(self, name):
        self.name = name
    def takeOrder(self, foodName):
        return Food(foodName)
        
class Food(object):
    def __init__(self, name):
        self.name = name
        
if __name__ == "__main__":
    lunch = Lunch('Chinggay')
    lunch.order('sinigang')
    lunch.result()
