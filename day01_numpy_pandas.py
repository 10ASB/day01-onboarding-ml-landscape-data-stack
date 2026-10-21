import numpy as np
import pandas as pd

# Array creation
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((2, 3))
c = np.ones((3, 2))
d = np.arange(1, 11)
e = np.linspace(0, 10, 5)

print("Array:", a)
print("Zeros:\n", b)
print("Ones:\n", c)
print("Arange:", d)
print("Linspace:", e)

# Broadcasting
print("\nBroadcasting:")
print(a + 5)
print(a * 2)

# Slicing
print("\nSlicing:")
print(a[1:4])
print(a[::-1])

# argmax
print("\nIndex of maximum value:")
print(np.argmax(a))

# where
print("\nValues greater than 3:")
print(np.where(a > 3))
