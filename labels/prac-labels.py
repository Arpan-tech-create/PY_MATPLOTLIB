import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


a=np.array([44,56,23,12])
b=np.array([66,12,4,89])

plt.figure(figsize=(12,6))
plt.plot(a,b)
plt.grid()
plt.title("LINES")
plt.xlabel("X-AXIS")
plt.ylabel('Y-AXIS')
plt.show()