
##Milestone 1 Kepler usando Crank-Nicolson

from numpy import array, zeros
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

u = array( [1, 0, 0, 1] )  #Condición inicial de la ecuación diferncial
u_2 = array( [1, 0, 0, 1] )
n=6300                  #Número de pasos de tiempo
dt=0.001                   #Paso de tiempo 

x = array( zeros(n) )     #Posición x del vector de posición   
y = array( zeros(n))      #Posición y del vector de posición

x_2 = array( zeros(n) )     #Posición x del vector de posición   
y_2 = array( zeros(n))      #Posición y del vector de posición

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

plt.plot(x,y)
plt.show()



# Metodo alternativo para Crank-Nicolson???

def CrankNicolson( dt, u_2 , n ):

    for i in range(n):

        def CN_res(x):

            return x - u_temp - dt/2 * F_e(x)
        
        u_temp = u_2 [:,i] + dt/2 * F_e( u_2[:,i] )

        u_2[:,i+1] = fsolve(CN_res, u_2[:,i])

        x_2[i] = u_2[0]
        y_2[i] = u_2[1]
 

    return u_2


plt.plot(x_2,y_2)
plt.show()



