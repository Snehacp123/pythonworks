# def getsum():
#     if num == 1:
#         return 1
#     # print(num + getsum(num - 5
#     #  1))
#     return num + getsum(num - 1)
#
# num = 10
# print(getsum(num))

# def tri_recursion(k):
#     if(k>0):
#         result = k + tri_recursion(k-1)
#         print(result)
#         # print(tri_recursion(k-1))
#     else:
#         result = 0
#     return result
# print("recursion example result")
# tri_recursion(6)

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
n = int(input("enter a number:"))
print(f'factorial of {n} is {fact(n)}')