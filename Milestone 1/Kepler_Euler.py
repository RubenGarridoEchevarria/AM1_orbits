    
##Milestone 1 Kepler usando Euler explícito


from numpy import array, zeros
import matplotlib.pyplot as plt

u = array( [1, 0, 0, 1] )  #Condición inicial de la ecuación diferncial
n=63000                    #Número de pasos de tiempo
dt=0.0001                   #Paso de tiempo 

x = array( zeros(n) )     #Posición x del vector de posición   
y = array( zeros(n))      #Posición y del vector de posición

x[0] = u[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y[0] = u[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y


def F_Kepler(u):            #Programa con el paradigma funcional 
   
   
   
   x, y, Vx, Vy = u[0], u[1], u[2], u[3]
   mr = (x**2 + y**2)**1.5
   
   
   return array( [Vx , Vy , -x/mr, -y/mr] )




for i in range(0,n):

    F = array( [ u[2], u[3], -u[0]/(u[0]**2+u[1]**2)**1.5 , -u[1]/( u[0]**2 + u[1]**2)**1.5] )  #Froumula de F=[dot(rx), dot(ry), dot(dot(rx)), dot(dot(ry))] velocidad en x y en y, aceleración en x y en y

    F_f=F_Kepler(u)         #Llamada a la función del paradigma funcional

    u = u + dt * F_f

    x[i] = u[0]           #Meto las nueva componente calculada de la coordenada x en la matrix de x
    y[i] = u[1]           #Meto la nuueva componente calculada de la coordenada y en la matrix de y

plt.axis('equal')
plt.plot(x,y)
plt.show()

del()