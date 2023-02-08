# 1.print all unique values in a dictionary
# listofdict = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VII":"S007"}]
# setofuvalues =set()
# for i in listofdict:
#     for value in i.values():#
#         setofuvalues.add(value)
# print(setofuvalues)

# 2.combine values in puthon list of dictionaries

# listofdict =[{'item':'item1','amount':400},{'item':'item2','amount':500}]
# #print("the given dictionary is :",listofdict)
# newdict = {}
# list1 =[]
# for d in listofdict:
#     #print(d)
#     p = list(d.values())#create list of values
#     list1.append(p[0])
#     list1.append(p[1])
# #print(list1)
# for i in range(0,len(list1),2):
#     if list1[i] in newdict:
#         rep =list1[i]
#         print(rep)
#         index = list1.index(rep)
#         list1[index+1] = list1[index+1] + list1[i+1]
#         #print(list[i+1])
#         newdict[list1[i]] = list1[index +1]
#     else:
#         mewdict.setdefault(list1[i],list1[i+1])
# print("the combined dictionary is:",newdict)

# 3.create a dictionary from a string
"""setdefault():
   -----------
if key is in the dictionary ,return its value.
if not ,insert key with a value of default and return default.
default defaults name.
"""

# str1 = 'luminar'
# print("the given string is ",str1)
# dict1 = {}
# for index in range(1,len(str1)+1):
#     dict1.setdefault(index,str1[index-1])#dict1.update({iindex:str1[index-1]}) or dict1[index] = dict1[index-1]
#    #print(str1[index - 1])
# print("the corresponding dictionary of the given string is:",dict1)

#4.print dictionary as a table
# dict1 = {"maths":87,"science":90,"english":95,"malayalam":100}
# print("subject\t\t\t\t\t marks\n*********************")
# for key,value in dict1.items():
#     if key =="maths":
#         print(key,"\t\t\t\t\t",value)
#     else:
#         print(key, "\t\t\t\t", value)

# 5.print a dictionary in line by line

# dict1 = {"maths":87,"science":90,"english":95,"malayalam":100}
# name = "sneha"
# print("student name is",name)
# for key,value in dict1.items():
#     print("the student scored",value,"marks in subject",key)

#6.sort(ascending,descending)a dictionary by value.

# dict1 = {1:2, 3:4, 4:3, 2:1, 0:0}
# ascDict = {}
# dscDict = {}
# val = []
# val1 =[]
# key =[]
# val = list(dict1.values())
# val1 = list(dict1.values())
# val.sort()
# print(val)
# val1.sort(reverse=True)
# print(val1)
# key = list(dict1.keys())
# for i in val:
#     index = list(dict1.values()).index(i)
#     ascDict[key[index]] = i
# for i in val1:
#     index = list(dict1.values()).index(i)
#     dscDict[key[index]]=i
# print("Ascending dictionary",ascDict.items(),"\n Descending dictionary",dscDict)

#7.concatinate two dictionaries to create new one
dict1 = {"Name":'Jyothis', "Age":22, "Place":"Kottarakara"}
dict2 = {"Institution":"Luminar Technolab","Qualification": "B.Tech"}

print("The first dicitionary is : ",dict1)
print("The second dicitionary is : ",dict2,"\n")

dict1.update(dict2)
print("The concantenated dictionary is : ",dict1)

#8.combine another method
d =[{'item':'item1','amount':400},
    {'item':'item2','amount':300},
    {'item':'item3','amount':750}]
lst = {}
for i in d:
    if i['item'] not in lst:
        lst[i['item']] = i['amount']
    else:
        lst[i['item']]+=i['amount']
print(lst)