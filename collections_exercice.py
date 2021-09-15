#***************************************************collections***************************************

#------------------------------------ counter -------------------------------------------
""" from collections import Counter

x = 'Hello this is a sentence, lets see how many a it as'
print(Counter(x)) #Counter(x) is a dictionary 
print(Counter(x).items())
print(Counter(x).values())
 """
#----------------------------- namedtuple -------------------------------------------

""" from collections import namedtuple

recta = namedtuple('recta', 'slope, intersection')
print(recta(5, 3))
 
punto = namedtuple('punto', 'x, y')
print(punto(3, 2))  """

#----------------------------- deque -------------------------------------------

from collections import deque

d = deque()
d.append('LUIS')
d.append('MIGUEL')
d.append('JIMENEZ')
d.appendleft('castro')
print(d)
