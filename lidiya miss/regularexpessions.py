# regular expression
# mainly 4 methods
# 1. findall()

import re
# str = 'rose is a beautiful and colourful flower'
# s = re.findall('ful',str)
# print(s)
# s = re.findall('full',str)
# print(s)
# d = 'cat mat pat rat sat'
# a = re.findall('[scr]',d)
# print(a)
# a = re.findall('[scr]at',d)
# print(a)
# a = re.findall('[^scr]',d)
# print(a)
# d = 'cat mat pat rat sat 99988 9999 6666 44'
# a = re.findall('\d{3}',d)
# print(a)
# a = re.findall('\d{1,4}',d)
# print(a)
# a = re.findall(r'\b\d{4}\b',d)#4 digitum vennam frontilum backilum spaceum vennam
# print(a)

# 2.search()

# str = 'class will start at 10 am'
# s1 = re.search('\s',str)
# print(s1)
# print(s1.start())
# s2 = re.search('\d',str)
# print(s2)
# print(s2.start())
# s3 = re.search('sneha',str)
# print(s3)
# print(s3.start())

# str = 'class will start at 10am'
# s = re.search('^class.*10am$',str)
# print(s)
# if s:
#     print('find')
# else:
#     print('not find')

# 3.split()
# str = 'class will start at 10am'
# s = re.split(' ',str)
# print(s)
#
# s = re.split('a',str)
# print(s)
# s = re.split(' ',str,2)
# print(s)

# str = "python is a lang"
# s = re.fullmatch(str,"python is a lang")
# print(s)
# str = "python is a lang"
# s = re.match(str,"python is alang")
# print(s)

# sub()

# input = "rose and jasmines are flowers"
# s = re.sub(' ','*',input)
# print(s)
#
# g = re.sub(' ','*',input,3)
# print(g)

# regular expression using validation

import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")
check('mohangmail.com')