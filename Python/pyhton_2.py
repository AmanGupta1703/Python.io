# Chapter 9 -> File I/O

# Use open function to read the content of the file!
# f = open('sample.txt', 'r')
# f = open('sample.txt') # by default the mode is r (read mode)

# Reading the file
# data = f.read()

# Reading the first five characters
# data = f.read(5)

# print("Reading from a file: " + data)

# closing the above file
# f.close()  


# Readline function
# f = open('sample.txt')

# data = f.readline()
# print(data)

# data = f.readline()
# print(data)

# f.close()

# f = open('another.txt', 'w')
# f.write('\nI am appending this to the file')
# f.close()
# print(f)

# with statement (context manager)
# with open('another.txt', 'w') as f:
#     a = f.write("Writing to a file using 'with statement'")
# print(a)

# Practice Set
# with open('poem.txt', 'r') as f:
#     a = f.read();

# if ('twinkle' in a):
#     print('Is present')
# else:
#     print('Not present')

# Q2
