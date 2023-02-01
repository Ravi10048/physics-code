'''Ball undergoing free fall
            d^2y/dt^2=-g 
   Starting at y0=0 find v0 that result in ball landing at t=10s  '''

import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate,optimize


g=9.8
y0=0
tf=10

def f(t,r):
    y,v=r
    dy_dt=v
    dv_dt=-g
    return dy_dt,dv_dt


@np.vectorize    
def find():
    sol=integrate.solve_ivp(f,(0,tf),(y0,v0),t_eval=t)
    y,v=sol.y
    return y
v0=60 # guessing
t=np.linspace(0,tf,51)

plt.plot(t,find(),".")
plt.show()

@np.vectorize 
def yf(v0):
    sol=integrate.solve_ivp(f,(0,tf),(y0,v0))
    y,v=sol.y
    return y[-1]
v0=np.linspace(0,100,100)
plt.plot(v0,yf(v0))
plt.grid()
plt.axhline(c="k")
plt.show()    

#use the secant method 

v0=optimize.newton(yf,50)
print("V0 =",v0)


#Use that v0 to plot actual solution

plt.plot(t,find(),".")
plt.show()


