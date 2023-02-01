import numpy as np
import matplotlib.pyplot as plt


#E in eV
#Length in nm
#h -use and hd =1240eV
#hbar -c use197 eV*nm
#mass in mc^2 mass of electron = 511000

a=1 #lengthbof well
U=0 #potential inside the well
#k=1 #this is equal to 2m/hbar^2
m=511000 
hbc=197
k=2*m/hbc**2

E=0 # 0.375
dE=0.001

psi=0
dpsi=1

x=0
dx=0.001

psip=[]
xp=[]

psifinal=1
while abs(psifinal)>0.002:
    x=0
    dpsi=1/np.sqrt(0.05123183508607787)
    #dpsi=1/np.sqrt(0.005661905900486636)
    xp=[]
    psip=[]
    while x<a:
        ddpsi=-k*(E-U)*psi
        dpsi=dpsi+ddpsi*dx
        psi=psi+dpsi*dx
        x=x+dx
        psip=psip+[psi]
        xp=xp+[x]
    psifinal=psi     
    E=E+dE
print("E =",E,"eV")
print("psifinal =",psifinal)
plt.plot(xp,psip)
plt.xlabel("x")
plt.ylabel("psi")
plt.grid()
plt.show()    


Area=0
for i in range(len(psip)-1):
    dA=(psip[i]**2)*dx
    Area=Area+dA
print("Area=",Area)    