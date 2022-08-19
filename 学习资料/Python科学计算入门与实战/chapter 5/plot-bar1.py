import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

xlabels = ["企业家","科学家","需要","做事","看见"]
counts = [4,3,2,2,2]

fig = plt.figure(figsize = (10,4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.bar(xlabels,height = counts,width = 0.2,align = "edge")
ax1.set_yticks([1,2,3,4,5])
ax1.set_ylabel("频次")
plt.bar(xlabels,counts,color = "red")
plt.yticks([1,2,3,4,5])
plt.ylabel("频次")
plt.show()

