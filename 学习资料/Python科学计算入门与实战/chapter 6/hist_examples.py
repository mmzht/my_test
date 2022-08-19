import numpy as np
import matplotlib.pyplot as plt

fig,axes = plt.subplots(2,2,)

loc,scale = 0,1
s = np.random.laplace(loc,scale,1000)
count,bins,ignored = axes[0,0].hist(s,30,density=True)
pdf = np.exp(-abs(bins-loc)/scale)/(2.*scale)
axes[0,0].plot(bins,pdf,lw=2,ls="dashed",color="red")
axes[0,0].set_title("laplace")

loc,scale = 10,1
s = np.random.logistic(loc,scale,10000)
count,bins,ignored = axes[0,1].hist(s,bins=50,density=True)
pdf = np.exp((loc-bins)/scale)/(scale*(1+np.exp((loc-bins)/scale))**2)
axes[0,1].plot(bins,pdf,lw=2,color="red")
axes[0,1].set_title("logistic")

mu,sigma = 0,2
s = np.random.normal(mu,sigma,1000)
count,bins,ignored = axes[1,0].hist(s,30,density=True)
pdf = 1/(sigma * np.sqrt(2 * np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2))
axes[1,0].plot(bins,pdf,lw=2)
axes[1,0].set_title("normal")

a = 4
s = np.random.power(a,10000)
count,bins,ignored = axes[1,1].hist(s,30,density=True)
pdf = a*bins**(a-1.)
axes[1,1].plot(bins,pdf,lw=2)
axes[1,1].set_title("power")

plt.subplots_adjust(left=0.1,right=0.95,bottom=0.1,
                    top=0.95,wspace=0.2,hspace=0.25)
plt.show()
