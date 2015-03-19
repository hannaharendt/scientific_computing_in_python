#!/usr/bin/env python

"""This is an example program to illustrate
	the notion of object-oriented programming
	and composition (Has-A Relationship)"""

# Programmer's point of view: composition involves embedding other objects in a container object,
# and activating them to implement container methods

# Designer's point of view: composition is another way to represent relationships in a problem domain.
# But rather than set membership, composition has to do with components - parts of a whole
# Composition also reflects the relationships between parts, called a "has-a" relationships
# Aggregation (weaker dependency between container and contained)
# Composition refers to a collection of embedded objects

# The composite class generally provides an interface all its own and implements it by directing the
# embedded objects

from oop_inheritance_example import PizzaRobot, Server

class Customer(object):
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "orders from", server)
    def pay(self, server):
        print(self.name, "pays for item to", server)

class Oven(object):
    def bake(self):
        print("oven bakes")

class PizzaShop(object):
    def __init__(self):         # Embed other objects
        self.server = Server('Pat')
        self.chef = PizzaRobot('Bob')
        self.oven = Oven()
    def order(self, name):      # Activate other objects
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()         # Make composite
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')
