#global scope

# x = 100
# def func():
#     print(x)
# func()
#
# #local scope
#
# def funct():
#     x = 300
#     print(x)
# funct()

def programming():

    def python():
        name = "sneha"

    def mean_stack():
        nonlocal name
        name = "aiswarya"

    def flutter():
        global name
        name = "megha"

    name = "harsha"

    python()
    print("coder is",name)
    mean_stack()
    flutter()

programming()
print(name)
