
from numpy import array
from numpy import zeros
from numpy import linspace
import matplotlib.pyplot as plt




#Condición inicial



U1 = array([1.75, 2.25])

U2 = array([2, 3])

U3 = array([1.3, 2.6])

U4 = array([-2, 6])


dt=0.01

n=2000
t=linspace(0,4,n)

x1 = array( zeros(n) )     #Posición x del vector de posición   
y1 = array( zeros(n))      #Posición y del vector de posición

x2 = array( zeros(n) )     #Posición x del vector de posición   
y2 = array( zeros(n))      #Posición y del vector de posición

x3 = array( zeros(n) )     #Posición x del vector de posición   
y3 = array( zeros(n))      #Posición y del vector de posición

x4 = array( zeros(n) )     #Posición x del vector de posición   
y4 = array( zeros(n))      #Posición y del vector de posición



x1[0] = U1[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y1[0] = U1[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y


x2[0] = U2[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y2[0] = U2[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y


x3[0] = U3[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y3[0] = U3[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y

x4[0] = U4[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y4[0] = U4[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y

for i in range(0,n):

    F1=array([1-4*U1[0]+U1[0]**2*U1[1], 3*U1[0]-U1[0]**2*U1[1]])       #Meter la matriz del sistema de ecuaciones diferenciales con U[0] = x, U[1] = y
    F2=array([1-4*U2[0]+U2[0]**2*U2[1], 3*U2[0]-U2[0]**2*U2[1]])
    F3=array([1-4*U3[0]+U3[0]**2*U3[1], 3*U3[0]-U3[0]**2*U3[1]])
    F4=array([1-4*U4[0]+U4[0]**2*U4[1], 3*U4[0]-U4[0]**2*U4[1]])

    U1 = U1 + dt * F1
    U2 = U2 + dt * F2
    U3 = U3 + dt * F3
    U4 = U4 + dt * F4

    x1[i] = U1[0]
    y1[i] = U1[1]

    x2[i] = U2[0]
    y2[i] = U2[1]

    x3[i] = U3[0]
    y3[i] = U3[1]

    x4[i] = U4[0]
    y4[i] = U4[1]


plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)

plt.grid()
plt.show()
plt.grid()


plt.plot(t,x1)
plt.plot(t,x2)
plt.plot(t,x3)
plt.plot(t,x4)

plt.show()