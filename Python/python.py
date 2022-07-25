# Autor: Aman
# Location: Moon
# Date: 20/8/90

#  ----------------- Chapter 1(Modules, Comments, pip)         -> Single line comment   -----------------
'''
Learning pyhton!    -> Multi-line comment
'''
# import os    importing the os module
# from playsound import playsound
# print("Hello, World!")

#   ----------------- Chapet 1 practice set  -----------------

#  Q1
# print(''' 
# "Twinkle, twinkle, little star,"
# "How I wonder what you are!" 
# "Up above the world so high,"
# "Like a diamond in the sky. ''')
#  
# Q3
#  playsound('"C:\\Users\Kunal\\Videos\\My Senpai is a Bunny Girl\\04. There Is No Tomorrow For A Rascal HDPrimeHUB.Org.mkv"')        

# Q4
# print(os.listdir())


#  ----------------- Chapet 1 practice set end  -----------------



# Chapter 2 ->  ----------------- Variables and Data-types  -----------------

# a = 30
# name = ''' "Aman" '''
# b = 45.32

#  Printing the variables 
# print(name)

#  Printing the type of variables
# print(type(a))
# print(type(b))
# print(type(name))

# print()

#   -----------------Opeartors  -----------------
# number1 =  100
# number2 =  50

# print("Airthematic Operators") 
# print("The value is: ", (number1 + number2))
# print("The value is: ", (number1 - number2))
# print("The value is: ", (number1 * number2))
# print("The value is: ", (number1 / number2))
# print()

# print("Assignment Operators")
# number = 25
# number += 12
# number *= 12
# number -= 12
# number /= 12
# print("Value: ", number)
# print()

#   ----------------- Comparion operator  -----------------
# print("Comapre Value: ", a > b)
# print("Comapre Value: ", a < b)
# print("Comapre Value: ", a >= b)
# print("Comapre Value: ", a <= b)
# print("Comapre Value: ", a == b)
# print("Comapre Value: ", a != b)


#   ----------------- Logical Operators  -----------------
# bool1 = True
# bool2 = False

# print()
# print("The value of bool1 and bool2: ", (bool1 and bool2))
# print("The value of bool1 and bool2: ", (bool1 or bool2))
# print("The value of not bool2: ", (not bool2))

#   ----------------- TypeCasting  -----------------
# print()
# print("TypeCasting: ")
# a = "3434"
# a = int(a)
# print(type(a))
# print("Value after TypeCasting: ", a + 5)

#  ----------------- Input function  -----------------
#  a = input("Enter a number: ")
# Converting String to Integer and adding 80 to it(if Possible)
# print(int(a) + 80)  

#  ----------------- Practice set  ----------------- -> Chapter 2
# print(5 + 7)
# print(8 % 4)
# print()

# age = input("Enter your age: ")
# print(type(age))
# print()

# a = 34
# b = 80
# print("Compare a and b: ", a > b)
# print()

# sqaure_of_input_number = input("Enter a number: ")
# sqaure_of_input_number = int(sqaure_of_input_number)
# square = sqaure_of_input_number * sqaure_of_input_number
# print("Sqaure of input number: ", square)

# a = input("Enter the first number: ")
# b = input("Enter the second number: ")
# a = int(a)
# b = int(b)
# average = (a + b) / 2

# print("Average: ", average)

# Chapter 2 ->  ----------------- practice set end -----------------

# Chapter 3 ->  ----------------- Strings  -----------------
# name = "Aman"
# greeting = "Good morning"

#Cocatenating two Strings
# c = greeting + ", " + name 

# print(name[:3]) # -> chharcters from 0 to 3 (3 - 1)

# print(name[ : -1]) # -> (represents length - 1)

# name = "AmanIsHere"
# d = name[0::3]
# print(d)

#  ----------------- String functions  -----------------
# story = "once there was a Youtuber named harry who uploaded harry python course with notes"
# print(len(story))
# print(story.endswith("notes"))
# print(story.count("a"))
# print(story.capitalize())
# print(story.find("harry"))
# print(story.replace("harry", "codeWithHarry"))

#  ----------------- Escape characters  -----------------
# story = "harry is good.\n\tHe i\\s very good\'s"
# print(story)

# Chapter 3 ->  ----------------- practice set  -----------------
# 1
# name = input("Enter Your name: ")
# print("Good Afternnon, ", name)


# Letter templet -> Q2
# letter = '''
# \tDear <|Name|>, 
# \tYou are selected!
# \tDate: <|Date|>'''

# name = input("Enter Your Name: ")
# day = input("Enter Date: ")
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", day)

# print(letter)

# -> Q3
# sentence = "Today is a rainy  day."
# doubleSpace = sentence.find("  ")
# print(doubleSpace)

# -> Q4
# sentence = "Today is a rainy  day."
# doubleSpaceReplace = sentence.replace("  ", " ")
# print(doubleSpaceReplace) 

# -> Q5
# letter = "Dear Harry, \n\tThis Python course is nice. \nThanks!"
# print(letter)

# Chapter 3 ->  ----------------- practice set end -----------------

# Chapter 4 ->  ----------------- List and Tuples  -----------------

# Creating a list
# a = [1, 2, 4, 56, 6]

# Printing the list using print function
# print("Before change: ", a)

# Accessing the list using:
# print("Value of 0th index: ", a[0])

# Changing the value of the list
# a[0] = 98
# print("After change: ", a)

# We can create a list with items of differnt data types
# a = ["Aman", 6.3, False, 49]
# print(a)

# List Slicing
# friends = ["Harry", "Tom", "Rohan", "Sam", "Divya", 45]
# print(friends[0:4])
# print(friends[-4:])

#  ----------------- List Methods  -----------------
# l1 = [1, 8, 7, 2, 21, 15]

# Sorts the original list (i.e: l1)
# l1.sort()

# l1.reverse() 

# l1.append(45) # -> adds 45 at the end of the list

# l1.insert(0, 544)

# l1.pop(2) # -> removes element at index 2

# l1.remove(21) # -> removes 21 from the list  
# print(l1)

#  ----------------- Tuples -----------------

#  ----------------- Creating a tuple   -----------------
# a = (1, 2, 3, 4, 5)

# t = () # -> Empty Tuple

# t = (1) # -> wrong way to declare a tuple with single element

# t = (1, ) # -> Tuple with a single element

#  Printing the element of a tuple
# t = a[0]
# print(t)

# Tuple Method
# a = (1, 2, 3, 4, 5, 1, 1, 1, 1)

# print(a.count(1))
# print(a.index(1))

# ----------------- Practice Set - chapter 4 -----------------

# Q1
# fruits = []

# fruit_1 = input("Enter the fruit: ")
# fruit_2 = input("Enter the fruit: ")
# fruit_3 = input("Enter the fruit: ")
# fruit_4 = input("Enter the fruit: ")
# fruit_5 = input("Enter the fruit: ")
# fruit_6 = input("Enter the fruit: ")
# fruit_7 = input("Enter the fruit: ")

# fruits.append(fruit_1)
# fruits.append(fruit_2)
# fruits.append(fruit_3)
# fruits.append(fruit_4)
# fruits.append(fruit_5)
# fruits.append(fruit_6)
# fruits.append(fruit_7)

# print(fruits)

# Q2
# marks = []

# mark1 = int(input("Enter your marks: ")) 
# mark2 = int(input("Enter your marks: ")) 
# mark3 = int(input("Enter your marks: ")) 
# mark4 = int(input("Enter your marks: ")) 
# mark5 = int(input("Enter your marks: ")) 
# mark6 = int(input("Enter your marks: "))

# marks.append(mark1)
# marks.append(mark2)
# marks.append(mark3)
# marks.append(mark4)
# marks.append(mark5)
# marks.append(mark6)

# marks.sort()
# print(marks)

# Q3
# t = (1, 2, 3)
# t[0] = 2    # throws TypeError 
# print(t)

# Q4
# l = [1, 2, 3, 4]
# print(l[0] + l[1] + l[2] + l[3])
# print(sum(l)) # -> using sum method

# Q5
# a = (7, 0, 8, 0, 0, 9)
# print(a.count(0)) 
# ----------------- Practice Set End - chapter 4 -----------------

# ----------------- chapter 5 -> Dictionary and Sets -----------------
# myDict = {  
#     "Fast": "In a fast manner",     # -> Key - value pairs 
#     "Harry": "A Coder",
#     "Marks": [1, 2, 5],
#     "anotherDic": {
#         "Harry": "A YouTuber"
#     }
# }

# print(myDict["Fast"])
# print(myDict["Harry"])
# print(myDict["Marks"])
# print(myDict["anotherDic"]['Harry'])
# myDict['Marks'] = [45, 89]  # -> chaninging the value of the list 
# print(myDict["Marks"])

# Dictionary Methods
# myDict = {  
#     "fast": "In a fast manner",     # -> Key - value pairs 
#     "harry": "A Coder",
#     "marks": [1, 2, 5],
#     "anotherDic": {
#         "Harry": "A YouTuber"
#     }, 
#     1: 2
# }
# 
# print(list(myDict.keys()))    # -> typeCasting and printing the keys of the disctionary
# print()
# print(myDict.values())       # -> prints the values of the dictionary 
# print()
# print(myDict.items())       # -> prints the (Key, value) for all contents of the dictionary

# print()
# print(myDict)

# updateDic = {
    # "Lovish": "Friend",
    # "Subham": "Friend",
    # "harry": "A Dancer"
# }
# myDict.update(updateDic) # -> update tje dictionary by the adding the key-value pairs fromt the updateDic

# Diff beyween .get method and [] syntax in dictionaries?
# print(myDict.get("harry")) # -> prints the value associated with key "harry" 
# print(myDict["harry"]) # -> prints the value associated with key "harry"     

# print(myDict.get("harry2")) # -> returns None as harry2 is not present in the myDic dictionary
# print(myDict["harry2"]) # -> throws an error (KeyError) as harry2 is not present in the myDic dictionary     

# ----------------- chapter 5 -> Sets -----------------
# a = {1, 3, 4, 6}
# print(a)
# print(type(a))

# Empty set
# a = {}  # This syntax will create a empty dictionary and not a empty set
# print(type(a))

# An empty set can be created using the below syntax
# a = set()
# print(type(a))

# Set Methods

# a = set()

# a.add(2)
# a.add(3)
# a.add(19)
# a.add((1,8,7)) # -> a tuple can be added to the set but a list cannot be added to a set

# Dictionary cannot be added to a set
# a.add({
#     "Name": "Kunal"
# })

# print(a)

# print("Length of Set a:", len(a))

# a.remove(19)

# print("Popping: ", a.pop(), " from the set.")

# print(a)

# ----------------- chapter 5 -> Prctice Sets -----------------

# Q1    
# myDic = {
#     "Pankha": "Fan",
#     "Dabba": "Box",
#     "Vastu": "Item"
# }

# print(myDic)

# print("The options are: ", myDic.keys(), "\n")
# a = input("Enter the Hindi Word: ")

# print("English word for", a, "is: ", myDic.get(a))

# Q2
# number_1 = int(input("Enter the number: "))
# number_2 = int(input("Enter the number: "))
# number_3 = int(input("Enter the number: "))
# number_4 = int(input("Enter the number: "))
# number_5 = int(input("Enter the number: "))
# number_6 = int(input("Enter the number: "))
# number_7 = int(input("Enter the number: "))
# number_8 = int(input("Enter the number: "))

# print()
# setOfNumbers = {number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8}

# print()
# print("Set of unique numbers:", setOfNumbers)

# Q3
# s = {"18", 18}
# print(s)

# Q4
# s = set() # -> Empty set
# s.add(20)
# s.add(20.0)
# s.add("20")

# print(s)
# print(len(s))

# Q5
# S = {}
# print(type(S))

# Q6
# nameDic = {}

# language_1 = input("\nEnter the language: ")
# language_2 = input("Enter the language: ")
# language_3 = input("Enter the language: ")
# language_4 = input("Enter the language: ")

# nameDic['Aman'] = language_1
# nameDic['Kunal'] = language_2
# nameDic['Ram'] = language_3
# nameDic['Shyam'] = language_4
 
# print("\n", nameDic)

 # ----------------- chapter 5 -> Prctice Set End -----------------

# ----------------- chapter 5 -> Conditional Statements -----------------


# a = 8
# if-elif-else ladder
# if(a < 3):
#     print('Number is greater than 4')
# elif(a > 13):
#     print('Number is greater than 13')
# elif(a > 7):
#     print('Number is greater than 7')    
# elif(a > 17):
#     print('Number is greater than 17')    
# else:
#     print('The value is not greater than 3 or 7')    
    
# print('Done')

# Multiple if statements
# a = 8

# if(a > 3):
#     if(a > 5):
#         print('Number is greater than 5 and')
#     print('Number is greater than 4')

# if(a > 13):
#   print('\nNumber is greater than 13')

# if(a > 7):
#   print('\nNumber is greater than 7')    

# if(a > 17):
#   print('\nNumber is greater than 17')    
# else:
#     print('\nThe value is not greater than 3 or 7')    
    
# print('Done')

# Quick Quiz
# age = int(input('Enter Your Age: '))

# Using Relational Operators
# if(age >= 18 ):
#     print('Yes')
# else:
#     print('No')    

# Using logical Operators
# age = 45

# if (age > 34 and age < 56):
#     print('You can work with us.')
# else:
#     print('You cannot work with us.')    

# in and is

# a = None
# if(a is None):
#     print('Yes')
# else:
#     print("No")    

# a = [45, 56, 6] # -> This is a list

# if(45 in a):
#     print("45 is present in the list.")    
# else:
#     print("45 is not present in the list.")

# ----------------- chapter 5 -> Conditional Statements Practice Set -----------------
# Q1

# if(num_1 > num_2):
#     if(num_1 > num_3):
#         if(num_1 > num_4):
#             print("Number 1 (", num_1, ") is greatest")
# elif(num_2 > num_1 and 
#      num_2 > num_3 and
#      num_2 > num_4):
#     print("Number 2 (", num_2, ") is greatest")
# elif(num_3 > num_1 and 
#      num_3 > num_2 and 
#      num_3 > num_4):
#     print("Number 3 (", num_3, ") is greatest")
# else:
#     print("Number 4 (", num_4, ") is greatest")             
# num_1 = int(input("Enter the number: "))
# num_2 = int(input("Enter the number: "))
# num_3 = int(input("Enter the number: "))
# num_4 = int(input("Enter the number: "))

# if(num_1 > num_4):
#     f1 = num_1
# else:
#     f1 = num_4
    
# if(num_2 > num_3):
#     f2 = num_2
# else:
#     f2 = num_3
    
# if(f1 > f2):
#     print(str(f1) + " is greatest")
# else:
#     print(str(f2) + " is greatest")
    
# Q2

# mark_1 = int(input('Enter Your Marks: '))
# mark_2 = int(input('Enter Your Marks: '))
# mark_3 = int(input('Enter Your Marks: '))

# if(mark_1 < 33 or mark_2 < 33 or mark_3 < 33):
#     print('You have failed the examination because you have scored less 33% percent in one(or more than one) subject')
# elif((mark_1 + mark_2 + mark_3) / 3 < 40):     
#     print('You have failed the examination because you have scored less 40% percent')
# else:
#     print('You have passed the examination.')

# Q3 

# text = input("Enter The Text: ")

# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This is a spam text")
# else:
#     print("This is not a spam text")

#  Q4

# 5:05:28
# username = input("Enter your username: ")

# if(len(username) > 10):
#     print("Username has more than 10 characters.")
# else:
#     print("Username has less than 10 characters.")

# Q5
# l = ["Aman", "Kunal", "Ram", "Shyam"]

# name = input("Enter your name: ")

# if(name in l):
#     print(name, " is present in the list")
# else:
#     print(name, " is not present in the list")

#  Q6

# marks = int(input("Enter you marks: "))
# grade = " "


# if marks > 90 and marks <= 100:
#     grade = "Excellent"
# elif marks > 80 and marks <= 90:
#     grade + "A"
# elif marks > 70 and marks <= 80:
#     grade + "B"
# elif marks > 60 and marks <= 70:
#     grade + "C"
# elif marks > 50 and marks <= 60:
#     grade + "D"
# else:
#     grade + "Fail"

    # print("Your Grade: ", grade)

# Q7

# post_comment = input("Enter the comment: ")

# if "Harry" in post_comment:
#     print("This post is talking about Harry")
# elif "harry" in post_comment:
#     print("This post is talking about Harry")
# elif "haRRy" in post_comment:
#     print("This post is talking about Harry")
# elif "hArrY" in post_comment:
#     print("This post is talking about Harry")
# elif "HArrY" in post_comment:
#     print("This post is talking about Harry")
# elif "HARRY" in post_comment:
#     print("This post is talking about Harry")
# else:
#     print("This post is not talking about Harry")    


# ----------------- chapter 6 -> Loops -----------------

# Quick Quiz
# i = 0
# while i <= 50:
#     print("#" + " " + str(i))
#     i += 1

# Quick Quiz

# l1 = ["Aman", "Kunal", "Raj"]

# i = 0
# while i < len(l1):
#     print(l1[i])
#     i += 1

# ---------------------- For Looop ---------------------

# fruits = ["Orange", 'Banana', "Mango", "WaterMelon"]

# for fruit in fruits:
#     print(fruit)

# ---------------------- Range ---------------------
# for i in range(1, 8, 3):  # starts from 0 and end at (n-1)
#     print(i)

# ---------------------- For Looop with else---------------------

# for i in range(10):
#     print(i)
# else:
#     print("Iteration Completed.")

# ---------------------- Break Statement ---------------------

# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# else:
#     print('This is inside else of for')
    
# ---------------------- Continue Statement ---------------------
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)

# ---------------------- pass Statement ---------------------

# i = 4
# if i < 10:
#     pass

# ---------------------- Chapter 7 -> Loop -> Practice Set ---------------------

# Q1

# number = int(input('Enter the number: '))

# for i in range(10, 1, -1):
#     print(str(number) + "X" + str(i) + " = " + str(number * i))
#     i = i - 1
#     print(f"{number} X {i} = {number * i}")

#  Q2

# names = ["Harry", "Sachin", "Subham", "Rahul"]

# for name in names:
#     if name.startswith("S"):
#         print("Hello, "+ name)
#     else:
#         pass

# Q3

# number = int(input('Enter the number: '))

# i = 1

# while i <= 10:
#     print(str(number) + "X" + str(i) + " = " + str(number * i))
#     i += 1

#  O4   Prime number divide by itself or divide by 1)

# number = int(input("Enter the number: "))
# prime = True

# for i in range(2, number):
#     if i % number == 0:
#        prime = False
#        break
   
# if prime:
#     print('The number is a prime number.')
# else:
#     print('The number is not a prime number') 

    

# Q5 ->

# number = int(input('Enter the number: '))

# sum = 0

# for i in range(1, number + 1):
#     sum = sum + i
# print(f'The sum of 1st n numbers are {sum}') 

# Q6 

# number = int(input('Enter the number: '))

# factorial = 1

# for i in range(1, number + 1):
#     factorial = factorial * i
# print(f'The factorial of {number} is {factorial}')

# Q7

# n = 4
  
# for i in range(1, n+1):
#     print(' * ' * i + ' ')  
    

# for i in range(3):
#     print(' ' * (n - i - 1), end=' ')
#     print('*' * ( 2 * i + 1), end=' ')
#     print(' ' * (n - i - 1))
    
            
#  Q9





# Q10

# number = int(input('Enter the number: '))

# for i in range(11, 1, -1):
#    print(str(number) + "X" + str(i) + " = " + str(number * i))
   
#    print(f" {number} X {i} = {number * i}")

#  Chapter 8 ============== Functions and Reursions
# Functions -> group of statement performing a specific task  (return -> laut chalo iss value ke sath)

# def greetings (usernameName):
#     print('Good Morning ', usernameName)

# name = input('Enter your name: ')

# greetings(name)

# Default Functions
# def greet(name = 'Stranger'):
#     print('Good Morning, '+ name)

# greet('Aman')
# greet()

# Recursions
# n = 5
# product = 1

# for i in range(n):
#     product = product * (i + 1)
# print(product)

# def factorial_iter(number):
#     n = 5
#     product = 1
#     for i in range(n):
#         product = product * (i + 1)
#     return product

# def factorial_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)
    
# n = 4

# print(factorial_recursive(n)) 

# Practice Set - 8

# def greatest_num(n1, n2, n3):
    
#     if n1 > n2:
#         if n1 > n3:
#             return str(n1) + ' is the greatest'
#         else:
#             return str(n3) + ' is the greatest'
#     else:
#         return str(n2) + ' is the greatest'
# n1 = 40
# n2 = 10
# n3 = 90

# compare_num = greatest_num(n1, n2, n3)

# print(compare_num)


# (0°C × 9/5) + 32 = 32°F

# def temp_convert_fraherheit(cel_temp):
#     return (cel_temp * (9/5)) + 32



# temp = int(input('Enter the temperature in celsius: '))

# frah = temp_convert_fraherheit(temp)

# print('The temperature in franhraheit: '+  str(frah))


# def sum(n):
     
#      if n == 0:
#         return 0
#      else:
#         return n + sum(n - 1)


# s = sum(5)

# print(s)



# 

# n = 6
# for i in range(n):
#     print(' * ' * (n - i))


# def convert_measure(inch):
#     return inch * 2.54

# inch = 90

# print(str(inch) + " -> " + str(convert_measure(inch)))


# Stripping a String


# def remove_and_split(string, word):
#     newStr = string.replace(word, " ")
#     return newStr.strip()

# this = 'Aman is here'

# n = remove_and_split(this, 'Aman')
# print(n) 

 # 
# def mult_table(n):
#     for i in range(1, 11, 1):
#         print(str(n) + "X" + str(i) + " = " + str(n * i ))
    
    
# n = 7
# print(mult_table(7))

