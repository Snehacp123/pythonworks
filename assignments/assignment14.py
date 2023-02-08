#1.square of numbers
# def sqrvalues():
#     ls = []
#     for i in range(1,31):
#         ls.append(i**2)
#     print(ls)
# sqrvalues()
#
# #2.assign new name to the function
#
# def function1():
#     print("iam sneha")
# # function1()
#
# newfunction = function1
# newfunction()
#
# #3.accept two numbers
# def sum(a,b):
#     print("sum of",a,"and",b, "is" ,a+b)
# sum(12,90)

# #4.accepts different values as parameters and return a list
#
def details():
    name = "sneha"
    age = 22
    course ="python"
    return[name,age,course]
values = details()
print(values)
#
# #5.accept values as parameters and return a tuple
# def details():
#     name = "sneha"
#     age = 22
#     course ="python"
#     return(name,age,course)
# values = details()
# print(values)

#6.accept 2 values and return its sum,sustracion and multiplication

# def values(a,b):
#     print("addition of a and b is",a+b)
#     print("subtraction of a and b is",a-b)
#     print("multiplication of a and b is", a * b)
#     return a,b
# n1 = int(input("enter a number"))
# n2 = int(input("enter another number"))
# values(n1,n2)

#7.PRESENT OR ABSENT
# def students(rollno):
#     i = [1,2,3,4,5,6,7,8,9]
#     if rollno in i:
#             print("present")
#     else:
#             print("absent")
# rollno = int(input("enter a roll no"))
# students(rollno)

#8.vowels and consonent

# def count(val):
#     vow = 0
#     con = 0
#     for i in range(len(val)):
#         if val[i] in ['a','e','i','o','u']:
#             vow =vow+1
#         else:
#             con = con+1
#     print("count of vowels:",vow)
#     print("count of consonent:",con)
# x=input("enter the string")
# count(x)
#
# # #even or odd
# def num(n):
#     if n%2 == 0:
#         print("num is even")
#     else:
#         print("num is odd")
# x = int(input("enter a number"))
# num(x)
#
# #three numbers
#
# def max(a,b,c):
#     if a>b and a>c:
#         print("a is max num")
#     elif b>a and b>c:
#         print("b is max num")
#     else:
#         print("c is max num")
# max(34,89,67)


def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a+b
    return add
func = test(4)
print(func(8))

