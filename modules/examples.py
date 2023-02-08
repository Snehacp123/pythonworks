"""
  write a python prgrm to generate a random color hex ,
  a random alphabetical string ,random value btw two string , random value btw two integers ,
  random multiple of 7 btw 0 and 70 .
  hint : use random.randint()
"""
import random
rand = random.randint(0,16777215)
hex_num = str(hex(rand))
hex_num = '#'+hex_num[2:]
print(hex_num)

str = ['h','u','t','s','k']
print(random.choice(str))

print(random.randint(1,60))
print(random.randrange(0,70,7))