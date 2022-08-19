import numpy as np
import matplotlib.pyplot as plt
##plt.rcParams['font.sans-serif'] = ['SimHei']   
##plt.rcParams['axes.unicode_minus'] = False

from mpl_toolkits.mplot3d import Axes3D
x=np.linspace(0,2*np.pi,50)
y1=np.sin(x)+1
y2=np.sin(x)+1
x1 =2*np.random.sample(20)*np.pi
y3 =2*np.random.sample(20)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x,y1,zs=0,zdir="z",label="curve in (x,y)")
ax.plot(x,y2,zs=2,zdir="y",label="curve in (x,z)")
ax.scatter(x1,y3,zs=0,zdir="y",label="points in (x,z)")

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(0, 2)
ax.set_zlim(0, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
