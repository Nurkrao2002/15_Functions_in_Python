#lambda that returns squares
# list1 = [1, 2, 3, 4, 5]
list1=[int(x) for x in input().split()]
list2 = list(map(lambda x: x**2, list1))
print(list2)