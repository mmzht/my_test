import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

x1 = [12,15,17,9,20,23,25,28,30,33,34,35,36,37]
x2 = np.reshape(x1,(-1,2))
x3 = np.array(x1 + [60,70])
x4 = np.array(x1 + [-20,65])
markers = dict(marker = "s",markerfacecolor="g",markersize=5)
colors = ["g","r"]

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
ax1.boxplot(x1)
boxplot2 = ax2.boxplot(x2,vert=False,patch_artist=True)
for patch,color in zip(boxplot2["boxes"],colors):
    patch.set_facecolor(color)
ax3.boxplot(x3,notch=True,labels=["x3"])
ax4.boxplot(x4,flierprops=markers)
plt.show()
