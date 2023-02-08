# f=open('test1','r')
# print(f.read())

# print(f.read(8))#8 position read cheyyum start value 0 aavum

# print(f.readline())# line by line aayi read cheyyum
# print(f.readline())#second line read cheyyum

# for i in f:
#     print(i)#for loop vech file readeeyam line by line aayirikkum
# f.close()
"""
# append()
f=open('test1','a')
f.write("python is oop")
f.close()
"""

# f = open('test1','r')
# for i in f:
#     print(i)
# f.close()

#write()

# f = open('test1','w')
# f.write("python follows oop concept")
# f.close()
# f = open('test1','r')
# for i in f:
#     print(i)
# f.close()

#seek()
# f = open('test1','r')
# f.seek(8)
# print(f.readlines())
# f.close()

# tell()
# f = open('test1','r')
# f.readline()
# pos = f.tell()
# f.close()
# print("the position is:",pos)

# write a program to read a file line by line and store it into a list

# def file_read(fna):
#     with open(fna) as f:   #instead of write this 'f=open('test1','r')'.
#         output_list = f.readlines()
#     print(output_list)
# file_read('test1')

# from shutil import copyfile
# copyfile('test1','test2')


# print(str)
# lst = str.split(' ')
# print(lst)
# d = {}
# for i in lst:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i] = 1
# print(d)

f = open('test1','r')
dic = {}
for i in f:
    var = i.split(' ')
    for j in var:
        if j not in dic:
            dic[j] = 1
        else:
            dic[j]+=1
print(dic)

















