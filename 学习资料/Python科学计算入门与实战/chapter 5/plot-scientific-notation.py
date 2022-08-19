import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False   

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
x = np.linspace(0, 1e5, 100)
y = x ** 2
axes[0].plot(x, y, 'b.')
axes[0].set_title("默认刻度显示", loc='right')

axes[1].plot(x, y, 'b')
axes[1].set_title("科学记数法显示", loc='right')
formatter = mpl.ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
axes[1].xaxis.set_major_formatter(formatter)
axes[1].yaxis.set_major_formatter(formatter)
plt.show()
