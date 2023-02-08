#1.Adding elements to a list using while loop

n = int(input("enter the number"))
my_list = []
i = 1
while len(my_list) <= n:
    my_list.append(i)
    i = i + 1
print(my_list)

#2.finding the average of 5 numbers

sum = 0
i = 0
while i < 5:
    n = int(input("enter a number"))
    sum = sum + n
    i = i + 1
avg = sum / 5
print(f"average of these number is: {avg}")

#3.printing the sqr of numbers
n = int(input("enter the number"))
i = 1
while i <= n:
    i = i+1
print("square of",n,"is",n*n)

#4.reversing a number

n = int(input("enter the number"))
rev = 0
while n > 0:
    reminder = n % 10
    rev = (rev * 10) + reminder
    n = n//10
print("reverse is",rev)

#5.finding the sum of even numbers
max = int(input("enter the maximum value"))
num = 1
sum = 0
while num <= max:
    if num % 2 == 0:
        print(num)
        sum = sum + num
    num = num + 1
print("sum of even numbers from 2 to",max, "is:", sum)

#6.check whether a number is prime or not
num = int(input("enter the number"))
count = 0
i = 2
while i < num:
    if num % i == 0:
        count = 1
        print(num,"is not a prime number")
    i = i + 1
if count == 0:
    print(num,"is a prime number")

#7. print even and odd numbers bw 1 to the entered numbers

n = int(input("enter the limit"))
print("odd\t\teven")
i = 1
while i < n:
    print(f'{i}\t\t{i+1}')
    i = i+2