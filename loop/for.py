#name = 'sneha'
#for i in name:
 #   print(i)

# for i in range(1,6):
#     print(i)

#multiplication table
# list1 = [1,2,3,4,5,6]
# n = 6
# for i in list1:
#     c = i * n
#     print(c)
#or
n = int(input("enter the number:"))
for i in range(1,11):
    c = i * n
    print(i,"*",n,"=",c)

# #sum of 10 numbers
# list1 = [1,2,3,4,5,6]
# sum =0
# for i in list1:
#  sum = sum + i
# print("sum is",sum)
#
# #even numbers
# for i in range(0,30,2):
#     print(i)
#
# for i in range(10):
#     print(i)
#
#
#

"""rows = int(input("enter the rows"))
for i in range(1,rows+1):#row
    print(i)
    for j in range(i):  #column
      print(j)
"""
"""

n = int(input("enther the rows"))
for i in range(n+1,0,-1): #row
    for j in range(i-1):  #column
        print("*",end="")
    print()
"""