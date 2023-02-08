# def mul(x):
#     num = 1
#     for i in x:
#         print(i)
#         num = num * i
#     return (num)
# j = [2,3,4]
# print(mul(j))
# ___________________________________________
# nested functions

# def inner(x,y):
#     sum = x + y
#     print(sum)
#     def outer(z):
#         return z+a
#     p = outer(sum)
#     print(p)
# d = int(input('d:'))
# e = int(input('e:'))
# a = int(input('a:'))
# inner(d,e)

def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_15 = create_adder(15)
print(add_15(10))






