# Single Inheritace 
# class Employee:
#     company = "Google"
    
#     def showDetails(self):
#         print("This is an employee")

# class Programmer (Employee):
#     language = "Python"
#     # over-riding the property of the parent class
#     company = "YouTube"

#     def showDetails(self):
#         print("This is an programmer")

#     def getLanguage(self):
#         print(f"The language is {self.language}")

# MultipleLevel
# class Employee:
#     company = "Visa"

# class FreeLancer:
#     company = "Fiverr"
#     level = 0
    
#     def upgradeLevel(self):
#         self.level = self.level + 1
        
# class Programmer(Employee, FreeLancer):
#     name = "Aman"
    
    
# p = Programmer()
# p.upgradeLevel()
# p.upgradeLevel()
# print(p.level) 

# MultiLevel
# class Person:
#     country = "India"
#     city = "Mumbai"

#     def takeBreath(self):
#         print("I am breathing...")

# class Employee(Person):
#     company = "Fiverr"

#     def takeBreath(self):
#         print("I a employee so I am luckily breathing...")

# class Programmer(Employee):
#     company = "Honda"

#     def takeBreath(self):
#         print("I a programmer so I am breathing++...")



# p = Person()
# p.takeBreath()

# e = Employee()
# p.takeBreath()
# print("City: "+ p.city)

# pr = Programmer()
# pr.takeBreath()
# print("Country: "+ pr.country)

# super method
# class Person:
#     country = "India"
#     city = "Mumbai"
    
#     def __init__(self):
#         print("Initializing Person...\n")

#     def takeBreath(self):
#         print("I am breathing...")

# class Employee(Person):
#     company = "Fiverr"
    
#     def __init__(self):
#         super().__init__()
#         print("Initializing Employee...\n")

#     def takeBreath(self):
#         super().takeBreath()
#         print("I a employee so I am luckily breathing...")
        

# class Programmer(Employee):
#     company = "Honda"
    
#     def __init__(self):
#         # super().__init__()
#         print("Initializing Programmer...\n")

#     def takeBreath(self):
#         super().takeBreath()
#         print("I a programmer so I am breathing++...")
        
# p = Person()
# p.takeBreath()
# print("\n")

# e = Employee()
# e.takeBreath()
# print("\n")

# pr = Programmer()
# pr.takeBreath()



# class methods

# class Employee:
#     name = "Aman"
#     salary = 100
    
#     # def changeSalary(self, sal):
#     #     self.salary = sal
    
#     @classmethod
#     def changeSalary(cls, sal):
#         cls.salary = sal
        
# e = Employee()
# print(e.salary)
# e.changeSalary(200)
# print(e.salary)
# print(Employee.salary)


# getters setters class decorator
# class Employee:
#     name = "Bharat Gas"
#     salary = 5600
#     salaryBonus = 400
#     # totalSalary =

#     @property
#     def totalSalary(self):
#         return self.salary + self.salaryBonus
    
#     @totalSalary.setter
#     def totalSalary(self, val):
#         self.salaryBonus = val - self.salary 
    
# e = Employee()
# print(e.totalSalary)
# e.totalSalary = 5800
# print(e.totalSalary)
# print(e.salaryBonus)

# ps
# q1
# class c2dVector:
    
#     def print(self):
#         print("I am c2dVector")
        
# class c3dVector(c2dVector):
    
#     def print(self):
#         super().print()
#         print("I am c3dVector")
    
# c = c2dVector()
# c.print()
# print("\n")
# d = c3dVector()
# d.print()

# q2
# class Animals:
    
#     def __init__(self):
#         print("I am a Animal Class")

# class Pets(Animals):
#     def __init__(self):
#         super().__init__()
#         print("I am a Pet Class")

# class Dogs(Pets):
#     def __init__(self):
#         super().__init__()
#         print("I am a Dog Class")
        
# a = Animals()
# p = Pets()
# d = Dogs()

# q3
from time import sleep
from idna import valid_contextj


# class Employee:
#     salary = 100
#     increement = 200
    
#     @property
#     def salaryAfterIncreement(self):
#         totalSalary = self.salary * self.increement
#         return totalSalary
    
#     @salaryAfterIncreement.setter
#     def salaryAfterIncreement(self, val):
#         self.increement = val / self.salary 
        
# e = Employee()
# print(e.salaryAfterIncreement)
# e.salaryAfterIncreement = 1000
# print(e.salaryAfterIncreement)
# print(e.increement)

# q3
class Complex:
    