from scipy import integrate,optimize
import numpy as np
from matplotlib import pyplot as plt

L=10
psi_0=0 # also psi_l=0
dpsi_0=1 # arbitary (nonzer0); we will normalize later

def f(t,y,E):
    psi,dpsi= y
    return dpsi,-E*psi

@np.vectorize    
def psi_L(E):
    sol=integrate.solve_ivp(lambda t,y : f(t,y,E),[0,L],[psi_0,dpsi_0])
    psi,dpsi=sol.y
    return psi[-1]
E=np.linspace(0,1,200)   
plt.plot(E,psi_L(E))
plt.grid()
plt.axhline(c="k")
plt.show()

# solution near 0.1,0.4,0.9

energy=[]
for guess in [0.1,0.4,0.9]:
    E=optimize.newton(psi_L,guess)
    energy.append(E)
    print(E)

'''
output:- 
0.09865605091459564
0.3945907560080154
0.8877757178384136   '''    

# plot eigenfunction(wave functions)
x=np.linspace(0,L,100)
for E in energy:
    sol=integrate.solve_ivp(lambda t,y : f(t,y,E),[0,L],[psi_0,dpsi_0],t_eval=x)
    psi,dpsi=sol.y
    plt.plot(x,psi)
plt.axhline(c="k")
plt.xlim(0,L)
plt.show()    

''' normalization condition-  ∫ |ψ(x)^2| dx=1  '''

for E in energy:
    sol=integrate.solve_ivp(lambda t,y : f(t,y,E),[0,L],[psi_0,dpsi_0],t_eval=x)
    psi,dpsi=sol.y
    norm=np.sqrt(integrate.simps(psi**2,x))
    plt.plot(x,psi/norm)
plt.axhline(c="k")
plt.xlim(0,L)
plt.show() 
