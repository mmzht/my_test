import random
import matplotlib.pyplot as plt
import numpy as np

def mc_integral(f,a,b,n,m,N=100):
    x = np.random.uniform(a,b,N)
    y = np.random.uniform(n,m,N)
    M = y[y < f(x)].size
    return M/N*(m-n)*(b-a)

def mc_integral1(f,a,b,N=100):
    x = np.random.uniform(a,b,N)
    return np.sum(f(x))/N*(b-a)


def f(x):
    return np.sin(x)
a = 0
b = np.pi
N = 10000
m = 1.1
n = 0.
I = mc_integral(f,a,b,n,m,N)
err = 2 - I
I1 = mc_integral1(f,a,b,N)

print("积分值为%f"%I)
print("误差为%f"%err)
