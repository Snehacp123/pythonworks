"""
functions
_________
oops programs are based on class and objects
 class : class is the way to bind functions and its related datas
 object : instance of a class or runtime entity of a class.
 function : repeated group of statements/we can create a function for a particular task.
   .mainly two parts - function definition and function calling
   .return value : we can pass onlu one value from function definition to function calling is called return value.
   .function parameters: we can pass more than one values from functon calling to function definition are called function parameters.

"""
# def sum():
#     a,b = 10,20
#     s = a+b
#     return s
# s1 = sum()
# print('sum is:',s1)
# print('sum is:',sum())

# with parameters
# def sum(x,y):
#     s = x+y
#     return s
# print('sum is:',sum(34,12))

# prgrm to find factorial of a number using functions with returntype and function parameters

# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i
#     return f
# f = fact(5)
# print('fact is',f)
# #
"""
function parameters
   .simple  
   .arbitary 
   .keyword 
   .default 
   .parameter value 
   .list
"""
# arbitary
# def color(*args):
#     print(args[2])
#     for i in args:
#         print(i)
# color('red','white','blue')
# #
# #
# def color(x,*r):
#     print('normal argument',x)
#     for i in r:
#         print(i)
# color('red','white','blue','black')
 # keyword argument
# def stud(st1,st2,st3):
#     print('first:',st1)
#     print('second:', st2)
#     print('third:', st3)
# stud('anu','ashik','athira')
# stud(st2='anu',st1='athira',st3='ashik')#keyword argument

# def student(x,*args,**kwargs):
#     print('simple argument:',x)
#     for j in args:
#         print(j)
#     for i,j in kwargs.items():
#         print('%s=%s'%(i,j))
# student('amal','varun','sini',st2='anu',st1='athira',st3='ashik')

# default parameter value
# def display(country = 'india'):
#     print('iam from',country)
# display()
# display('america')
#
# # list
# def dis(ls):
#     for i in ls:
#         print(i)
# dis([10,20,30])
# print()

l1 = []
def create():
  for i in range(int(input('enter the number of elements in the list:'))):
    item = int(input('enter the item:'))
    l1.append(item)
  print(l1)
def search():
    num = int(input('enter a number to be searched:'))
    if num in l1 :
        print(num,"found in list")
    else:
        print(num,"not found in list")
def Remove():
    num1 = int(input('enter a number to be removed:'))
    if num1 in l1:
        l1.remove(num1)
    else:
        print('item not found in list')
    print(l1)
def Replace():
    old = int(input('enter a item to be replaced:'))
    new = int(input('enter a new item replaced:'))
    for i in range(len(l1)):
        if l1[i]==old:
            l1[i]=new
    print(l1)
while True:
    opt = int(input("1.create\n2.search\n3.remove\n4.replace\nenter your choice:"))
    if opt == 1:
        create()
    elif opt == 2:
        search()
    elif opt == Remove():
        Remove()
    elif opt == Replace():
        Replace()
    else:
        break
#
create()
search()
Remove()
Replace()

# recurssion
def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
f =  factorial(5)
print("factorial of 5 is",f)

# 5*4 ---5*24
# 4*3 ---4*6
# 3*2 ---3*2
# 2*1---2*1















