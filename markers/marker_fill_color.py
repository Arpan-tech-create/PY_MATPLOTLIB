import matplotlib.pyplot as plt

import numpy as np


x=np.array([1,2,3,40,50,22])

plt.plot(x,marker='o',ms=20,mec='r',mfc='g')   # marker=symbol,, ms= mark size,,, mec= marker edge colour

plt.show()