import matplotlib.pyplot as plt
import numpy as np

a = np.array([2,6,7,3,12,8,4,5]) # 배열 생성
plt.plot(a)
plt.show()

plt.savefig('jpg/plt_plot.jpg')