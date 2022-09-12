# a lambda function that returns even numbers from a list
# a = [2,7,4,1,8,13,16,19,21,24]
a=[int(x) for x in input().split()]
b = list(filter(lambda x: (x%2 == 0), a))
c = list(filter(lambda x: (x%2 != 0), a))
print(b)
print(c)