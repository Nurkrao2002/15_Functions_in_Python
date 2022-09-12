""" Local Scope
Value can be accessed inside the function only """
"""
def fun():
    x=7;y=8;z=9
    print(x+y)
fun()
"""

""" Global Scope of a Variable , can be accessed by anyone """
""" 
a=2
def bm():
    a=4
    b=3;c=5
    print(a)
    print(b)
print(a)
bm()
print(a)
"""

""" global is the keyword , which is need to be specified if we want to use 
the local variable as global variable. """
"""
c=4
def fun1():
    a=3
    global c,b
    b=8
    c=9
    print(b)
print(c)
fun1()
print(c)
print(b)
print(c)
"""

""" Count the length of a string without using built-in function """
""" 
def fn(st):
    c=0
    for i in st:
        c+=1
    return c
print(fn('python'))
"""

""" A guy having multiple names """
"""
def sc():
    school='John'
    print(f'Name in School is {school}')
    cl()
def cl():
    college='Max'
    print(f'Name in College is {college}')
def wk():
    work='Peter'
    print(f'Name at work location is {work}')
    sc()
wk()
"""