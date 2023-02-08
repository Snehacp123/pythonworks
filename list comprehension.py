fruits = ["apple","banana","cherry"]
new_list = []
for x in fruits:
    if 'a' in x:
        new_list.append(x)
print(new_list)

# same thing using list comprehension

fruit = ["apple","banana","cherry","orange","pineapple","guava"]
new_list1 = [x for x in fruit if 'a' in x]
print(new_list1)

# print something using list comprehension

print([x for x in "helloword"])

# prime using loop

prime = [x for x in range(2,21) if all(x%y!=0 for y in range(2,x))]
print(prime)

#print range of numbers using if condition

num_list =[ y for y in range(100) if y % 2 == 0 if y % 5 == 0 ]
print(num_list)

# without list comprehension
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)

# with list comprehension

h_letters1 = [letter for letter in 'human']#first letter used for append to hletters1
print(h_letters1)

# even or odd
even = [x for x in range(101) if x%2 == 0]
print(even)

#sum of natural numbers
print(sum([ i for i in range(11)]))
print(sum([ i for i in range(1, int(input("enter the range:"))+1)]))#user input
print([(n*(n+1)/2) for n in range (1, int(input("enter the range:"))+1)])#using equation



print()