# def makepretty(func):
#     def inner():
#         print("i got decorated")
#         func()
#     return inner()
#
# @makepretty
# def ordinary():
#     print("am ordinary")
# ordinary()

# def upper_decor(fun):
#     def wrapper():
#         result = fun()
#         return result.upper()
#     return wrapper()
# def hello_name():
#     return "hello"
# f = upper_decor(hello_name)
# print(f)

def upper_decor(fun):
    def wrapper(name):
        result = fun(name)
        return result.upper()
    return wrapper

@upper_decor
def hello_name(name):
    return "hello" + name
# f = upper_decor(hello_name)
print(hello_name(" arya"))

