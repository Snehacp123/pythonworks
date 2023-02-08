#leap year or not

year = int(input("enter a year:"))
#divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0)and(year%100==0):
    print(year,"is leap year")
elif(year % 4 == 0) and (year % 100 != 0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#check whether a character is a vowel or consonant
# a e i o u , A E I O U
# ch = input("enter a character:")
# if (ch == 'A' or ch =='a' or ch == 'E' or ch == 'e' or ch =='I' or ch == 'i' or ch == 'O' or ch =='o' or ch == 'U 'or ch == 'u'):
#     print(ch,"is vowel")
# else:
#     print(ch,"is consonant")
#OR
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# str1 = input("enter a string")
# for i in str1:
#     if i in vowels:
#         print(f'{i} is vowel)
#     else:
#         print(f'{i} is consonant)
#
#armstrong number
num = int(input("enter a number"))
sum = 0
temp = num
while temp > 0:
    r = temp % 10
    sum += r*r*r
    temp =temp//10
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num, "is not an armstrong number")