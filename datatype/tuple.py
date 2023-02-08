# tpl = (1,2,3,4,5,6,"sneha",1.3)
# print(tpl)
# print(type(tpl))
# tple = [1,2,3,4,5,6,5,"sneha",1.3]#list
# print(tuple(tple))#converted to tuple
# print(len(tpl))
# #nested tuple
# ntple = (1,2,3,4,5,6,("sneha",1.3))
# print(ntple)
# print(tpl[4])#indexed
# print(tpl[-2])#negative indexing
# print(tpl[1:3])#slicing
# print(tpl[:-5])#5 positions removed
# print(tpl[::-1])#reversing
# print(tpl[-4:-1])
#
#updation of tuple not directly possible
# tpl = (1,2,3,4,5,6,"sneha",1.3)
# y = list(tpl)#list is mutable so converted to list
# y[0] = "athira"
# print(y)#now its in list so again converted to tuple
# tpl = tuple(y)
# print(tpl)

# #append
# y = list(tpl)
# y.append("megha")
# tpl = tuple(y)
# print(tpl)
#
# #add another tuple in tuple
# tpl2 = ("ashik","aparna",9,0)
# tpl += tpl2
# print(tpl)
#
# #remove elements in tuple
# x = list(tpl)
# x.remove("aparna")
# tpl = tuple(x)
# print(tpl)
#del
# new_tple = (4,5,66,77,88)
# del new_tple
# print(new_tple)

#unpacking a tuple
fruits = ('apple','banana','cherry')
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)


