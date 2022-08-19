import matplotlib.pyplot as plt
def harmonic(n):
    return sum(1/i for i in range(1,n+1))

n1 = 10
x1 = list(range(1,n1+1))
y1 = [harmonic(i) for i in x1]

n2 = 100
x2 = list(range(1,n2+1))
y2 = [harmonic(i) for i in x2]

n3 = 1000
x3 = list(range(1,n3+1))
y3 = [harmonic(i) for i in x3]

n4 = 10000
x4 = list(range(1,n4+1))
y4 = [harmonic(i) for i in x4]



plt.subplot(221)
plt.plot(x1,y1)
plt.ylabel("$S_n$")
plt.subplot(222)
plt.plot(x2,y2)
plt.subplot(223)
plt.plot(x3,y3)
plt.xlabel("$n$")
plt.ylabel("$S_n$")
plt.subplot(224)
plt.plot(x4,y4)
plt.xlabel("$n$")
plt.show()
