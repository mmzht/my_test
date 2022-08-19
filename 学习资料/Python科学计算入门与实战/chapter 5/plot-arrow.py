import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

fig = plt.figure()
ax = fig.add_subplot(111)
##x = np.linspace(0,5,100)
##y = np.cos(2*np.pi*x) 
##ax.plot(x,y)
ax.set_xlim([-4,5])
ax.set_ylim([-4,1])
##ax.text(x=-2,y=1,s="Nomal",fontdict = dict(family="serif",fontsize=13,
##                                           horizontalalignment='right',
##                                           verticalalignment='bottom'))
##ax.text(x=-2,y=1,s="Nomal",fontdict ={"family":"serif","fontsize":13,
##                                      "ha":'right',
##                                      "va":'bottom'})
##ax.text(x=-2,y=-1,s="Rotation",family="serif",fontsize=13,rotation=45)
##ax.text(2, 2, r"Equation: $i\hbar\partial_t \Psi = \hat{H}\Psi$",
##        family="serif",fontsize=14)
ax.arrow(x=-2,y=-3,dx=1,dy=0,width=0.05,head_width = 0.2,
         head_length = 0.1)
ax.arrow(x=-2,y=-2,dx=1,dy=0,width=0.05,head_width = 0.2,
         head_length = 0.1,length_includes_head = True)
ax.arrow(x=0,y=-1,dx=1,dy=0,width=0.05,head_starts_at_zero = True)
ax.arrow(x=0,y=-3,dx=2,dy=2,width = 0.1,shape="right",color = "green")
ax.arrow(x=1,y=-3,dx=2,dy=2,width = 0.1,shape="left",color = "red")

##ax.annotate('Data Mode',xy=(3,3), xycoords='data')
##ax.annotate('Fraction Mode',xy=(0.7,0.4), xycoords='figure fraction')
##ax.annotate('$cos(2 \pi x)$',
##            xy=(2, 1), xycoords='data',
##            xytext=(-15, 25), textcoords='offset points',
##            arrowprops=dict(facecolor='black', shrink=0.05),
##            horizontalalignment='right', verticalalignment='bottom')
plt.show()
##mathtexts = [r"$\alpha_i>\beta_i$",
##             r"$\alpha_{i+1}^j = {\rm sin}(2\pi f_j t_i) e^{-5 t_i/\tau}$",
##             r"$\frac{3}{4},\ \binom{3}{4},\ \genfrac{}{}{0}{}{3}{4}$",
##             r'$s(t) = \mathcal{A}\mathrm{sin}(2 \omega t)$',
##             r'$\sum_{i=0}^\infty x_i , (\frac{5 - \frac{1}{x}}{4})$',
##             r'$\sqrt{2} , \sqrt[3]{x}$',
##             r"$\alpha,\ \beta,\ \chi,\ \delta,\ \lambda,\ \mu$",
##             r"$\Delta,\ \Gamma,\ \Omega,\ \Phi,\ \Pi,\ \Upsilon,\ \nabla $",
##             r"$\aleph,\ \beth,\ \daleth,\ \gimel,\ \ldots$",
##             ]
##
##fig = plt.figure()
##ax = fig.add_subplot(111)
##ax.set_xlim([-5,5])
##ax.set_ylim([-5,5])
##for i in range(9):
##    ax.text(-1,4-i,mathtexts[i])
##
##plt.show()
