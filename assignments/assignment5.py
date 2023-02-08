# #full pyramid with *s
# print("full pattern pyramid with stars")
# n = int(input("enter your number"))
# for i in range(n): #row
#     for s in range(n-i-1):#space 5-0-1
#         print(" ",end="")#print 4 space
#     for j in range(i+1):
#         print("* ", end="")#column
#     print()

#print("reverse pattern 10-1")
# n = int(input("enter the number"))
# for i in range(0,n):
#     for j in range(n-i,0,-1):
#         print(" *",end=' ')
#     print()
#
#half pyramid using no:s
r = int(input("enter no of rows"))
for i in range(1,r+1):
    #print(i)
    for j in range(i):
        #print(j)
        print(j+1,end = " ")
    print()


