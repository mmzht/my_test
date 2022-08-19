import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(N):
    rn = np.random.uniform(-1,1,(N,2))
    x,y = rn[:,0],rn[:,1]
    d = x**2 + y**2
    M = np.where(d < 1)[0].shape[0]
    return 4*M/N


rectx = [-1,-1,1,1,-1]
recty = [-1,1,1,-1,-1]
plt.plot(rectx,recty,lw=2,color="red")

r = 1
theta = np.arange(0, 2*np.pi, 0.01)
circx = r*np.cos(theta)
circy = r*np.sin(theta)
plt.plot(circx,circy,color="green")

N = 1000
rn = np.random.uniform(-1,1,(N,2))
x,y = rn[:,0],rn[:,1]
plt.scatter(x,y,marker="+")

plt.xticks([-1,1])
plt.yticks([-1,1])
plt.axis("equal")
plt.show()
