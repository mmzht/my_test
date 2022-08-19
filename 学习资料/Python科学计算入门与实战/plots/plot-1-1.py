import numpy as np
import matplotlib.pyplot as plt

def parabola(x,a,b,c):
    return a*x**2 + b*x + c

a1 = 4
b1 = 0
c1 = 10
center1 = -b1/(2*a1)
ran1 = 5

x1 = np.linspace(-ran1+center1,ran1+center1,20)
y1 = parabola(x1,a1,b1,c1)

a2 = 2
b2 = 0
c2 = 10
center2 = -b2/(2*a2)
ran2 = 5

x2 = np.linspace(-ran2+center2,ran2+center2,20)
y2 = parabola(x2,a2,b2,c2)

a3 = -2
b3 = 24
c3 = -60
center3 = -b3/(2*a3)
ran3 = 5

x3 = np.linspace(-ran3+center3,ran3+center3,20)
y3 = parabola(x3,a3,b3,c3)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.plot(x1,y1,'--r',label = '$a=4,b=0,c=10$')
plt.plot(x2,y2,'-g',label = '$a=2,b=0,c=10$')
plt.plot(x3,y3,'-*k',label = '$a=-2,b=24,c=-60$')
plt.xlim([-6,15])
plt.ylim([-50,50])
plt.legend(loc = 'upper right')
plt.show()
