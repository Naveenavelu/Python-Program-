# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:16:39 2024

@author: Naveena Palanivelu
"""

# Example for Abstract class

#from abc import ABC, abstractmethod
from math import pi

class Shapes():
    
    def area(self1):
        pass
 #   @abstractmethod
    def perimeter(self1):
        pass

class Rectangle(Shapes):
    def __init__(self1, width, height):
        self1.width = width
        self1.height = height
    def area(self1):
        Area= self1.width * self1.height
        return Area
    def perimeter(self1):
        Perimeter= 2 * (self1.width + self1.height)
        return Perimeter

class Circle(Shapes):
    def __init__(self1, radius):
        self1.radius = radius
    def area(self1):
        Area1 = pi * self1.radius ** 2
        return Area1
    def perimeter(self1):
        perimeter1= 2 * pi * self1.radius
        return perimeter1
class Square(Shapes):
    def __init__(self1, side):
        self1.side = side
    def area(self1):
        Area2 =  self1.side ** 2
        return Area2
    def perimeter(self1):
        perimeter2= 4 *  self1.side
        return perimeter2
# Show examples how to use the classes above
r = Rectangle(3, 4)     
print(r.area())         
print(r.perimeter())    
c = Circle(3)             
print(c.area())            
print(c.perimeter())  
s = Square(5)             
print(s.area())            
print(s.perimeter())       
