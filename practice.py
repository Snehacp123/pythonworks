str1 = input("enter first string")
str2 = input("enter second string")
new_str = ' '
for i in range(len(str1)):
    if i == len(str1)//2 :
        new_str = new_str + str1[i] + str2
    else:
        new_str = new_str+str1[i]
print(new_str)
