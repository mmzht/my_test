import numpy as np
import matplotlib.pyplot as plt
##plt.rcParams['font.sans-serif'] = ['SimHei']   
##plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0,1e3,100)
y1,y2 = x**3,x**4

fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(12,3))

ax1.loglog(x,y1,"b",x,y2,"r")
ax1.set_title("loglog base 10")

ax2.semilogy(x,y1,"b",x,y2,"r",basey=2)
ax2.set_title("semilogy base 2")

ax3.semilogx(y1,x,"b",y2,x,"r",basex=3)
ax3.set_title("semilogx base 3")
plt.show()

