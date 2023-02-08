l1 = []
def create():
  for i in range(int(input('enter the number of elements in the list:'))):
    item = int(input('enter the item:'))
    l1.append(item)
  print(l1)
def search():
    num = int(input('enter a number to be searched:'))
    if num in l1 :
        print(num,"found in list")
    else:
        print(num,"not found in list")
def Remove():
    num1 = int(input('enter a number to be removed:'))
    if num1 in l1:
        l1.remove(num1)
    else:
        print('item not found in list')
    print(l1)
def Replace():
    old = int(input('enter a item to be replaced:'))
    new = int(input('enter a new item replaced:'))
    for i in range(len(l1)):
        if l1[i]==old:
            l1[i]=new
    print(l1)
# while True:
#     opt = int(input("1.create\n2.search\n3.remove\n4.replace\nenter your choice:"))
#     if opt == 1:
#         create()
#     elif opt == 2:
#         search()
#     elif opt == Remove():
#         Remove()
#     elif opt == Replace():
#         Replace()
#     else:
#         break

# create()
# search()
# Remove()
# Replace()














