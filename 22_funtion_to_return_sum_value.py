def sum():  
    a=int(input('Enter the value of a:'))                     # function definition
    b=int(input('Enter the value of b:'))                     # function definition
    c=a+b
    return c
    return 'The value of {}+{} is {}'.format(a,b,c)
print(sum())
