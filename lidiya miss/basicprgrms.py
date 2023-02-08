# # python allows multiple values assigned to multile variables so we can easly swap values to each other
# a,b = int(input('enter first number:')),int(input('enter second number:'))
# a,b = b,a
# print('a=',a)
# print('b=',b)
#
# # another method to swap variales without using third variable
# a,b = int(input('enter first number:')),int(input('enter second number:'))
# a = a+b
# b = a-b
# a = a-b
# print('a=',a)
# print('b=',b)

# to check whether the given number is +ve ,-ve or zero

# num = int(input("enter a number:"))
# if num > 0:
#     print(num,"is +ve ")
# elif num < 0:
#     print("the number is -ve")
# else:
#     print("the number is zero")

#largest of three number is nested if

# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# c = int(input("enter a number:"))
# if a>b :
#     if a>c :
#         print(a," is largest number")
#     else:
#         print(c," is largest number")
# elif b>c :
#         print(b," is largest number")
# else:
#     print(c,"is largest number")

# reverse ,product ,sum of anumber using while
# n = 1234
# rev = 0
# p=1
# s=0
# while n > 0:#12>0,1>0
#     r = n%10#3,2,1
#     rev = rev*10 + r#3,32,321
#     p = p*r
#     s = s+r
#     n = n // 10#12,1
# print("reverse is:",rev)
# print("product is:", p)
# print("sum is:",s)

# simple for loop
# for i in 'python':
#     print(i)
#
# # for loop with range
# # for i in range(start,stop,increment)
#
# for i in range(2,10):
#     print(i)

# print fibonocci series using for loop
# a = int(input("enter a range:"))
# f = 0
# s = 1
# for i in range(0,a):
#     if i<=1:
#         temp = i
#     else:
#         temp = f + s
#         f = s
#         s = temp
#     print(temp)

# prime numbers
# n = int(input('enter the number:'))
# f = 0
# if n <= 1:
#     print('not defined')
# else:
#     for i in range(1,n+1):
#         if n%i == 0:
#             f = f + 1
#     if f == 2:
#         print(n,'is a prime number')
#     else:
#         print(n,'is not a prime number')

# else in for loop
# for i in 'python':
#     print(i)
# else:
#     print("completed")

# break statement
# l = [10,20,30,40,100,50,60,70]
# for i in l:
#     print(i)
#     if i == 100:
#         break
# continue statement
# l = [10,20,30,40,100,50,60,70]
# for i in l:
#     if i == 100:
#         continue
#     print(i)

# list
# l1 = [12,34,56,34,32]
# l2 = [60,70,80,90]
# l1.append(l2)
# print(l1)
# l3 = [12,34,56,32]
# l4 = [60,70,80,90]
# l3.extend(l4)
# print(l3)
# del l3[1]
# print(l3)
# l3.sort()
# print(l3)
# l3.sort(reverse=True)
# print(l3)

# l1 = []
# for i in range(int(input('enter the number of elements in the list:'))):
#     item = int(input('enter the item:'))
#     l1.append(item)
# print(l1)

# dictionary
# d = {}
# num = int(input("enter the number:"))
# for i in range(num):
#     key = int(input("enter the key:"))
#     value = int(input("enter the value:"))
#     d.update({key:value})
# print(d)

# d = {1:'red',2:'yellow'}
# for i in d.keys():
#     print(i)
#
# for i in d.values():
#     print(i)
# for i,j in d.items():
#     print(i,j)
# x = d.get(2)
# print(x)

# tuple
# t = (100,200,300)
# print(t)
# print(t[2])

# set

# s = {10,20,30,40,10,20}
# print(s)
# for i in s:
#     print(i)







