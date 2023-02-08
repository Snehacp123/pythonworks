# #while
# tupl = (1,2,3,4,5,6)
# i=0
# while i <= len(tupl):
#     print(i)
#     i=i+1
#
#
# #nested tuple
# n_tuple =("sneha",[1,2,3,4],[7,9.8,9])
# print(n_tuple)
# print(n_tuple[0][0])
# print(n_tuple[1][2])
# n_tuple[2][1]= 6
# print(n_tuple)
#
#count
# my_tuple = ('a','p','p','l','e')
# print('a' in my_tuple)
# print("total count of p is", my_tuple.count('p'))
# print("index of l is:", my_tuple.index('l'))

# #for loop
# names = ('sneha','aparna','athira')
# for name in names:
#     print("hello",name)

# built in functions with tuples
#-------------------------------
#1. all()
# tuple1 =("sneha",[1,2,3,4],[7,9.8,9],4,2.4,0,'sneha')#0 paadila
# x=all(tuple1)
# print(x)
# tuple2 = (1,2,3,4,5,6,6)
# x=all(tuple2)
# print(x)
# #2.any()
# tuple1 =("sneha",[1,2,3,4],[7,9.8,9],4,2.4,0,'sneha')
# x=any(tuple1)
# print(x)
# tuple2 = ()
# x=any(tuple2)
# print(x)
#3.len()
# tuple1 =("sneha",[1,2,3,4],[7,9.8,9],4,2.4,0,'sneha')
# x=len(tuple1)
# print(x)
#4.max() 5.min() 6.sum()
# tuple1 =(1,2,3,4,5,6,6)
# x=max(tuple1)
# print(x)
# y=min(tuple1)
# print(y)
# print(sum(tuple1))
#6. tuple()
# tuple1 = ["sneha",[1,2,3,4],[7,9.8,9]]
# print(type(tuple1))
# tuple2=tuple(tuple1)
# print(type(tuple2))
# #7.sorted()
# tuple1 =(7,5,4,8,3,2,9,0)
# x=sorted(tuple1)
# print(x)

#7.enumerate()
x = ('python','java','c++')
y = enumerate(x)
print(tuple(y))

name = ['sneha','ashik','athira']
no = [2,4,7]
x = zip(name,no)
print(tuple(x))#zip is used to map values

names = ('sneha','megha','harsha')
age =(23,25,21)
for i, (names ,age) in enumerate(zip(names, age)):
    print(i,names,age)

letters = [('a','A'),('b','B')]
for i ,letters in enumerate(letters):
    print("letters in %d is %s/%s" % (i,letters[0],letters[1]))

#8.map():it can listify the list of strings individualy

l =['sat','bat','cat','mat']
x = list(map(tuple,l))#we can change the data types.
print(x)