import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,2,4)
y = np.linspace(0,3,6)
vx,vy = np.meshgrid(x,y)
vx,vy = vx.flatten(),vy.flatten()
markers = [".",",","^","v","<",">",
           "1","2","3","4","8","s",
           "p","P","*","h","H","+",
           "X","D","d","|","_"]
for i in range(len(markers)):
    plt.plot(vx[i],vy[i],marker = markers[i],markersize = 8,color = "r")
plt.show()
