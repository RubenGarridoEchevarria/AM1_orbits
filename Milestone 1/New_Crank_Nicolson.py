
from numpy import array, zeros
from scipy.optimize import newton
import matplotlib.pyplot as plt

n=3000 
dt=0.1

U = array( [1, 0, 0, 1] )  #Condición inicial de la ecuación diferncial
x = array( zeros(n) )     #Posición x del vector de posición   
y = array( zeros(n))      #Posición y del vector de posición

x[0] = U[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y[0] = U[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y


def F_Kepler(U):            #Programa con el paradigma funcional definición de la función de Kepler
   
   
   
   x, y, Vx, Vy = U[0], U[1], U[2], U[3]
   mr = (x**2 + y**2)**1.5
   
   
   return array( [Vx , Vy , -x/mr, -y/mr] )
     


def G(X):

    return X-U-dt/2*(F_Kepler(U)+F_Kepler(X))


for i in range(1,n):

    U=newton(G, U)
    x[i] = U[0]           
    y[i] = U[1]  


plt.plot(x,y)
plt.show()

