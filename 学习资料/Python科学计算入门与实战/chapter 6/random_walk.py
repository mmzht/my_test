import random

def random_walk1d(x0,s,N=10):
    pos = x0
    trajectory = [x0]
    for _ in range(N):
        rn = random.random()
        if rn < 0.5:
            pos += s
        pos -= s
        trajectory.append(pos)
    return pos,trajectory

import numpy as np
def random_walk1d_vec(pos,s,N=10):
    pos = np.array(pos)
    nop = pos.shape[0]
    traj = np.zeros((N,nop))
    traj[0] = pos
    s = np.asarray(s)
    moves = np.random.random_integers(1,2,N*nop).reshape(N,nop)
    FORWARD,BACKWARD = 1,2
    traj[moves==FORWARD] = 1.
    traj[moves==BACKWARD] = -1.
    traj = np.cumsum(traj*s,axis=0)
    return traj

def random_walk_vec(pos,s,N=10):
    pos = np.array(pos)
    nop,dim = pos.shape
    traj = np.zeros((N,nop,dim))
    traj[0] = pos
    s = np.asarray(s)
    if dim == 2:
        moves = np.random.random_integers(1,4,N*nop*dim).reshape(N,nop,dim)
        RIGHT,LEFT,UP,DOWN = 1,2,3,4
        traj[moves== RIGHT] = 1.
        traj[moves== LEFT] = -1.
        traj[moves== UP] = 1.
        traj[moves== DOWN] = -1.
    if dim == 3:
        moves = np.random.random_integers(1,6,N*nop*dim).reshape(N,nop,dim)
        RIGHT,LEFT,UP,DOWN,FRONT,BACK, = 1,2,3,4,5,6
        traj[moves== RIGHT] = 1.
        traj[moves== LEFT] = -1.
        traj[moves== UP] = 1.
        traj[moves== DOWN] = -1.
        traj[moves== FRONT] = 1.
        traj[moves== BACK] = -1.   
    traj = np.cumsum(traj*s,axis=0)
    return traj


import matplotlib.pyplot as plt
nop = 1000
pos = np.zeros((nop,2))
s = 1
N = 1000
traj = random_walk_vec(pos,s,N)
X0 = traj[:,0,0] 
Y0 = traj[:,0,1]
s = np.random.normal(0,1,(N,nop,2))
traj = random_walk_vec(pos,s,N)
X1 = traj[:,0,0] 
Y1 = traj[:,0,1]

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(8,3))
ax1.plot(X0,Y0,"r")
ax2.plot(X1,Y1,"r")
plt.show()

##X1 = traj[49,:,0]
##Y1 = traj[49,:,1]
##X2 = traj[199,:,0]
##Y2 = traj[199,:,1]
##X3 = traj[499,:,0]
##Y3 = traj[499,:,1]
##X4 = traj[999,:,0]
##Y4 = traj[999,:,1]
##
##fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharex=True,sharey=True)
##ax1.scatter(X1,Y1,marker=".")
##ax1.set_title("N=50")
##ax2.scatter(X2,Y2,marker=".")
##ax2.set_title("N=200")
##ax3.scatter(X3,Y3,marker=".")
##ax3.set_title("N=500")
##ax4.scatter(X4,Y4,marker=".")
##ax4.set_title("N=1000")
##
##plt.show()
