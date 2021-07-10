# plot 의 색 지정

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x **2
plt.plot(x,y,'r')
plt.savefig('jpg/plt_color.jpg')
plt.show()

