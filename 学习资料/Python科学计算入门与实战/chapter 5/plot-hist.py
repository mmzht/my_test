import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

x = [117.7,112.4,122.8,124.2,119.3,131.0,121.3,114.5,113.0,
     118.5,121.1,129.0,108.2,121.5,124.8,122.5,118.8,117.0,
     123.5,115.2,126.1,116.9,129.7,124.8,118.5,126.8,124.4,
     118.7,118.7,130.6]

x2 = np.reshape(np.array(x),(-1,2))
bins1 = 10
bins2 = np.linspace(108,132,10)
bins3 = 5
fig,axes = plt.subplots(2,2)
ax1 = axes[0,0]
ax2 = axes[0,1]
ax3 = axes[1,0]
ax4 = axes[1,1]

ax1.hist(x,bins=bins1)
n,bins,patches = ax2.hist(x,bins=bins2,color="g",density=True)
ax3.hist(x,bins=bins1,histtype="step",cumulative=True)
ax4.hist(x2,bins=bins3,stacked=True)

mu = np.mean(x)
sigma = np.std(x)
y = ((1/(np.sqrt(2*np.pi)*sigma))*\
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax2.plot(bins,y,lw=3,color="r",ls="dashed")
plt.show()
