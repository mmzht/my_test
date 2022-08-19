import numpy as np
import random
import matplotlib.pyplot as plt
A = np.array([0,0])
B = np.array([5,0])
v0 = (B - A)/np.linalg.norm(B - A)
v1 = np.array([v0[1],v0[0]])
N = 10
step = 0.5
w1 = 4
traj = np.zeros((N,2))
for i in range(N):
    offset = random.uniform(-1,1)*0.8*w1/2
    traj[i] = A + v0*step*(i+1) + v1*offset

plt.scatter(traj[:,0],traj[:,1],color = "green")
plt.plot([0,5],[-2,-2],"k-")
plt.plot([0,5],[2,2],"k-")
plt.plot([0,5],[0,0],"r--")
plt.show()
