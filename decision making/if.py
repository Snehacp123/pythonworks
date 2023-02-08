#calculator
choice = input("enter the choice: +,-,*,/")
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the  third number:"))
if choice== '+':
    print("sum is",a+b+c)
elif choice== '-':
    print("difference is",a-b)
elif choice== '*':
    print("multiplication is",a*b)
elif choice== '/':
    print("division is",a/b)
else:
    print("invalid")


#nested if
a=5
if a < 10:
    print("not above ten")
    if a>20:
        print("above twenty")
    else:
        print("not above twenty")
else:
    print("invalid")

