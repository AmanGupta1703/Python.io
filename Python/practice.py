# print('Hello, World!')

'''
what is a module ?
module is a file containing the code writteb by somebody else but can be imported and used in our Program

what is pip?
pip is a python package manager
used to install external modules on your computer

python features
Easy to understand = less development time
Free and open source 
high level language
poratable => can be used in linux mac 

REPL -> READ EVALUATE PRINT LOOP

variable is a name given to a memory location in a program

variables -> container to store value

type() -> helps to find out the data type of a given variable

input() -> allows to take input from the user in a form of a String

String is a data-type in python

String is a sequence of characters

String slicing -> we can slice a String to get a part of that String 

String functions

len() -> returns the length of the String

endswith(' ') -> returns a boolean value 

capatalize() -> capatilizes the first character of the String 

find(word) -> finds the first occurence of the given character

replace(oldWord, newWord) -> replaces the oldword with the new word 

list -> container to store a set of values of any data-type

List Methods

l1 = [2, 1, 3, 4]

sort() -> updates the list to [1, 2, 3, 4]

reverse() -> updates the list to [4, 3, 1, 2]

append(5) -> adds 5 at the end of the list

insert(0, 0) -> insert 0 at index 0 

pop(2) -> will remove value at index 2 and return its value

remove(4) -> remove 4 from the list

tuples are immutable datatypes in python

once defined -> the elements of tuples cannot be altered and manipulated

tuple methods:

count(2) -> returns the number time 2 occurs in the tuple

index(2) -> will return the first occurence of 2 in the tuple

Dictionary -> is a collection of key-value pairs

Dictionary Properties
Unordered
Indexed
mutable
cannot contain duplicate values

Dictionary methods

item() -> returns the list of the dictionary as a tuple

key() -> returns a list of keys present in the dictionary

update("Key": "value") -> updates the dictionary with supplied key-value pairs

get('keyName') -> returns the value of the specified key

'''

# myDic = {
#     "Pankha": "Fan",
#     "Dabba": "Box",
#     "Vastu": "Item"
# }

# print(myDic)

# print("The options are: ", myDic.keys() , "\n")
# a = input("Enter the Hindi Word: ")

# print("English word for", a, "is: ", myDic.get(a))

# num_1 = input('Enter the number: ')
# num_2 = input('Enter the number: ')
# num_3 = input('Enter the number: ')
# num_4 = input('Enter the number: ')
# num_5 = input('Enter the number: ')
# num_6 = input('Enter the number: ')
# num_7 = input('Enter the number: ')
# num_8 = input('Enter the number: ')

# s = {num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8}

# print(s)

# s = {18, '18', 18}
# print(s)

# s = {1, 2, 3, 'Harry', [4, 5, 6]}

# print(s) 
# print(12 + 3)

# print(15 % 2)

# name = input("Enter you name: ")
# print(type(name))

# a = 34
# b = 80
# print(a > b)

# num_1 = int(input("Enter a number: "))
# num_2 = int(input("Enter a number: "))

# average = (num_1 + num_2) / 2

# print("Average: ", average)

# a = int(input("Enter a number: "))
# print("Sqaure of the given number: ", (a*a))

# name = input("Enter your name: ")
# print("Good Morning, "+ name)

 
# date = input("Enter the date: ")

# letter =  '''
# Dear <|Name|>,
# \tYou're selected!
# Date: <|Date|>
# ''' 
# letter = letter.replace("<|Name|>", name)
# letter = letter.replace("<|Date|>", date)

# print(letter)

# string = "This is a good  game"
# doubleSpaces = string.find("  ")
# print(doubleSpaces)

# c = string.replace("  ", " ")
# print(c)

# letter_1 = "Dear Harry,\n\tThis is course is very helpful.\nThanks"
# print(letter_1)
'''
fruit_1 = input("Enter the name of the fruit you like: ")
fruit_2 = input("Enter the name of the fruit you like: ")
fruit_3 = input("Enter the name of the fruit you like: ")
fruit_4 = input("Enter the name of the fruit you like: ")
fruit_5 = input("Enter the name of the fruit you like: ")
fruit_6 = input("Enter the name of the fruit you like: ")
fruit_7 = input("Enter the name of the fruit you like: ")

l1 = []
l1.append(fruit_1)
l1.append(fruit_2)
l1.append(fruit_3)
l1.append(fruit_4)
l1.append(fruit_5)
l1.append(fruit_6)
l1.append(fruit_7)
print(l1)


mark_1 = int(input("Enter your mark for sub_1: "))
mark_2 = int(input("Enter your mark for sub_2: "))
mark_3 = int(input("Enter your mark for sub_3: "))
mark_4 = int(input("Enter your mark for sub_4: "))
mark_5 = int(input("Enter your mark for sub_5: "))
mark_6 = int(input("Enter your mark for sub_6: "))

marks = [mark_1, mark_2, mark_3, mark_4, mark_5, mark_6]

marks.sort()
print("Marks:", marks)


t1 = (1, 2, 3, 4, 5)
t1[0] = 4
print(t1)


num_1 = int(input("Enter a number:"))
num_2 = int(input("Enter a number:"))
num_3 = int(input("Enter a number:"))
num_4 = int(input("Enter a number:"))

l1 = [num_1, num_2, num_3, num_4]
sumOfList = l1[0] + l1[1] + l1[2] + l1[3]
print(sumOfList)
'''


# a = (7, 0, 8, 0, 0, 9)
# print(a.count(0))

'''
myDict = {
    "pankha": "fan",
    "darwaza": "door",
    "dabba": "Box" 
}
print("Hindi Words: ", myDict.keys())
hindiWord = input("Enter the word: ")
print("English Translation: ", myDict[hindiWord])

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
num_3 = int(input("Enter a number: "))
num_4 = int(input("Enter a number: "))
num_5 = int(input("Enter a number: "))
num_6 = int(input("Enter a number: "))
num_7 = int(input("Enter a number: "))
num_8 = int(input("Enter a number: "))

numbers = {num_1, num_2, num_3, num_4, num_5, num_6, num_7}
print(numbers)

a = {18, "18"}
print(a)
'''
'''
s = set() #-> empty set
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))


S = {}
print(type(S))

friend_1 = input("Enter your favorite subject: ")
friend_2 = input("Enter your favorite subject: ")
friend_3 = input("Enter your favorite subject: ")
friend_4 = input("Enter your favorite subject: ")


friends = {
    
}

updateFriendsDic = {
    "friend_1": friend_1,
    "friend_2": friend_2,
    "friend_3": friend_3,
    "friend_3": friend_4
}

friends.update(updateFriendsDic)
print(friends)

a = [1, 2, 4]

if 2 in a:
    print(a)
else:
    print("No")
'''

# num_1 = int(input("Enter a number: "))
# num_2 = int(input("Enter a number: "))
# num_3 = int(input("Enter a number: "))
# num_4 = int(input("Enter a number: "))

# if (num_1 > num_4):
#     f = num_1
# else: 
#     f = num_4
    
# if (num_2 > num_3):
#     f_1 = num_2
# else:
#     f_1 = num_3
    
# if f > f_1:
#     print(str(f) + " is the greatest")
# else:
#     print(str(f_1) + " is the greatest")

# marks_1 = int(input("Enter your marks: "))
# marks_2 = int(input("Enter your marks: "))
# marks_3 = int(input("Enter your marks: "))
# marks_4 = int(input("Enter your marks: "))

# totalMarks = (marks_1 + marks_2 + marks_3 + marks_4)/400 * 100


# if marks_1 < 33 or marks_2 < 33 or marks_3 < 33 or marks_4 <33:
#     print("You have failed")
# elif totalMarks >= 40:
#     print("You have the passed") 
# else:
#     print("You have failed")

# text = input("Enter a text: ")

# if "make a lot of money" in text:
#     spam = True
# elif "buy now" in text:
#     spam = True
# elif "subscribe" in text:
#     spam = True
# elif "click this" in text:
#     spam = True
# else:
#     spam = False


# if spam: 
#     print("Spam Text")
# else:
#     print("Not a spam Text")

# username = input("Enter your Username: ")

# if len(username) >= 10:
#     print("You're good to go.")
# else:
#     print("Username should of length greater than 10 characters")

# name = input("Enter your name: ")

# l1 = ["Aman", "Kunal", "Teddy"]
# print("Before adding any value: ", l1)

# if name in l1:
#     print("Is Presnt")
# else:
#     l1 = l1.append(name)
#     print(l1)

# print(l1)

# text = "Harry"

# comment = input("Write your comment: ")

# if comment in text:
#     print(text + " is present in the comment")
# else:
#     print(text + " is not present in the comment")

# i = 1   
 
# while i <= 50:
#     print(i)
#     i = i + 1
    
# nameList = ["Aman", "Kunal", "Raj"]

# # i = 0

# # while i < len(nameList):
# #     print(nameList[i])
# #     i = i + 1


# for name in nameList:
#     print(name)
    
# T1 = (1, 2, 3, "aman") 

# for element in T1:
#     print(element)

# n = 4

# for i in range(1, 11):
#     result = n * i
#     print(f"{n} X {i} = {result}")

# l1 = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l1:
#     if name.startswith("S"):
#         print("Good Morning, "+ name)
#     else:
#         print("Good Night!!" + name)
        

# i = 1

# while i <= 10:
#     result = n * i
#     print(f"{n} X {i} = {result}")
#     i += 1
    
    
# n = int(input("Enter a number: "))

# isPrime = True

# for i in range(2, n):
#     if n % i == 0:
#         isPrime = False
#         break
        
# if isPrime:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

# number = int(input("Enter a number: "))

# factrial_base = 1

# for i in range(1, number+1):
#     factrial_base = factrial_base * i
    
# print("Factorial", str(factrial_base))


# sum = 0

# for i in range(1, number+1):
#     sum = sum + i
    
# print("Sum: "+ str(sum))

# n = 4
# for i in range(4):
#     print(" * " * (i+1))

# n = 3

# for i in range(3):
#     print(" " * (n - i - 1), end="")
#     print("*" * (2*i+1), end="")
#     print(" " * (n - i - 1))

# n = 2

# i = 10

# while i >= 1:
#     result = n * i
#     print(f"{n} X {i} = {result}")
#     i = i - 1




# def factorial_recursive(n):

#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)

# n = factorial_recursive(5)

# print(n)

# def MaxOfThreeNumbers(a, b, c):
#     if a > b:
#         if a > c:
#             return a
#         else:
#             return c
#     else:
#         if b > c:
#             return b
#         else:
#             return c
        
        
# a = MaxOfThreeNumbers(12, 99, 56)
# print(a)


# def ConvertFranhToCel(celisus):
#     return (celisus * (9/5) ) + 32

# franh = ConvertFranhToCel(100)
# print(franh)

# def Sum(n):
#     if n <= 1:
#         return n
#     else:
#         return n + Sum(n - 1)
        
# sum_recursive = Sum(10)
# print(sum_recursive)        


# def PrintPattern(n):
#     for i in range(n+1):
#         print(" * " * (n - i))
        
# print(PrintPattern(10))

# def ConvertInchToCms(inch):
#     return (inch * 2.54)

# inch = 20
# convert = ConvertInchToCms(inch)

# print(convert)

# def remove_and_strip(string, word):
#     newStr = string.replace(word, "")
#     return newStr.strip()

# string = "      This is a Box      "
# print("Before using the function:\n"+ string)
# n = remove_and_strip(string, "Box")
# print("After using the function(remove_and_strip()):")
# print(n)

# def MultiplicationTable(n):
#     for i in range(1, 11):
#         result = n * i
#         print(f"{n} X {i} = {result}")

# MultiplicationTable(2)
# print("\n")
# MultiplicationTable(4)
# print("\n")
# MultiplicationTable(6)
# print("\n")
# MultiplicationTable(10)
        
# f = open("sample.txt", "r")
# data = f.read()
# print(data)
# f.close()

# f = open("sample.txt", "r")
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# f.close()




# f = open("sample.txt", "w")
# f.write("This is text which i am writing to the file_2\n")
# f.close()

# f = open("sample.txt", "a")
# f.write("I am trying to append to the file")
# f.close()

# f = open("sample.txt", "r")
# data = f.read()
# print(data)
# f.close()

# with open("sample.txt", "r") as f:
#     data = f.read()
    
# with open("sample.txt", "w") as f:
#     data = f.write("I am re-writing the content of this file.\n")

# with open("sample.txt", "a") as f:
#     data = f.write("I am appeding to the content of this file.\n")


# print(data)


# with open("sample.txt", "r") as f:
#     data = f.read()
#     if "twinkle" in data:
#         print("Twinkle is present")
#     else:
#         print("It is not present")


# print(data)

# def game():
#     return 34


# score = game()
# with open("sample.txt") as f:
#     hiScoreStr = f.read()

# if hiScoreStr == '':
#     with open("sample.txt", "w") as f:
#         f.write(str(score))

# if int(hiScoreStr) < score:
#     with open("sample.txt", "w") as f:
#         f.write(str(score))

# for i in range(1, 21):
#     with open(f"tables/Multp_table_of_{i}", "w") as f:
#         for j in range(1, 11):
#             result = i * j
#             f.write(f"{i} X {j} = {result}\n")
#             if j != 10:
#                 f.write("\n")
    

# with open("sample.txt") as f:
#     content = f.read()
    
# content = content.replace("donkey", "#$#$#$#$#^")

# with open("sample.txt", "w") as f:
#     f.write(content)




# words = ["donkey", "fat", "pig"]

# with open("sample.txt") as f:
#     content = f.read()
    
# for word in words:
#     content = content.replace(word, "#$#$#$#$#^")
    
#     with open("sample.txt", "w") as f:
#         f.write(content)


# with open("log.txt") as f:
#     content = f.read().lower()
    
# if content.find("python"):
#     print("Python is presnt")

# content = True
# i = 0
# with open("log.txt") as f:
#     while content:
        
#         content = f.readline()
        
#         if "python" in content.lower():
#             print(content)
#             print("Python is presnt")
#             print(i)
#         i += 1

# with open("this.txt") as f:
#     content = f.read()
    
# with open("copy.txt", "w") as f:
#     f.write(content)

# file_1 = "copy.txt"
# file_2 = "this.txt"

# with open(file_1) as f:
#     f = f.read()
    
# with open(file_2) as f:
#     f2 = f.read()
    
# if f == f2:
#     print("files are identical")
# else:
#     print("files are not identica;")



# with open("sample.txt", "w") as f:
#     f.write("")
    
import os

old_name = "copy.txt" 
new_name = "renamed_by_python.txt"

with open(old_name) as f:
    content = f.read()
    
with open(new_name, "w") as f:
    f.write(content)

os.remove(old_name)