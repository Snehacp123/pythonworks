# #prgrm without lambda functn
# def sum(a,b):
#     return a+b
# print(sum(10,20))
#
# # lambda function
# # syntax : lambda arguments:expression
#
# add = lambda a,b:a+b
# print(add(3,4))
#
# # lambda with if function
# largest = lambda a,b:a if a>b else b
# print(largest(300,800))
#
# # methods of lambda
# # 1.filter 2.map 3.reduce
# # filter
# l = [10,2,3,4,50,40]
# lst = list(filter(lambda x:x%2 == 0,l))
# print(lst)
# # # map
# l = [10,2,3,4,50,40]
# lst1 = list(map(lambda x:x%2 == 0,l))
# print(lst1)
# l = [10,2,3,4,50,40]
# lst2= list(map(lambda x:x*2,l))
# print(lst2)
# # # reduce
# from functools import reduce
# l1 = [1,2,4,6,5]
# product = reduce(lambda x,y:x*y,l1)
# print(product)

# list compehension
# syntax : [expression for item in list if condition]

# l = [x+3 for x in [2,3,4]]
# print(l)

# l = [i for i in range(25) if i%2 == 0]
# print(l)
#
# v = [i for i in 'hai how are you?' if i in ['a','e','i','o','u']]
# print(v)

str ='hai how are you'
words = str.split(' ')
print(words)
firstletter = [i[0] for i in words]
print(firstletter)

colors = ['red','white','pink','green']
clr = [i for i in colors if 'e' in i]
print(clr)

colors = ['red','white','pink','green']
clr = [i for i in colors if i!= 'green']
print(clr)

colors = ['red','white','pink','green']
clr = [i.upper() for i in colors ]
print(clr)

colors = ['red','white','pink','green']
newlist = ['hello' for i in colors]
print(newlist)

 # if else

colors = ['red','white','pink','green']
newlist = [i if i!='pink' else 'blue' for i in colors]
print(newlist)

# dictionary comprehension
words = 'hai how are you'
ans = {i : len(i) for i in words}# set do not allow duplicate values
print(ans)