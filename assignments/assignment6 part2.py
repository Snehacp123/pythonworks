#9.heart pyrammid

# num =int(input("enter a number:"))
# n = num // 2
# for i in range(2,n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("* ", end="")
#     if num%2 ==0:
#        for j in range(2*(n-i-1)):
#            print(" ",end="")
#        for j in range(i + 1):
#            print("* ", end="")
#        print()
# #lower part
# for i in range(num,0,-1):
#     print(" "*(num-i)+"*"*(2*i-1))

#or

num = int(input("enter a number"))
half = round(num/2)
for i in range(2,half):
    print(" "*(half-i-1)+"*"*(2*i-1)+" "*(half-i)+"*"*(2*i+1))
for i in range(num,0,-1):
    print(" "*(num-i)+"*"*(2*i-1))
