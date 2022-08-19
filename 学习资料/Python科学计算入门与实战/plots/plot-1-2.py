from math import pi
import numpy as np
import matplotlib.pyplot as plt
def cook_egg(M,T0,Tw =100,Ty = 70):
    density,c,K = 1.038,3.7,5.4e-3
    numerator = M**(2/3)*c*density**(1/3)
    denominator = K*pi**2*(4*pi/3)**(2/3)
    ln = np.log(0.76*(T0 - Tw)/(Ty - Tw))
    t = numerator/denominator*ln
    return t

    
    
M1 = 47
T01 = 20

M2 = 67
T02 = 4
Ty = np.linspace(50,70,10)
t1 = cook_egg(M1,T01,Tw = 100, Ty = Ty)
t2 = cook_egg(M2,T02,Tw = 100, Ty = Ty)
ax = plt.gca()
plt.plot(Ty,t1,'--r',label = '$M=47g,T_0=20^\circ C,T_w=100^\circ C$')
plt.plot(Ty,t2,'-+g',label = '$M=67g,T_0=4^\circ C,T_w=100^\circ C$')
plt.xlabel('$T_y(^\circ C)$')
plt.ylabel('t($s$)')
plt.legend(loc = 'upper center')
plt.show()
