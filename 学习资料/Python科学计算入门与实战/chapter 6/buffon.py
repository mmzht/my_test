import numpy as np
import matplotlib.pyplot as plt
def buffon(N,a,L):
    x = np.random.uniform(0,a/2,N)
    theta = np.random.uniform(0,np.pi,N)
    d = x*np.sin(theta)
    index = np.where(x < L/2*np.sin(theta))[0]
    return index.shape[0]/N

##N = 100000
a = 1
L = 0.6
##P = buffon(N,a,L)
##pi = 2*l/(a*P)

N = [10,100,1000,10000,100000,1000000,10000000]
pi = [2*L/(a*buffon(n,a,L)) for n in N]

plt.semilogx(N,pi)
plt.xlabel("N times")
plt.ylabel("$\pi$")
plt.show()
