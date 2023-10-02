    
##Milestone 1 Kepler usando Euler explícito


from numpy import array, zeros
import matplotlib.pyplot as plt

U = array( [1, 0, 0, 1] )  #Condición inicial de la ecuación diferncial
n=63000                    #Número de pasos de tiempo
dt=0.01                   #Paso de tiempo 

x = array( zeros(n) )     #Posición x del vector de posición   
y = array( zeros(n))      #Posición y del vector de posición

x[0] = U[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y[0] = U[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y


def F_Kepler(U):            #Programa con el paradigma funcional 
   
   
   
   x, y, Vx, Vy = U[0], U[1], U[2], U[3]
   mr = (x**2 + y**2)**1.5
   
   
   return array( [Vx , Vy , -x/mr, -y/mr] )




for i in range(0,n):

    F = array( [ U[2], U[3], -U[0]/(U[0]**2+U[1]**2)**1.5 , -U[1]/( U[0]**2 + U[1]**2)**1.5] )  #Froumula de F=[dot(rx), dot(ry), dot(dot(rx)), dot(dot(ry))] velocidad en x y en y, aceleración en x y en y

    F_f=F_Kepler(U)         #Llamada a la función del paradigma funcional

    U = U + dt * F_f

    x[i] = U[0]           #Meto las nueva componente calculada de la coordenada x en la matrix de x
    y[i] = U[1]           #Meto la nuueva componente calculada de la coordenada y en la matrix de y

plt.axis('equal')
plt.plot(x,y)
plt.show()


def Euler(U, dt, t, F):

    return U + dt * F(U,t)