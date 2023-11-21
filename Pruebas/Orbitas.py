
from numpy import array
from numpy import zeros
from numpy import linspace, reshape
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




#Condición inicial



U1 = array([1, -1, 1])




dt=0.01

n=20000
t=linspace(0,4,n)
a = 0.398
b = 2
c = 4
r = 28
s = 10



x1 = array( zeros(n) )     #Posición x del vector de posición   
y1 = array( zeros(n))      #Posición y del vector de posición
z1 = array( zeros(n))





x1[0] = U1[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y1[0] = U1[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y
z1[0] = U1[2]
 


for i in range(0,n):

    F1=array([-U1[1] - U1[2], a*U1[1] + U1[0], b+U1[2]*(U1[0]-c)])       #Meter la matriz del sistema de ecuaciones diferenciales con U[0] = x, U[1] = y
  

    U1 = U1 + dt * F1
    

    x1[i] = U1[0]
    y1[i] = U1[1]
    z1[i] = U1[2]

    


plt.plot(x1,y1)

plt.grid()
plt.show()
plt.grid()


plt.plot(t,x1)


plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.plot(x1,y1,z1)

plt.show()