#convert string to tuple
str1 = "luminar"
tple = tuple(str1)
print(tple)

#convert list to tuple
lst = ['sneha',7.8,9,10,9,10]
tple1 = tuple(lst)
print(tple1)

#find repeated items from a tuple
tpl = (1,3,5,3,5,7,8,9,1,1,)
n = int(input("enter the value :"))
count = tpl.count(n)
print(count)