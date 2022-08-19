import numpy as np
import matplotlib.pyplot as plt

d0i = 5
p0i = 0.1
A = 2.
wij1 = 0
wij2 = 0.5

def caculate_p(dij,d0i,wij,p0i,A):
    if dij < d0i:
        return (1 + wij)*p0i
    return (1 + wij)*p0i*A**(-(dij-d0i))

dij = np.arange(0,20,0.5)

pij1 = [caculate_p(d,d0i,wij1,p0i,A) for d in dij]
pij2 = [caculate_p(d,d0i,wij2,p0i,A) for d in dij]

plt.plot(dij,pij1,"r-",label = "$w=0$")
plt.plot(dij,pij2,"g--",label = "$w=0.5$")
plt.legend()
plt.xlim([0,20])
plt.xlabel("$d_{ij}$",fontsize = 12)
plt.ylabel("$p_{ij}$",fontsize = 12)
plt.show()
