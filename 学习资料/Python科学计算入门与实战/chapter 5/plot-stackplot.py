import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

x = [1,2,3,4,5]
y1 = [2,3,5,8,1]
y2 = [0,1,4,3,6]
y3 = [4,0,3,5,2]
y = np.vstack((y1,y2,y3))
fig,(ax1,ax2,ax3) = plt.subplots(3,1,figsize=(6,6))
ax1.stackplot(x,y1,y2,y3)
ax2.stackplot(x,y,baseline="sym")
ax3.stackplot(x,y,baseline="wiggle",
              colors=["red","cyan","green"])
plt.show()

