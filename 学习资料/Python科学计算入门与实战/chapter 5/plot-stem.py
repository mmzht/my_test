import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(10) + 1
y = [10,-18,-21,4,7,-3,13,16,9,-10]
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,4))
ax1.stem(x,y)
markerlines, stemlines, baseline=ax2.stem(
    x,y,linefmt="g--",markerfmt="sg",bottom=1,label="data")
markerlines.set_markerfacecolor("none")
baseline.set_linewidth(2)
baseline.set_linestyle("dashed")
ax2.legend()
plt.show()
