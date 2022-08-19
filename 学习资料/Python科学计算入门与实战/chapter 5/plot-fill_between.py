import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0,1,100)
y1 = np.cos(2*np.pi*x)
y2 = np.cos(5*np.pi*x)
fig,(ax1,ax2,ax3) = plt.subplots(3,1,figsize=(6,6),sharex=True)
ax1.fill_between(x,y1,y2,color="red")
ax1.set_title("y1和y2之间填充红色")
ax2.fill_between(x,y2,0)
ax2.set_title("y2和0之间填充默认颜色")
ax3.fill_between(x,y1,y2,where = y1<y2,facecolor="green",alpha=0.3)
ax3.fill_between(x,y1,y2,where = y1>y2,facecolor="black",alpha=0.3)
ax3.set_title("y1<y2处填充绿色,y1>y2处填充黑色")
plt.show()

