# Set-1

# Q-1

# d={}
# for i in range(1,9):
#     d[i]=i*i
# print(d)


# Q2

# input_numbers = input("Enter comma seperates numbers :")
# List = input_numbers.split(',')
# print("List :",List)
# Tuple =tuple(List)
# print("Tuple :", Tuple)

# Q3

# class IOString():
#     def __init__(self):
#         self.str1 = ""
#
#     def get_String(self):
#         self.str1 = input("Enter tne string :")
#
#     def print_String(self):
#         print(self.str1.upper())

# str = IOString()
# str.get_String()
# str.print_String()
#
# def test_function():
#     x= IOString()
#     x.get_String()
#     x.print_String()
# test_function()


# Q4
# words = input("Enter comma seprated words :")
# print(words)
# list_of_words = words.split(',')
# print(list_of_words)
# sorted_words = sorted(list_of_words)
# print("sorted_words :",sorted_words)

# Q5
# t1 = (1,2,3,4,5,6,7,8,9,10)
# l1 = []
# for i in t1:
#     if i%2 == 0:
#         l1.append(i)
# t2 = tuple(l1)
# print(t2)

# Q-6

# class Circle():
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius**2
#
# x = Circle(10)
# print(x.area())

# Q-7

# import re
# email = input("Enter email :")
# regex = '[a-z]+'
# username = re.match(regex,email)
# print(username[0])

# Q-8
#
# x = int(input("Enter number of elements"))
# list1 = []
# list2 = []
# for i in range(x):
#     element = int(input("Enter a number"))
#     list1.append(element)
# for i in list1:
#     if i%2!=0:
#         list2.append(i)
# list2.sort()
# print(list2)

# Q-9

# num_lines = 0
# num_words = 0
# num_chars = 0
#
# with open(r"C:\Users\HP\Desktop\abc.txt", 'r') as f:
#     for line in f:
#         words = line.split()
#
#         num_lines += 1
#         num_words += len(words)
#         num_chars += len(line)
# print(num_lines)
# print(num_words)
# print(num_chars)

