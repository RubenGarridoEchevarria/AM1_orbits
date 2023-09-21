


from numpy import array,zeros
import matplotlib.pyplot as plt

def F_Kepler(U):
   
   
   
   x, y, Vx, Vy = U[0], U[1], U[2], U[3]
   mr = (x**2 + y**2)**1.5
   
   
   return array( [Vx , Vy , -x/mr, -y/mr] )

N = 100
print(N)
U = array([1,0,0,1])
dt = 0.01
x = array( zeros (N) )
y = array (zeros (N) )

x[0]= U[0]
y[0]= U[0]

 
for i in range(0,N):
   
   F = array( [U[2], U[3] , -U[0]/(U[0]**2+U[1]**2)**1.5 , -U[1]/(U[0]**2+U[1]**2)**1.5] )
   #F=F_Kepler(U)  #El paradigma segundo puedo quitar la línea de arriba y va a funcionar igual.
   U = U + dt*F
   x[i] = U[0]
   y[i] = U[1]
    
    
plt.plot(x,y)
plt.show()