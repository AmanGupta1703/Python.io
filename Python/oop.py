# class Employee:
#     # class Attribute
#     company = "Google"

# Aman = Employee()
# print(Aman.company)
# Employee.company = "YouTube"
# print(Aman.company)


# class Programmer:
#     company = "MicroSoft"

#     def __init__(self, name, product):
#         self.name = name
#         self.product = product

#     def getInfo(self):
#         print(f"Name of the employee: {self.name}")
#         print(f"The product that he work for: {self.product}")


# emp_1 = Programmer("Aman", "Xbox")
# emp_1.getInfo()


# q2
# class Calculator:
#     def __init__(self, num):
#         self.number = num
        
#     def sqaure(self):
#         print(f"The sqaure of {self.number} is {self.number **2}")
    
#     def sqaureRoot(self):
#         print(f"The sqaure of {self.number} is {self.number **0.5}")
    
#     def cube(self):
#         print(f"The cube of {self.number} is {self.number **3}")

    
  
# a = Calculator(3)
# a.sqaure()
# a.cube()
# a.sqaureRoot()

# q3
# class Sample:
#     a = 10
    
#     @staticmethod
#     def greet():
#         print("Hello")
    
    
# obj = Sample()
# obj.greet()
# print(Sample.a)
# obj.a = 1
# print(obj.a)

# q5
'''
class Train:
    def __init__(self, trainName, trainFare, seatLeft):
        self.trainName = trainName
        self.trainFare = trainFare
        self.seatLeft = seatLeft
    
    def getStatus(self):
        print("==================================")
        print(f"Train Name: {self.trainName}")
        print(f"Number of seats left: {self.seatLeft}")
        print("==================================")
        
    def getTrainFareInfo(self):
        print("==================================")
        print(f"Train Fare: {self.trainFare}")
        print("==================================")

    def bookATicket(self, numOfTicketToBook):
        print("==================================")
        if self.seatLeft > 0:
            print("Ticket Booked")
            self.seatLeft -= numOfTicketToBook
            self.getStatus()
        else:
            print("No Available Seats")
    
        print("==================================")

    def canelTicket(self, cancelTicket):
        print("==================================")
        print("You have cancelled your ticket.")
        self.seatLeft += cancelTicket
        self.getStatus()
        print("==================================")

intercity = Train("Intercity-141010", 90, 50)
intercity.getStatus()
intercity.getTrainFareInfo()
intercity.bookATicket(23)
intercity.canelTicket(20)
'''

# q6

# class Sample:
#     a = "Aman"
    
#     def __init__(self, name):
#         self.name = name

# obj = Sample("Aman")

