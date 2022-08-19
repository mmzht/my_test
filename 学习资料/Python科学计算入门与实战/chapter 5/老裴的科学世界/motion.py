from math import *
from tkinter import *
import time
import threading
def thread_it(func, *args):
    t = threading.Thread(target=func, args=args) 
    t.setDaemon(True) 
    t.start()
    
class Model:
    def __init__(self,cvs,x0,y0,R,L,r,r1,r2,w,h):
        self.cvs = cvs
        self.x0 = x0
        self.y0 = y0
        self.R = R
        self.L = L
        self.r = r    #底座圆半径
        self.r1 = r1  #曲柄与连杆相交处外圆半径
        self.r2 = r2  #曲柄与连杆相交处内圆半径
        self.w = w    #活塞的宽度
        self.h = h    #活塞筒的半高
        self.move = 1
        self.start = 0
        self.crank = None
        
    def create_static(self):  
        r = self.r
        h = 1.5*r
        R = self.R
        L = self.L
        ch = self.h
        w = self.w
        cvs = self.cvs
        x0,y0 = self.x0,self.y0
        xmin,xmax = x0+L-R-2*w,x0+R+L+2*w
        p = 0.3
        cvs.create_oval(x0-r,y0-r,x0+r,y0+r,outline = "green",width = 3)
        cvs.create_oval(x0-p*r,y0-p*r,x0+p*r,y0+p*r,outline = "green",width = 2)
        cvs.create_line(x0-r,y0,x0-r,y0+h,fill = "red",width = 3)
        cvs.create_line(x0+r,y0,x0+r,y0+h,fill = "red",width = 3)
        cvs.create_line(x0-r,y0+h,x0+r,y0+h,fill = "red",width = 3)
        cvs.create_rectangle(xmin,y0-ch,xmax,y0+ch,width = 3)

    def create_dynamic(self,theta):
        r = self.r
        r1 = self.r1
        r2 = self.r2
        R = self.R
        L = self.L
        h = self.h
        w = self.w
        x1,y1 = x0 + r*cos(theta),y0 + r*sin(theta)
        ox,oy = x0 + R*cos(theta),y0 + R*sin(theta)
        x2,y2 = ox - r1*cos(theta),oy - r1*sin(theta)
        belta = asin(R*sin(theta)/L)
        x3,y3 = ox + r1*cos(belta),oy + r1*sin(belta)
        x4,y4 = x0 + R*cos(theta)+sqrt(L**2-(R*sin(theta))**2),y0
        self.crank = cvs.create_line(x1,y1,x2,y2,fill = "green",width = 4)
        self.outer_circle = cvs.create_oval(ox-r1,oy-r1,ox+r1,oy+r1)
        self.inner_circle = cvs.create_oval(ox-r2,oy-r2,ox+r2,oy+r2)
        self.link = cvs.create_line(x3,y3,x4,y4,fill = "red",width = 4)
        self.plunger = cvs.create_rectangle(x4-w,y4-h,x4+w,y4+h,fill = "cyan",width = 2)

    def delete_all(self):
        cvs = self.cvs
        if self.crank:
            cvs.delete(self.crank)
            cvs.delete(self.outer_circle)
            cvs.delete(self.inner_circle)
            cvs.delete(self.link)
            cvs.delete(self.plunger)

    def rock_and_roll(self,dt = 0.005):
        self.create_static()
        i = self.start
        theta = pi/180*i
        self.create_dynamic(theta)
        while self.move:
            self.delete_all()
            i += 1
            theta = pi/180*i
            self.create_dynamic(theta)
            time.sleep(dt) 
            self.cvs.update()
            if i > 360:
                i = 0
        self.start = i
            
    
window = Tk()
window.title('Motion')
window.geometry("800x600")
cvs = Canvas(window,bg = "Gainsboro")
cvs.pack(fill = BOTH,expand = True)
btn_start = Button(window,text = "运动")
btn_start.pack()
btn_end = Button(window,text = "停止")
btn_end.pack()

x0,y0 = 250,300
r = 30
R = 80
L = 300
w = 10
h = 20
r1,r2 = 6,4
model = Model(cvs,x0,y0,R,L,r,r1,r2,w,h)

def btn_start_click(event):
    model.move = 1
    model.delete_all()
    model.rock_and_roll()

def btn_end_click(event):
    model.move = 0
    
btn_start.bind('<Button-1>',btn_start_click)
btn_end.bind('<Button-1>',btn_end_click)

window.mainloop()







