# row = int(input("enter the rows:"))
# for i in range(0,row+1):#range 1 il starteeyam appo aadhyame ulla space kurayum ,2 vil starteethal ** vechaayirikkum starteeya.
#      for j in range(i): # i yil koduthitula numbernte star printeeyipikaaan for eg i yil 2 aanel ** printeeyum .
#          print("*",end=" ")#starinte edel space verum endinte ullil space koduthaal,star nu pakaram i koduthaal numbers printeeyum
#      print()

#reverse pyrammid
row = int(input("enter the rows:"))
for i in range(row+1,0):
    for j in range(i):
       print("*",end=" ")
       print()