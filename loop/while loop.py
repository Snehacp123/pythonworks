#i = 1
#while i <= 10:
 #   print(i)
#i=i+1

# i=1
# number =0
# b=9
# number = int(input("enter the number:"))
# while i<=10:
#     print("%dX%d=%d\n"%(number,i,number*i))
#     i = i+1

#sum of n natural numbers

# num = int(input("enter the number"))
# sum = 0
# i = 0
# while i <= num:
#     sum = sum + i
#     i = i + 1
# print(sum)

#fibinocci numbers

num = int(input("entern the number"))
count = 0
n1 = 0
n2 = 1
while n1<=num:
    count = n1 + n2
    n1 = n2
    n2 = count
    print(n1)

#factorial of a number
num = int(input("enter a number"))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i = i + 1
print("factorial of %d is %d"%(num,fact))

