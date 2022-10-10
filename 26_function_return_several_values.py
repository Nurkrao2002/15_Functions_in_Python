def fv(n1,n2):
    a=n1+n2
    b=n1-n2
    c=n1*n2
    d=n1/n2
    return a,b,c,d
x=float(input("Enter the value of x:"))
y=float(input("value of y:"))
Ar=fv(x,y)
print(Ar)
# print(*Ar)
# for i in Ar: print(i)