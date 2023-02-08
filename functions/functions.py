def sample():
    print("hi dears")

sample()  #function calling

#2.sum()
def sum():
     a = 10
     b = 30
     c = a + b
     return c
print("the sum is",sum())#function calling along with print

#3.with arguments
def func(name):
    print("hi",name)
func("sneha")

#type of arguments
#1.arbitery arguments

def func(*name):
    print("hi",name)
func("sneha","ashik")
func("athira")

#2.keyword arguments
def func(child1,child2,child3):
    print("the youngest child is",child3)
func(child1="sneha",child2="ashik",child3="athira")


#3.arbitary keyword arguments
def func(**kid):
    print("his last name is "+kid["lname"])
func(fname="sneha",lname="mohan")

#4.default arguments
def func(country="india"):
    print("am from "+country)
func("argentina")
func()
func("brazil")

