import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False     

r = np.linspace(0,6,30)
area = np.pi*r**2
perimeter = 2*np.pi*r
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(r,area,'g-',label ="半径")
ax2.plot(r,perimeter,'r--',label ="周长")
ax1.set_xlabel("圆的半径/$m$",fontsize = 12)
ax1.set_ylabel("圆的面积/$m^2$",fontsize = 12)
ax2.set_ylabel("圆的周长/$m$",fontsize = 12)
ax1.legend(loc=2)
ax2.legend(loc=9)
plt.show()
