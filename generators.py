import sys
#Function without a generator
def n(x):
    N = []
    n = 0
    while n < x:
        N.append(n)
        n = n + 1
    return N

print(n(10))

#Function with a generator // low weight memory

def m_generator(y):
    m = 0
    while m < y:
        yield m
        m = m + 1
         
print(list(m_generator(10)))