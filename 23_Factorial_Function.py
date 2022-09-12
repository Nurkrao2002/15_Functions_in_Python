def factorial(n):
    if n==0:
        return 1
    else:
        r=n*factorial(n-1)
        return r
n=abs(int(input("Enter any Number:")))
print(f"{n}! =" ,factorial(n))

""" 2nd way """
# import math
# print(math.factorial(5))