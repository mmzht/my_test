import numpy as np

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.coord = (x,y)

class Route:
    def __init__(self,nodes,ws):
        self.nodes = nodes
        self.non = len(nodes)
        self.init()
        self.ws = np.asarray(ws)

    def init(self):
        coords = []
        for node in self.nodes:
            coords.append(node.coord)
        coords = np.asarray(coords)
        diff = np.diff(coords,axis = 0)
        norm = np.linalg.norm(diff,axis = 1)
        norm = norm.reshape(-1,1)
        self.v = diff/norm
        self.coords = coords
        self.norm = norm

    def add_individuals(self,noi):
        norm = self.norm
        v = self.v
        coords = self.coords
        axis_pos = np.zeros((noi,2))
        non = self.non
        rds = np.random.randint(0,non-1,noi)
        offset = norm[rds,:]*np.random.uniform(0,1,(noi,1))
        axis_pos = coords[rds,:] + offset * v[rds,:]
        self.noi = noi
        self.rds = rds
        self.axis_pos = axis_pos

    def change_dir(self):
        axis_pos = self.axis_pos
        rds = self.rds
        max_rds = self.non-2
        rde = rds + 1
        v = self.v
        coords = self.coords
        iv = v[rds,:]
        icoords = coords[rde,:]
        nv = icoords - axis_pos
        dot = np.sum(iv*nv,axis = 1)
        indices = np.where(dot < 0)
        axis_pos[indices] = icoords[indices,:]
        rds[indices] += 1
        maxer = rds > max_rds
        axis_pos[maxer] = coords[0]
        rds[maxer] = 0
        self.axis_pos = axis_pos
        self.rds = rds
        
    def move(self,s):
        self.change_dir()
        axis_pos = self.axis_pos 
        rds = self.rds
        v = self.v
        ws = self.ws
        iv = v[rds,:]
        ivc = iv[:,[1,0]]
        ivc[:,1] *= -1
        iws = ws[rds].reshape(-1,1)
        s_min,s_max = s
        s = np.random.uniform(s_min,s_max,(self.noi,1))
        rand = np.random.uniform(-0.4,0.4,(self.noi,2))
        axis_pos = axis_pos + s*iv
        pos = axis_pos + rand*iws*ivc
        self.axis_pos = axis_pos
        self.pos = pos

    def init_para(self,D0,P0,W,A=np.e):
        self.D0 = np.asarray(D0)   
        self.P0 = np.asarray(P0)   
        self.W = np.asarray(W)   
        self.A = np.asarray(A)
        self.patients = np.zeros(self.noi,dtype = int)
        self.patients_list = [self.patients.copy()]
        
    def place_source(self,source):
        self.patients[source] = 1

    def update_patients(self,coords):
        for coord in coords:
            D = coord - self.pos
            D = np.hypot(D[:,0],D[:,1])
            Dij = D - self.D0
            WP0 = (1+self.W)*self.P0
            WP1 = (1+self.W)*self.P0/(self.A**(Dij))
            Pij0 = np.where(Dij<=0,WP0,0.)
            Pij1 = np.where(Dij>0,WP1,0.)
            Pij = Pij0 + Pij1
            Pr = np.random.uniform(0.001,1,self.noi)
            DP = Pr - Pij
            infected = DP < 0
            self.patients[infected] = 1
            self.patients_list.append(self.patients.copy())


class System:
    def __init__(self,routes):
        self.routes = routes
        self.nor = len(self.routes)

    def add_individuals(self,nois):
        for route,noi in zip(self.routes,nois):
            route.add_individuals(noi)

    def init_para(self,D0,P0,W,A=np.e):
        for route in self.routes:
            route.init_para(D0,P0,W,A)

    def discover_patients(self):
        patients_coords = []
        for route in self.routes:
            infected = route.patients == 1
            patients_coords.append(route.pos[infected])
        self.patients_coords = np.vstack(patients_coords)

    def run(self,s,N):
        patients = []
        for route in self.routes:
            route.traj = np.zeros((N,route.noi,2))
            
        for step in range(N):
            for route in self.routes:
                route.move(s)
                route.traj[step] = route.pos
                
            self.discover_patients()
            
            for route in self.routes:
                route.update_patients(self.patients_coords)

    def plot_route(self,ax):
        from planimetry import Point,Line
        for route in self.routes:
            coords = route.coords
            v = route.v
            vc = v[:,[1,0]]
            vc[:,1] *= -1
            ws = route.ws
            
            outer_lines = []
            for i in range(route.non-1):
                c0,c1 = coords[i]+vc[i]*ws[i],coords[i+1]+vc[i]*ws[i]
                p0,p1 = Point(c0[0],c0[1]),Point(c1[0],c1[1])
                outer_lines.append(Line(p0,p1))   
            outer = [coords[0]+vc[0]*ws[0]]
            for i in range(len(outer_lines)-1):
                l1,l2 = outer_lines[i],outer_lines[i+1]
                po = l1.intersect(l2)
                outer.append([po.x,po.y])
            outer.append([p1.x,p1.y])
            outer = np.asarray(outer)

            inner_lines = []
            for i in range(route.non-1):
                c0,c1 = coords[i]-vc[i]*ws[i],coords[i+1]-vc[i]*ws[i]
                p0,p1 = Point(c0[0],c0[1]),Point(c1[0],c1[1])
                inner_lines.append(Line(p0,p1))   
            inner = [coords[0]-vc[0]*ws[0]]
            for i in range(len(inner_lines)-1):
                l1,l2 = inner_lines[i],inner_lines[i+1]
                po = l1.intersect(l2)
                inner.append([po.x,po.y])
            inner.append([p1.x,p1.y])
            inner = np.asarray(inner)
            
        ax.plot(outer[:,0],outer[:,1],"k-")
        ax.plot(inner[:,0],inner[:,1],"k-")
        ax.axis('equal')

    def plot_pos(self,n):
        import matplotlib.pyplot as plt
        fig = plt.figure()
        ax = fig.add_subplot(111)
        self.plot_route(ax)
        for route in self.routes:
            patients = route.patients_list[n]
            infected = route.traj[n][patients == 1]
            noninfected = route.traj[n][patients == 0]
            ax.scatter(infected[:,0],infected[:,1],marker = "*",color = "red")
            ax.scatter(noninfected[:,0],noninfected[:,1],marker = ".",color = "green")
            ax.set_title("N = %d"%n)
        plt.show()
                 
if __name__ == "__main__":
    A = Node(0,0)
    D = Node(10,0)
    G = Node(20,10)
    L = Node(20,30)
    ws1 = [5,5,5]
    ws2 = [5,5,5]
    r1 = Route([A,D,G,L],ws1)
    r2 = Route([L,G,D,A],ws2)
    s = (0.1,0.5)
    nois = [20,20]
    N = 100
    routes = [r1,r2]
    nois = [20,20]
    D0 = 0.6
    P0 = 0.1
    W = 0
    sys = System([r1,r2])
    sys.add_individuals(nois)
    sys.init_para(D0,P0,W)
    r1.place_source(10)
    sys.run(s,N)
    for i in [1,20,40,60,80,99]:
        sys.plot_pos(i)


    
