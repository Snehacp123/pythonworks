try:
    n1 = int(input("enter first number:"))
    n2 = int(input("enter second   number:"))
    n3 = n1/n2
    print("output is :",n3)
# except ZeroDivisionError as er:
#     print(er)
# except ValueError as er:
#     print(er)

# if we dont what is  the eerror so we can just write exception
except Exception as ex:
    print(ex)