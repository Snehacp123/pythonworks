import random
print("select a random element from a list:")
elements = [1,2,3,4,5]
print(random.choice(elements))
print(random.choice(elements))
print("select a random element from a set:")
element = set([1,2,3,4,5,6])
print(random.choice(tuple(element)))
print(random.choice(tuple(element)))
print("select a random element from a dictionary:")
d = {"a":1,"b":2,"c":3,"d":4,"e":5}
key = random.choice(list(d))
print(d[key])
print(random.random())
print(random.randint(1,100))
print(random.randrange(1,100,2))
num = [12,56,89,65,87]
print(random.shuffle(num))
print(num)
# print(dir(random))
