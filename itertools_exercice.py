#----------------------------- Product -------------------------------------------

""" from itertools import product

#this part of the code shows all possible combinations between the elements of a list a y b.
a = [1, 2, 3]
b = [4, 1, 5]

x = product(a, b)
y = product(b,a)
print(list(x))
print(list(y)) 
 """
#----------------------------- permutations -------------------------------------------

""" from itertools import permutations

#this part of the code shows all possible combinations the elements of a list a y b.
a = [1, 2, 3]
b = [4, 1, 5]

x = permutations(a)
y = permutations(b)
print(list(x))
print(list(y))  """

#----------------------------- combinations -------------------------------------------

""" from itertools import combinations

#this part of the code shows all possible combinations the elements of a list a y b.
a = [1, 2, 3]
b = [4, 1, 5]

x = combinations(a, 1)
y = combinations(b, 2)
print(list(x))
print(list(y))  """

#----------------------------- accummulate -------------------------------------------

"""from itertools import accumulate

#this part of the code adds item by item the arguments in the list.
a = [1, 2, 3, 4, 5, 6]

x = accumulate(a)
print(list(x)) """

#----------------------------- groupby -------------------------------------------

""" from itertools import groupby

#this part of the code returns true for numbers less than 30 and false for the ohters.
def function(x):
    return x < 30


#this part of the code creates an empty list an fills it with numbers from one to one hundred.
a = []
for i in range(100):
    a.append(i+1) """

""" this part of the code groups the elements in the list a according to the condition entered in function(x), 
in this case it groups the values in a list if they are less than 30 (true) and 
in another list (false) if they are greater than 100.
"""
""" y = groupby(a, function)

for function, t in y:
    print(function, list(t))

students = [{'name': 'Raul', 'age': 28, 'nationality': 'mexican'}, 
{'name': 'Luis', 'age': 30, 'nationality': 'colombian'},
{'name': 'Guadalupe', 'age': 26, 'nationality': 'mexican'},
{'name': 'Rosa', 'age': 26, 'nationality': 'mexican'}]

z = lambda x: x['nationality']
y = groupby(students, z)
for z , t in y:
    print(z, list(t))  """

#----------------------------- infinite iterators -------------------------------------------

from itertools import count, cycle, repeat

x = ['luis', 'Miguel', 'Jimenez']
""" for i in count(90):
    print(i)
    if i == 100:
        break
 """
k = 0
""" for j in cycle(x):
    print(j)
    k = k + 1
    if k == 9:
        break """

for l in repeat(2, 8):
    print(l)