# oops
# example1
# class Emp:
#     x = 100
#     def display(self):
#         print("simple function")
#     def sum(self,a,b):
#         print("sum is",a+b)
#     def product(self,a,b):
#         print("product is",a*b)
#     # def disp():
#     #     print("without self parameter")
# obj = Emp()
# obj.display()
# obj.sum(23,45)
# obj.product(4,8)
# print("variable is",obj.x)
# # ob = Emp#function braket idaathe koduthal disp() workeeyum
# # ob.disp()

# example2
# class example:
#     def read(self,a,b):
#         self.x = a #a assigned to x and b assigned to y
#         self.y = b
#     def sum(self):
#         print("sum is ",self.x+self.y)
#     def product(c): #self nu pakaram eth variable koduthaalum ath self aaye kanakaakulu it is used to call current object using in the class
#         print("product is",c.x*c.y)
# obj =example()
# obj.read(30,60)
# obj.sum()
# obj.product()

# to find factorial of a number using class with arguments and return value
#
# class facto:
#     def fact(self,n):
#         f = 1
#         for i in range(1,n+1):
#             f = f*i
#         return f
# obj=facto()
# n = int(input("enter a number:"))
# f = obj.fact(n)
# print('factorial is:',f)

# another method using recursion
# class example:
#     def fact(self,x):
#         if x==1:
#             return 1
#         else:
#             return x*self.fact(x-1)
# obj = example()
# n = int(input("enter a number"))
# f=obj.fact(n)
# print('facorial is:',f)

#inheritance
# 1.single level inheritance
# class A:
#     def displayA(self):
#         print("base class method")
# class B(A):
#     def displayB(self):
#         print("derrived class method")
# obj = B()
# obj.displayA()
# obj.displayB()

# class A:
#     def read(self):
#         self.x = int(input("enter a number:"))
#         self.y = int(input("enter a number:"))
#
# class B(A):
#     def sum(self):
#         print("sum of a and b is:",self.x+self.y)
#
# obj = B()
# obj.read()
# obj.sum()

# 2.multilevel inheritance
# class A:
#     def read(self):
#         self.x = int(input("enter a number:"))
#         self.y = int(input("enter a number:"))
#
# class B(A):
#     def sum(self):
#         self.s = self.x+self.y
#         print("sum of a and b is:",self.s)
# class C(B):
#     def avg(self):
#         print("average is:",(self.s/2))
# obj = C()
# obj.read()
# obj.sum()
# obj.avg()
#
# # 3.hierarchical inheritance
# class A:
#     def read(self):
#         self.x = int(input("enter a number:"))
#         self.y = int(input("enter a number:"))
#
# class B(A):
#     def sum(self):
#         self.s = self.x+self.y
#         print("sum of a and b is:",self.s)
# class C(A):
#     def avg(self):
#         print("average is:",(self.x+self.y)/2)
# class D(A):
#     def product(self):
#         print("product is is:",self.x*self.y)
# ob1 = B()
# ob1.read()
# ob1.sum()
#
# ob2 = C()
# ob2.read()
# ob2.avg()
#
# ob3 = D()
# ob3.read()
# ob3.product()

# 4.multiple inheritance
# class A:
#     def readPersonalDetails(self):
#         self.name=input("enter the name:")
#         self.age = int(input("emter the age:"))
# class B:
#     def readSalaryDetails(self):
#         self.des=input("enter the designation:")
#         self.sal = int(input("enter the salary:"))
# class C(A,B):
#     def empDetails(self):
#         print('{}:{},{}:{},{}:{},{}:{}'.format('Name is',self.name,'Age is',self.age,'designation is',self.des,'salary is',self.sal))
# obj = C()
# obj.readPersonalDetails()
# obj.readSalaryDetails()
# obj.empDetails()

# 5.hybrid


# polymorphism

# one in many forms
# two types - function overloading , function overriding
#
# function overloading:same class
# class A:
#     def display(self,name=None):
#         if name is None:
#             print('hello')
#         else:
#             print('hello '+name)
# ob = A()
# ob.display()
# ob.display('sneha')

# FUNCTION OVERRIDING : different class

class rectangle:
    def Area(self,l,b):
        print('area of a rectangle:',l*b)
class square(rectangle):
    def Area(self,l,b):
        print('area of square:',l*b)
ob = square()
ob.Area(30,20)

# ABSTRACTION
from abc import ABC,abstractmethod
# abstract class
# class polygon(ABC):
#     #abstract method
#     @abstractmethod
#     def sides(self):
#         pass
#     def display(self):
#         print("non abstract method")
# class triangle(polygon):
#     def sides(self):
#         print("triangle has 3 sides")
# t = triangle()
# t.sides()
# t.display()

# CONSTRUCTOR
# two types - non parameterized constructor , parameterized constructor
# non parameterized constructor

# class A:
#     def __init__(self):
#         print('non parameterized constructor')
# ob =A()

#parameterized constructor
class A:
    def __init__(self,name):
        print('parameterized constructor')
        self.na = name
    # def __del__(self):
    #      print('destructors')
    def display(self):
        print('Name is:',self.na)
ob =A('Aashi')
# del ob
ob.display()


