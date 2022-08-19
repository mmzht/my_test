import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(10)
y1 = 2.5 * np.sin(x / 20 * np.pi)
y2 = y1 + 1
y3 = y1 + 2
y4 = y1 + 3
yerr = np.linspace(0.05, 0.2, 10)

plt.errorbar(x,y1,yerr=0.1,label="默认上下限")
plt.errorbar(x,y2,yerr=yerr, errorevery=3,
             uplims=True,label="不显示上限")
plt.errorbar(x,y3,yerr=yerr,lolims=True,
             lw=3,capsize=1,capthick=1.5,elinewidth=1,label="不显示下限")
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x,y4,yerr=yerr,ls="dotted",
             uplims=upperlimits, lolims=lowerlimits,
             label="交叉显示")
plt.legend()
plt.show()
