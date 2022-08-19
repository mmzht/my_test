from odesolver import RungeKutta
import numpy as np

class Solver(RungeKutta):
    def solve(self,y_end = 0):
        F = self.F
        u = self.u0
        dt = self.dt
        t = self.t0
        self.T = [t]
        self.U = [u]
        while True:
            t,u = self.step(F,t,u,dt)
            self.T.append(t)
            self.U.append(u)
            if u[2] <= y_end:
                break
        self.T = np.array(self.T)
        self.U = np.array(self.U)
        

from math import sqrt,sin,cos
class Ball:
    def __init__(self,m,v0,theta):
        self.m = m
        self.v0 = v0
        self.theta = theta
        self.Cd = 0.03
        self.g = 9.80665

    def F(self,t,u):
        u1 = u[1]
        u3 = u[3]
        Cd = self.Cd
        m = self.m
        g = self.g
        a = -(Cd/m)*u1*(u1**2+u3**2)**0.25
        b = -(Cd/m)*u3*(u1**2+u3**2)**0.25-g
        return np.array([u1,a,u3,b])

    def fly(self,dt = 0.01):
        m = self.m
        v0 = self.v0
        theta = self.theta
        F = self.F
        t0 = 0
        u0 = np.array([0,v0*cos(theta),0,v0*sin(theta)])
        solver = Solver(F,t0,u0,dt)
        solver.solve()
        self.T = solver.T
        self.X = solver.U[:,0]
        self.Vx = solver.U[:,1]
        self.Y = solver.U[:,2]
        self.Vy = solver.U[:,3]
        self.range = self.X[-1]
        self.flying_last = self.T[-1]


if __name__ == "__main__":
    from math import pi
    m = 0.25
    v0 = 50
    theta = 30
    theta = theta/180*pi
    ball = Ball(m,v0,theta)
    ball.fly()
    
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111,aspect='equal')
    ax.plot(ball.X,ball.Y,"-r")
    ax.scatter(ball.X[::10],ball.Y[::10])
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    plt.show()

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(211)
    ax1.plot(ball.T,ball.Vx,"-r")
    ax1.set_ylabel("$v_x$")  
    ax2 = fig1.add_subplot(212)
    ax2.plot(ball.T,ball.Vy,"-r")
    ax2.set_xlabel("$t$")
    ax2.set_ylabel("$v_y$") 
    plt.show()
    
    
    

