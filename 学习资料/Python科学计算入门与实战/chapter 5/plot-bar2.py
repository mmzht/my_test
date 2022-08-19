import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

months = ['1月', '2月', '3月', '4月', '5月']
A_means = [20, 35, 30, 35, 27]
B_means = [25, 32, 34, 20, 25]
A_std = [2, 3, 4, 1, 2]
B_std = [3, 5, 2, 3, 3]
width = 0.35

fig = plt.figure(figsize = (10,4))
##ax1 = fig.add_subplot(121)
##ax2 = fig.add_subplot(122)
ax1 = fig.add_subplot(121,projection="polar")
ax2 = fig.add_subplot(122,projection="polar")

ax1.bar(months, A_means, width, yerr=A_std, label='A')
ax1.bar(months, B_means, width, yerr=B_std, bottom=A_means,
       label='B')
ax1.legend(loc = 8)
ax1.set_ylabel('数量')

x = np.arange(len(months))
ax2.bar(x-width/2,A_means,width,yerr=A_std,label="A")
ax2.bar(x+width/2,B_means,width,yerr=B_std,label="B")
ax2.set_xticks(x)
ax2.set_xticklabels(months)
ax2.legend(loc = 8)

plt.show()
