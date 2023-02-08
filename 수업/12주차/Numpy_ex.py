import numpy as np

a = np.arange(0, 10, 5)
print(a)

b = np.linspace(0, 10, 5)
print(b)

c = np.linspace(0, 10, 4)
print(c)

d = np.logspace(1, 10, 5)
print(d)

e = np.arange(12)
print(e)
e.reshape(3, 4)
print(e)
e.reshape(6, -1)
print(e)

f = e.reshape(6 , -1)
print(f)

g = f.flatten()
print(g)
