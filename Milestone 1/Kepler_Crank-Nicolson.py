
##Milestone 1 Kepler usando Crank-Nicolson

from numba import njit
from numpy import array, zeros
from scipy.optimize import newton
import matplotlib.pyplot as plt

u = array( [1, 0, 0, 1] )  #Condición inicial de la ecuación diferncial
U = array( [1, 0, 0, 1] )  #Condición inicial de la ecuación diferncial

n=66                   #Número de pasos de tiempo
dt=0.1                   #Paso de tiempo 

x = array( zeros(n) )     #Posición x del vector de posición   
y = array( zeros(n))      #Posición y del vector de posición

def F_Kepler(U):            #Programa con el paradigma funcional 
   
   
   
   x, y, Vx, Vy = U[0], U[1], U[2], U[3]
   mr = (x**2 + y**2)**1.5
   
   
   return array( [Vx , Vy , -x/mr, -y/mr] )


x[0] = u[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y[0] = u[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y

for i in range(0,n):

    F_e = array( [ u[2], u[3], -u[0]/(u[0]**2+u[1]**2)**1.5 , -u[1]/( u[0]**2 + u[1]**2)**1.5] )  #Froumula de F=[dot(rx), dot(ry), dot(dot(rx)), dot(dot(ry))] velocidad en x y en y, aceleración en x y en y

    # Para calcular la solución u en el tiempo siguiente con Crank-Nicolsón necesito F en el punto siguiente

    u_e = u + dt * F_e 

    # Una vez calculada la solución con Euler vuelvo a calcular F con esa solución

    F_CN = array( [ u_e[2], u_e[3], -u_e[0]/(u_e[0]**2+u_e[1]**2)**1.5 , -u_e[1]/( u_e[0]**2 + u_e[1]**2)**1.5] )

    # Por último calculo la solución final del problema con la expresión de Crank-Nicolson 

    u = u + 1/2 * dt * ( F_CN + F_e )

    x[i] = u[0]           #Meto las nueva componente calculada de la coordenada x en la matrix de x
    y[i] = u[1]           #Meto la nuueva componente calculada de la coordenada y en la matrix de y

plt.axis('equal')
plt.plot(x,y)
plt.show()



# Metodo alternativo para Crank-Nicolson???
 
@njit

def Crank_Nicolson(U, dt, t, F_Kepler ): 
    
    def Residual_CN(X): 
         
         
         return  X - a - dt/2 *  F_Kepler(X, t + dt)

    a = U  +  dt/2 * F_Kepler( U, t)  
    return newton( Residual_CN, U )


print(U)



