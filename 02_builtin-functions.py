''' Pre-Defined Functions '''

'''   sorted()  '''
# a=[1,6,3,8,2]
# a.sort()
# print(a)
# print(sorted([12,3,120,9]))
# print(sorted((12,3,4,56)))
# a=['a','A','Z','z']
# print(sorted(a))
# print(ord('A'))
# print(chr(90))

'''  all()  '''
# print(all([True,1,2]))   
# print(all([True,'',1,2]))   
# print(all([True,' ',1,2]))   
# print(all([True,False,1,2])) 
# print(all([True,True,1,2,0])) 
# print(all([True,True,1,2,None])) 
# print(all((True,True,1,2,None))) 

'''  any() '''
# print(any([True,False,False,0,23])) 
# print(any([False,False,'']))     
# print(any([True,True,None,0]))  

'''   bool()  '''
# print(bool(False))
# print(bool(1))
# print(bool(0))
# print(bool(None))
# print(bool('bool'))
# print(bool(''))
# print(bool(' '))

'''  eval() '''
# print('eval=',eval("5+6.8-1"))
# a=eval('5+6-1')
# b=eval('4+3.8-1')
# print(a,type(a))
# print(b,type(b))

'''  sum() '''
# print('sum=',sum([1,2,3,4,5]))
# print('sum=',sum((10.5,20,30)))


'''  reversed()-list  '''
# for i in reversed([1,2,3,4]):
#     print (i)

'''  reversed()-tuple  '''
# for i in reversed((10,20,30,40)):
#     print (i)

'''  enumerate()  '''
# a=['bread','milk','python']
# b=enumerate(a)
# print(type(b))
# print(dict(b))
# print(list(b))
# print(tuple(b))


# a=['bread','milk','python']
# c=enumerate(a,-1)
# print(list(c))