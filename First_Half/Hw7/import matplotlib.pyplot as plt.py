import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
x=np.arange(0,5.1,0.1,dtype=float)
y=(x**3-4*x**2+x)*sin(5*x)
y1=(3*x**2-8*x)*sin(5*x)+sin(5*x)+(5*x**3-20*x**2+5*x)*cos(5*x)
y2=(-25*x**3+100*x**2-19*x)*sin(5*x)-8*sin(5*x)+(30*x**2-80*x)*cos(5*x)+10*cos(5*x)
func=plt.subplot(311)
plt.plot(x,y)
plt.grid()
plt.plot(np.argmax(y)*0.1,np.amax(y),'ro')
plt.plot(np.argmin(y)*0.1,np.amin(y),'go') 
plt.plot(x,y[30]+y1[30]*(x-x[30]))
plt.plot(x,y[30]-(x-x[30])/y1[30])
deriviative1=plt.subplot(323)
plt.plot(x,y1)
plt.grid()
deriviative2=plt.subplot(324)
plt.plot(x,y2)
plt.grid()
func1=plt.subplot(313)
plt.plot(x,y)
for i in range(2,10):
    plt.plot(x[5*i-3:5*i+3],y[5*i]+y1[5*i]*(x[5*i-3:5*i+3]-x[5*i]),'r')
length=sum(np.sqrt((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2) for i in range(len(x)))
print(length)
plt.grid()
plt.show()