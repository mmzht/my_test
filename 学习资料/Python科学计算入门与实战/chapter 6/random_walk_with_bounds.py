import numpy as np

class Box:
    def __init__(self,ori,width,height):
        self.ori = ori
        self.width = width
        self.height = height

    def outsider(self,x,y):
        x0,y0 = self.ori
        width = self.width
        height = self.height
        dx,dy = x - x0,y - y0
        flagx = np.logical_or(dx > width, x < x0)
        flagy = np.logical_or(dy > height, y < y0)
        return flagx,flagy
        
        
class Molecules:
    def __init__(self,nom):
        self.nom = nom
        self.x = None
        self.y = None
        self.initbox = None
        self.walkbox = None
        self.N = 0

    def set_initbox(self,box):
        self.initbox = box
        if not self.walkbox:
            self.walkbox = box
            
    def set_walkbox(self,box):
        self.walkbox = box

    def set_step(self,s):
        self.s = s

    def init_pos(self):
        self.N = 0
        x0,y0 = self.initbox.ori
        width = self.initbox.width
        height = self.initbox.height
        nom = self.nom
        self.initx = np.random.uniform(x0,x0+width,nom)
        self.inity = np.random.uniform(y0,y0+height,nom)
        self.x = self.initx.copy()
        self.y = self.inity.copy()
        self.sx = self.initx.copy()
        self.sy = self.inity.copy()
        self.sign_sx = np.ones_like(self.x)
        self.sign_sy = np.ones_like(self.y)
        
    def random_walk(self,N):
        self.N += N
        s = self.s
        nom = self.nom
        moves = np.random.random_integers(1,4,(N,nom))
        sx = np.random.uniform(0,s,(N,nom))
        sy = np.random.uniform(0,s,(N,nom))
        tempx = self.x.copy()
        tempy = self.y.copy()
        sign_sx = np.zeros_like(sx)
        sign_sy = np.zeros_like(sy)
        RIGHT,LEFT,UP,DOWN = 1,2,3,4
        sign_sx[moves== RIGHT] = 1.
        sign_sx[moves== LEFT] = -1.
        sign_sy[moves== UP] = 1.
        sign_sy[moves== DOWN] = -1.
        for step in range(N):
            this_sx = sx[step]
            this_sy = sy[step]
            tempx += sign_sx[step]*this_sx
            tempy += sign_sy[step]*this_sy
            o_x,o_y = self.walkbox.outsider(tempx,tempy)
            this_sx[o_x] = 0
            this_sy[o_y] = 0
            self.x += sign_sx[step]*this_sx
            self.y += sign_sy[step]*this_sy
        self.sx = np.vstack((self.sx,sx))
        self.sy = np.vstack((self.sy,sy))
        self.sign_sx = np.vstack((self.sign_sx,sign_sx))
        self.sign_sy = np.vstack((self.sign_sy,sign_sy))

    def traj(self,index = 0):
        sx,sy = self.sx,self.sy
        sign_sx,sign_sy = self.sign_sx,self.sign_sy
        traj_x = np.cumsum(sx*sign_sx,axis=0)
        traj_y = np.cumsum(sy*sign_sy,axis=0)
        return traj_x[:,index],traj_y[:,index]

import matplotlib.pyplot as plt
box1 = Box((0,0),1,0.5)
box2 = Box((0,0),1,1)
s = 0.02
nom = 5000
N = 1000
ms = Molecules(nom)
ms.set_initbox(box1)
ms.set_walkbox(box2)
ms.set_step(s)
ms.init_pos()

def plot_axis(ax,title,x,y):
    ax.scatter(x,y,marker = ".",s=5)
    ax.set_xticks([0,1])
    ax.set_yticks([0,1])
    ax.set_title(title)
    
fig,axes = plt.subplots(2,2)
plot_axis(axes[0,0],"N=%d"%ms.N,ms.x,ms.y)
ms.random_walk(N)
plot_axis(axes[0,1],"N=%d"%ms.N,ms.x,ms.y)
ms.random_walk(N)
plot_axis(axes[1,0],"N=%d"%ms.N,ms.x,ms.y)
ms.random_walk(N)
plot_axis(axes[1,1],"N=%d"%ms.N,ms.x,ms.y)
plt.show()

fig1 = plt.figure()
ax = fig1.add_subplot(111)
x,y = ms.traj(12)
ax.plot(x,y,"r-")
ax.set_xticks([np.min(x)-0.1,np.max(x)+0.1])
ax.set_yticks([np.min(y)-0.1,np.max(y)+0.1])
plt.show()
