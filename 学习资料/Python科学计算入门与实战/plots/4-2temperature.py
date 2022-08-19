import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   
mpl.rcParams['axes.unicode_minus'] = False

from math import pi,log
T0 = 10
A = 10
k = 3600e-6
P = 24
w = 2*pi/P
a = sqrt(w/(2*k))
def ground_temp(z,t):
    return T0 + A*np.exp(-a*z)*np.cos(w*t - a*z)

z = np.arange(0,1,0.1)
y1 = ground_temp(z,t = 0)
y6 = ground_temp(z,t = 9)
y18 = ground_temp(z,t = 14)

plt.plot(z,y1,'--r',label = "$t=0h$")
plt.plot(z,y6,'-g',label = "$t=9h$")
plt.plot(z,y18,'-+k',label = "$t=14h$")
plt.xlabel('$z/m$')
plt.ylabel('T/$^\circ$C')
plt.legend(loc = 'upper center')
plt.show()
