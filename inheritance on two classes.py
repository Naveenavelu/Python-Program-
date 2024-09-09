# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 17:52:43 2024

@author: Naveena Palanivelu
"""
# inheritance on two classes 
class Details:
    def __init__(self):#constructor initializes the idn, name, and gender attributes 
        self.idn = 0
        self.name = ""
        self.gender = ""
 
    def setDetails(self):  #set the details of a person, including the ID number, name, and gende
        self.idn = input("Enter the ID Number : ")
        self.name = input("Enter the Name : ")
        self.gender = input("Enter the Gender : ")
 
    def showDetails(self):  # displays all the details of a student
        print("ID : ",self.idn)
        print("Name : ",self.name)
        print("Gender : ",self.gender)
 
class Student(Details):
    def __init__(self):
        self.total = 0
        self.per = 0
 
    def setStudent(self):
        self.setDetails()
        self.total = int(input("Enter the Total Mark : "))
        self.per = float(input("Enter the Percentage : "))
 
    def showStudent(self):
        self.showDetails()
        print("Total : ",self.total)
        print("Percentage : ",self.per)
 
class Staff(Details):
    def __init__(self):
        self.depart = ""
        self.salary = ""
 
    def setStaff(self): # method collects additional information related to staff, such as the department and salary,
        self.setDetails()
        self.depart = input("Enter the Department : ")
        self.salary = float(input("Enter the Salary : "))
 
    def showStaff(self): #  displays all the details of a staff member, including the common details (ID, name, and gender) from the Details class
        self.showDetails()
        print("Department : ",self.depart)
        print("Salary : ",self.salary)
 
print("Student Details : ")
stu = Student()
stu.setStudent()
stu.showStudent()
 
print("\nStaff Details : ")
stf = Staff()
stf.setStaff()
stf.showStaff()