# Function: It is a collection of statements
# a function will run only when you are calling it or else it wont run
# a function is represented by def keyword
# Syntax:  def functionname() , 0 arguments
# def functionname(n) , 1 arguments .... etc as many arguments as you want
# why we use functions? to make our code more efficient and reliable

# basic function program
# def sentence():  # function declaration
#     print("Hello we wrote a basic function program") # to print on screen
# sentence()  # calling the function

# little bit advanced
# def n(name):
#     print("Your name is:"+name)
# n() # TypeError: n() missing 1 required positional argument
# n("Josh Innovations")
# n("Parrot")
# n("Alba")
# n('Vijay')

# advanced
# A=input("Enter your A: ")
# B=input("Enter your B: ")
# C=input("Enter your C: ")
# D=input("Enter your D: ")
# A,B,C,D=[str(x) for x in input("Enter the value of 4 strings: ").split()]
# def n():
#     print("Your name is: "+A)
#     print("Your name is: "+B)
#     print("Your name is: "+C)
#     print("Your name is: "+D)
# n()


# name,name1=[x for x in input("Enter the Name:").split()]
# def n(name):
#     print("Your name is: "+name)
#     print("Your name is still: "+name1)
# n('Python')
# n(name)

# passing Hello , Josh , Python , Class
# Class for 4 times will be printed
# def n(name="Python"):
#     print("Hello "+name+" How are you?")
# n()
# n("HD")
# n("Josh")
# n("RSVJ")


# def f1(name='XYZ',age=None,year=2021):
# 	age=int(input("Enter your age:"))
# 	print(f'your name is {name}, age is {age} in the year {year}')

# f1()
# f1('HD')
# f1('SD')
# f1('CD')
# f1('NF')
# f1('HN')


# def n(*name):
#     print("Hello "+str(name[1])+" How are you?")
# n('python','adv','fun')


# return statement in functions 
def num():
    print("Python")
    return 2+2
def raj():
    print("Tkinter")
    return 5+2
# print(num())
# print(raj())