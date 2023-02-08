str1 = "hello"
str2 = "there"
new_str1 = str1 + str2
print(new_str1)
new_str2 = str1+' '+str2
print(new_str2)
str3 = 4
new_str3 = str1+ ' '+str(str3)
print(new_str3)
# #also we can use () to cocatinate numbers
new_str4 = int(str3) + 3
print(new_str4)
print(len(new_str1))

# #string formatting
#
name ='sneha'
age =23
print("%s is %d years old" %(name, age))
print("{} is {} years old".format(name,age))
print(f'{name} is {age} years old')

bag =3
apples_in_bag =12
print(f'there are total of {bag * apples_in_bag} apples')
#
# val1 = 4
# val2 = 6
# print(f'the sum of two valuse is {val1 * val2}')