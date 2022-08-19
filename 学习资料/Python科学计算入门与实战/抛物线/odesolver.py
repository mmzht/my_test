import numpy as np

class OdeSolver:
    def __init__(self,F,t0,u0,dt):
        self.F = F
        self.t0 = t0
        self.u0 = u0
        self.dt = dt
        self.T = None
        self.U = None

    def step(self):
        pass

    def solve(self,k):
        F = self.F
        u = self.u0
        dt = self.dt
        t = self.t0
        self.T = [t]
        self.U = [u]
        for _ in range(k):
            t,u = self.step(F,t,u,dt)
            self.T.append(t)
            self.U.append(u)
        self.T = np.array(self.T)
        self.U = np.array(self.U)

class ForwardEuler(OdeSolver):
    def step(self,F,t,u,dt):
        u = u + dt*F(t,u)
        t = t + dt
        return t,u
        
class RungeKutta(OdeSolver):
    def step(self,F,t,u,dt):
        K0 = dt*F(t,u)
        K1 = dt*F(t + dt/2,u + K0/2)
        K2 = dt*F(t + dt/2,u + K1/2)
        K3 = dt*F(t + dt,u + K2)
        u = u + (K0 + 2*K1 + 2*K2 + K3)/6.0
        t = t + dt
        return t,u

if __name__ == "__main__":
    def F(t,u):
        u1 = u[1]
        return np.array([u1,-0.5*u1-t])
    t0 = 0
    u0 = np.array([0,1])
    dt = 0.1
    s1 = ForwardEuler(F,t0,u0,dt)
    s2 = RungeKutta(F,t0,u0,dt)
    s1.solve(5)
    s2.solve(5)
