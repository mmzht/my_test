import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = np.linspace(-3,3,20)
y = 10*x                       #y=10x
x1 = np.linspace(-2,2,20)
y1 = 8*x1**2                  #y=8x2
x2 = np.linspace(-3,3,20)
y2 = x2**3                    #y=x3
line1, = plt.plot(x,y,"r-*",linewidth = 1.5,)
line2, = plt.plot(x1,y1,"g--",linewidth = 0.9,)
line3, = plt.plot(x2,y2,"k:",linewidth = 2.0)
handles = [line1,line2,line3]
labels = ["$y=10*x$","$y=10*x^2$","$y=x^3$"]
##plt.legend(handles,labels)
##plt.xlabel("$x$ value",fontsize = 15)
##plt.ylabel("$y$ value",fontsize = 16)
ax = plt.gca()
plt.legend(handles,labels)
##ax.set_xlabel("$x$ value",fontsize = 12)
##ax.set_ylabel("$x$ value",fontsize = 12)
ax.set_xlabel("$x$ 值",fontsize = 12)
ax.set_ylabel("$y$ 值",fontsize = 12)
##ax.set_xlim([-10,10])
##ax.set_ylim(-40,40)
##ax.invert_xaxis()
##ax.invert_yaxis()
##plt.xticks([-3,-2,-1,0,1,2,3])
##plt.yticks([-30,-20,-10,0,10,20,30])
##ax.set_xticks([])
##ax.set_yticks([])
##
ax.set_title("三个函数图像")
plt.savefig("1.png")
plt.show()
