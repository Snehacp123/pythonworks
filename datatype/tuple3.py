 # 1 .reverse a tuple
# tpl = (78,23,4,5,87,2)
# print(tpl[::-1])

#2.to remove repeated elements from the tuple

tple2 = (1,2,40,[10,2,30],(30,20,10),40,1,2)
a = []
for i in tple2:
    if i not in a:
        a.append(i)
print(tuple(a))

# 3.to access the value 20 from the tuple


# 3 .check if all the items in the tuple are same
# 4 .copy specific elements from one tuple to a new tuple
# 5 .swap two tuples in python