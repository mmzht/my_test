# -*- coding: utf-8 -*-
"""
Created on Wed May  9 11:20:27 2018

@author: yaoya
"""
import numpy as np
import matplotlib.pyplot as plt


data = np.array([[40,60],
                 [40,30],
                 [30,40],
                 [40,50],
                 [44,50],
                 [60,30],
                 [60,60],
                 [70,55],
                 [60,65],
                 [70,65],
                 [65,67],
                 [64,65],
                 [80,90],
                 [85,88],
                 [95,90],
                 [80,80],
                 [90,70],
                 [95,95],
                 [98,100]])


target = np.array([0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2])
def make_circle(r,c):
    t = np.arange(0, np.pi * 2.0, 0.01)
    t = t.reshape((len(t), 1))
    x = (r-c[0]) * np.cos(t)
    y = (r-c[1]) * np.sin(t)
    return np.hstack((x, y))

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.axis([0,100,0,100])
plt.scatter(data[:6,0],data[:6,1],marker = 'o')
plt.scatter(data[6:12,0],data[6:12,1],marker = 's')
plt.scatter(data[12:,0],data[12:,1],marker = 'v')
plt.scatter(50,80,marker = '*')
plt.plot([40,50],[60,80])
plt.plot([60,50],[65,80])
plt.plot([80,50],[80,80])
##plt.plot([20,80],[100,20],"--")
##plt.plot([55,90],[90,55],"--")
plt.xlabel(u'到课率(%)')
plt.ylabel(u'作业质量')
plt.axis([0,120,0,120])
plt.show()
