# a=8 # global variable
# def n():
#     a=10
#     print("The local variable value is:",a) # local variable
# n()
# print("The global variable value is:",a)

'''Note: The value of the global variable can be used by local function variable
  containing print .
  But the value of the local variable cannot be used by the global function variable
  containing print.
  
  '''

# x=20
# def f1():
#   global x
#   x=5
#   print(x)
# print(x)
# f1()
# print(x) 