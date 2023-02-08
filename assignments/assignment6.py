#1.right angled patteern with character

# row = int(input("enter the rows"))
# k = 1
# ch = chr(64+k)
# for i in range(0,row+1):
#     for j in range(i):
#         print(ch,end=" ")
#         k += 1
#         ch = chr(64+k)
#     print()

#2.try to create diamond pattern

# n = int(input("enter the level"))
# for i in range(n+1):
#     for j in range(n-i):
#         print(" ", end = " ")
#     for j in range(i):
#         print("  *", end=" ")
#     print()
# for i in range (n+1,0,-1):
#     for j in range (n-i+1):
#         print(" ", end = " ")
#     for j in range (i):
#         print("*  ", end=" ")
#     print()

#3.try to create below designed pattern

# num = int(input("enter the rows"))
# for i in range(num):
#     for s in range(i):
#         print(" ",end ='')
#     for j in range(num-i):
#         print("* ",end="")
#     print()
# for i in range(num):
#     for s in range(num-i-1):
#         print(" ",end ='')
#     for j in range(i+1):
#         print("* ",end="")
#     print()

#4.try to create inverted full pyrammid pattern

# num = int(input("enter the rows"))
# for i in range(num):
#     for s in range(i):
#         print(" ",end ='')
#     for j in range(num-i):
#         print("* ",end="")
#     print()

#5.try to create hollow diamond pattern
# num = int(input("enter the rows"))
# for i in range(num):
#     print("   "*(num-i)+"*",end=' ')
#     if i != 0 :
#         print("   "*(2*i)+"*",end=" ")
#     print()
# for i in range(num,-1,-1):
#     print("   "*(num-i)+"*",end=' ')
#     if i != 0 :
#         print("   "*(2*i)+"*",end=" ")
#     print()

#6.odd patterns

# n = int(input("enter the rows:"))
# for count in range(n+1):
#     num = 2*count-1
# for i in range (num+1):
#     if i%2!=0:
#         for j in range(num-i):
#             print(' ', end = ' ')
#         for j in range(i):
#                 print('*  ', end=' ')
#         print()

#7.reverse pattern from 10 to 1

# levels = int(input("enter the rows"))
# for i in range(levels + 1,0,-1):
#      for j in range(i-1,0,-1):
#          print(j, end="   ")
#      print()

#8.hollow sqr using characters
# n = 5
# for i in range (1,n+1) :
#     for j in range (1,n+1) :
#         ch = chr(64 + i)
#
#         if (i==1 or i==n or j==1 or j==n):
#             print(ch, end=" ")
#         else:
#             print(' ', end=" ")
#         print(' ')
#
