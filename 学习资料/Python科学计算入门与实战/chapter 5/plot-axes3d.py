import numpy as np
import matplotlib.pyplot as plt
##plt.rcParams['font.sans-serif'] = ['SimHei']   
##plt.rcParams['axes.unicode_minus'] = False

from mpl_toolkits.mplot3d import Axes3D

##ax = Axes3D(fig)
##fig, ax=plt.subplots(1,1,figsize=(8,6),subplot_kw={'projection':'3d'})
##
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
##ax = fig.gca(projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
