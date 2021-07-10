# y = x^2 그래프 그리기

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10) # 0:9
y = x**2 # 0 ,1 ,4, ..., 81
plt.plot(x,y)
plt.show()
plt.savefig('jpg/plt_simple.jpg')