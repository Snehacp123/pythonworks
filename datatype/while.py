#while loop

fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index + 1

#for loop
fruit = 'banana'
for i in fruit:
    print(i)
#searchin a string

fruit = 'banana'
pos = fruit.find("na")
print(pos)
aa = fruit.find("z")
print(aa)

#search and replace

greet = "hello bob"
pos = greet.replace('bob','sneha')
print(pos)
pos2 = greet.replace('o','x')
print(pos2)
pos3 = greet[3].replace("0",'j')
print(pos3)