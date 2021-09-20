#----------------------------Errors and Exceptions-----------------------------------

""" try:
    x = 5/0
except:
    print('division by zero') """

""" x = -5
assert (x >= 0), 'x is not positive' """

x = -5
if x < 0:
    raise Exception('x should be positive')