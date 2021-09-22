#This module implements pseudo-random number generators.
#random module

""" import random """

""" #random number between one and zero.
a =  random.random() 
print(a)

#random number between x and y, not include y // random.uniform(x, y)
b = random.uniform(5, 10)
print(b)

#random integer number between x and y, include y // random.randint(x, y)
c = random.randint(5, 10)
print(c)

#random integer number between x and y, not include y // random.uniform(x, y)
d = random.randrange(5, 10) 
print(d)

#random number with normal distribution // random.normalvariate(float, standar deviation)
e = random.normalvariate(0, 5)
print(e) """

""" #selects an item from the list at random // random.choice()
string = 'LuisMgel'
list_1 = list(string)
f = random.choice(list_1) """

""" #selects x items from the list at random, selections can be repeated // 
h = random.choices(list_1, k=4)
print(h)

#selects x items from the list at random // random.sample(sequence('list'), x)
g = random.sample(list_1, 2)
print(g)  """

#--------------------------secrets------------------------------------------
""" #used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication and security tokens

import secrets

#random integer number between zero and y, not include y // secrets.randbelow(y)
i = secrets.randbelow(5)
print(i)

#random integer number binary // secrets.randbits(xbits) 
j = secrets.randbits(3) # 000 (0), 001 (1), 010 (2), 011 (3), 100 (4), 101 (5), 110 (6), 111 (7). 3bits.
print(j) """

#--------------------------numpy------------------------------------------
import numpy

#random matriz rows x columns, with numbers between x and y // numpy.random(x, y, (rows, columns)) 
k = numpy.random.randint(0, 10, (4, 3))
print(k)