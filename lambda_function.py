#----------------*****Lambda Function*****--------------

#this part of the code defines a function in a single line
""" x = lambda y : y + 8
print(x(3)) """

#this part of the code shows the classic way of defining a function
""" def sum_plus8(t):
    return t + 8
print(sum_plus8(3)) """

""" cartesia_points = [(4, 2), (1, 4), (-3, 1), (1, -5)]

#this part of the code sort by y coordinate
sorted_points = sorted(cartesia_points, key = lambda x: x[1])
print(sorted_points)

#this part of the code sort by x coordinate
sorted_points = sorted(cartesia_points, key = lambda x: x[0])
print(sorted_points)

#this part of the code sort by x and y coordinate
sorted_points = sorted(cartesia_points, key = lambda x: x[0] + x[1])
print(sorted_points) """

#-----------------------filter function------------------ filter(func, seq)
a = [] 

for i in range(100): 
    a.append(i) 
    b = filter(lambda x: x%2 == 0, a) 

c = [y for y in a if y%2 == 0]

print(list(b))
print(c)

#-----------------------reduce function------------------ reduce(func, seq)

