import matplotlib.pyplot as plt
import numpy as n
sx=[]
sy=[]
def f(t,x,y):
    
    return 5*x-2*y

def g(t,x,y):
    
    return  3*x

t=0
x0=1 #initial value of x
y0=2 #initial value of  y both are given
h=0.2

while(t<=1):
    
    print("t={}       x0={}      y0={}".format(t,x0,y0))
    G1=h*f(t,x0,y0)
    M1=h*g(t,x0,y0)
    
    G2=h*f(t+h/2,x0+G1/2,y0+M1/2)
    M2=h*g(t+h/2,x0+G1/2,y0+M1/2)
    
    G3=h*f(t+h/2,x0+G2/2,y0+M2/2)
    M3=h*g(t+h/2,x0+G2/2,y0+M2/2)
    
    G4=h*f(t+h,x0+G3,y0+M3)
    M4=h*g(t+h,x0+G3,y0+M3)

    G=(1/6)*(G1+2*(G2+G3)+G4)
    M=(1/6)*(M1+2*(M2+M3)+M4)
    
    x=x0+G #'''value of theta'''
    y=y0+M#'''value of velocity'''
    
    sx.append(x)
    sy.append(y)
    x0=x
    y0=y
    
    t=t+h
    
plt.plot(sx,sy ,'ko')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
#plt.title("The angular velocity ω versus the angle θ")
plt.show()
