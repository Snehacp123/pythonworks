#concatinating a string to the middle of another

str1 = input("enter the first string")
str2 = input("enter the second string")
newstr1 = ''
for i in range (len(str1)):
    if i == (len(str1))//2:
        newstr1 = newstr1 + str1[i] + str2
    else:
        newstr1 = newstr1 + str1[i]
print(newstr1)