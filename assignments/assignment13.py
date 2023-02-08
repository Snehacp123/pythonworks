#1.multiply all the numbers in a list
ls=[1,3,5]
def multi(ls):
    mul = 1
    for i in ls:
        mul = mul*i
    print("multiplication of elements in a list:",mul)
multi(ls)

#2.reverse a string

a = "sneha90"
def rev(a):
    reve = a[::-1]
    print("before reverse of a string is", a)
    print("reverse of a string is",reve)
rev(a)

#3.factorial numbers
def fact(n):
    if n ==0:
        return 1
    else:
        return n * fact(n-1)
n = int(input("enter a number:"))
print(fact(n))

#4.prime numbers
n = int(input("enter a number"))
def prime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                print(n,"not prime")
                break
        else:
            print(n,"prime")
    else:
        print("not prime number")
prime(n)

#5 add using 2 functions
def outeradd(a,b):
    def inneradd(a,b):
        return a+b
    return(inneradd(a,b)+5)
print(outeradd(2,3))

#6. even numbers

def even(a,b):
    x = []
    for i in range(a,b,2):
        x.append(i)
    return x
print(even(2,20))
