import random
import matplotlib.pyplot as plt
import numpy as np

def tri(low,high,mode,x):
    left = 2*(x-low)/((high-low)*(mode-low))
    right = 2*(high-x)/((high-low)*(mode-low))
    return np.where(x<=mode,left,right)

N1,N2,N3 = 100,1000,10000
low = 0
high = 1
mode = 0.5
numbers1 = [random.triangular(low,high,mode) for _ in range(N1)]
numbers2 = [random.triangular(low,high,mode) for _ in range(N2)]
numbers3 = [random.triangular(low,high,mode) for _ in range(N3)]
fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(12,3),sharey=True)

n1,bins1,patches1 = ax1.hist(numbers1,bins=20,color="g",density=True)
ax1.plot(bins1,tri(low,high,mode,bins1),"--k",lw=2)
ax1.set_title("N=100")

n2,bins2,patches2 = ax2.hist(numbers2,bins=20,color="g",density=True)
ax2.plot(bins2,tri(low,high,mode,bins2),"--k",lw=2)
ax2.set_title("N=1000")

n3,bins3,patches3 = ax3.hist(numbers3,bins=20,color="g",density=True)
ax3.plot(bins3,tri(low,high,mode,bins3),"--k",lw=2)
ax3.set_title("N=10000")
plt.show()
