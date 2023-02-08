import numpy as np

a = np.arange(25)
b = a.reshape(5,5)

print(b[0:5, 0:5:2])
