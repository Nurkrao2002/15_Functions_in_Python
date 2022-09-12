# positional arguments demo
def attach(s1,s2):
    s3=s1+s2
    print('total string: '+s3)
attach('New', 'York')
s1,s2=[x for x in input().split(',')]
attach(s1,s2)
