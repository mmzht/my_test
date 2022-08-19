import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

a = 2
theta = np.linspace(-np.pi,np.pi,100)
r1 = a*np.cos(3*theta)
r2 = a*(1-np.sin(theta))
ax1 = plt.subplot(121, projection='polar')
ax2 = plt.subplot(122, projection='polar')

ax1.plot(theta,r1,"r-")
ax1.set_rmax(3)
ax1.set_rticks([1,2]) 
ax1.set_rlabel_position(45)
ax1.grid(True)

ax2.plot(theta,r2,"g--")
ax2.set_rmax(5)
ax2.set_rticks([1,2,3,4]) 
ax2.set_rlabel_position(-45)
ax2.grid(True)

plt.show()
