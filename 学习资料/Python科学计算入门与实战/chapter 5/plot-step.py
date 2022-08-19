import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(15)
y = np.sin(x / 2)
plt.step(x, y + 2, label='默认前侧')
plt.plot(x, y + 2, 'o--', color='green')

plt.step(x, y + 1, where='mid', label='中间')
plt.plot(x, y + 1, 'o--', color='purple', alpha=0.3)

plt.step(x, y, where='post', label='后侧')
plt.plot(x, y, 'o--', color='black', alpha=0.3)

plt.grid(axis='x', color='0.95')
plt.legend()
plt.show()

