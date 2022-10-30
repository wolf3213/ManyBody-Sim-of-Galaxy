import math
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import numpy as np
def R12(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
def F(G,m1,m2,x1,x2,y1,y2):
    return G*m1*m2/R_12(x1,x2,y1,y2)
def plot(x1,y1):
    plt.plot(x1, y1, 'r.')

x=[];y=[];vx=[];vy=[];ax=[];ay=[];m=[]
G=1.0
dt=10.0
tend=3000.0
N=200#number of stars
x.append(0.0)
y.append(0.0)
m.append(400000.0)
vx.append(0.0)
vy.append(0.0)
ax.append(0.0)
ay.append(0.0)
q=0 #index for plotting
_nums_plot=500
all_names = []
for i in range(1, (_nums_plot + 1)):
    str_zeros = ""
    zeros_to_write = int(math.log10(_nums_plot)) - int(math.log10(i))

    for j in range(0, zeros_to_write):
        str_zeros = str_zeros + '0'
    name = str_zeros + str(i)
    all_names.append(name)


for i in np.arange(1,50,1):
    x.append(-5000.0+(i-1)*100)
    y.append(0)
    m.append(1.0)
    vx.append(0)
    vy.append(-math.sqrt(G*m[0]/R12(x[0],x[i],y[0],y[i])))
    ax.append(0.0)
    ay.append(0.0)
for i in np.arange(50,100,1):
    x.append(-5000.0+(i-1)*101)
    y.append(0)
    m.append(1.0)
    vx.append(0)
    vy.append(math.sqrt(G*m[0]/R12(x[0],x[i],y[0],y[i])))
    ax.append(0.0)
    ay.append(0.0)
for i in np.arange(100,150,1):
    x.append(0)
    y.append(-5000.0+(i-100)*100)
    m.append(1.0)
    vy.append(0)
    vx.append(math.sqrt(G*m[0]/R12(x[0],x[i],y[0],y[i])))
    ax.append(0.0)
    ay.append(0.0)
for i in np.arange(150,201,1):
    x.append(0)
    y.append(-5000.0+(i-100)*101)
    m.append(1.0)
    vy.append(0)
    vx.append(-math.sqrt(G*m[0]/R12(x[0],x[i],y[0],y[i])))
    ax.append(0.0)
    ay.append(0.0)
for t in np.arange(0.0,tend,dt):
    plt.plot(x[0], y[0], 'k+')
    plt.xlim(xmin=-6000,xmax=6000)
    plt.ylim(ymin=-6000,ymax=6000)
    for i in np.arange(1,N+1,1):
        plot(x[i],y[i])
    plt.grid(b=True, which="major", color='#666666', linestyle='-', linewidth=0.2)
    plt.savefig("d"+all_names[q]+".png",dpi=500)
    for i in np.arange(1,N+1,1):
        for j in np.arange(0, N + 1, 1):
            if i!=j:
                ax[i]+=G*m[i] * m[j] *(x[j]-x[i])/(R12(x[i],x[j],y[i],y[j])**3)
                ay[i]+= G * m[i] * m[j] * (y[j] - y[i]) / (R12(x[i],x[j],y[i],y[j])**3)
    for i in np.arange(1,N+1,1):
        vx[i]+=ax[i]*dt
        vy[i]+=ay[i]*dt
    for i in np.arange(1,N+1,1):
        x[i]=x[i]+vx[i]*dt
        y[i]=y[i]+vy[i]*dt

    if t % 1.0 == 0.0:
        print(t)
    for i in np.arange(1,N+1,1):
        ax[i]=0.0
        ay[i]=0.0
    plt.figure()
    q=q+1

