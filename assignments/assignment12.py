#check that items of a tuple are same or not
tup = (8,9,76)
f = 1
for i in tup:
    for j in range(i,len(tup)-1):
        if tup[i] != tup[j+1]:
            f = 0
            break
if f == 1:
    print("same")
else:
    print("not same")

#another method

# tupl = (9,3,7)
# tupl = set(tupl)
# if len(tupl) == 1:
#     print("same")
# else:
#     print("not same")