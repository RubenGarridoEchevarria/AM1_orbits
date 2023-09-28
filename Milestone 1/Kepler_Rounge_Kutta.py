
##Milestone 1 Kepler usando Runge-Kutta de cuarto orden


from numpy import array, zeros
import matplotlib.pyplot as plt

u = array( [1, 0, 0, 1] )  #Condición inicial de la ecuación diferncial
n=6300                    #Número de pasos de tiempo
dt=0.001                   #Paso de tiempo 

x = array( zeros(n) )     #Posición x del vector de posición   
y = array( zeros(n))      #Posición y del vector de posición

x[0] = u[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y[0] = u[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y



def F_Kepler(u):            #Programa con el paradigma funcional 
   
   
   
   x, y, Vx, Vy = u[0], u[1], u[2], u[3]
   mr = (x**2 + y**2)**1.5
   
   
   return array( [Vx , Vy , -x/mr, -y/mr] )

for i in range(0,n):

    F1 = array( [ u[2], u[3], -u[0]/(u[0]**2+u[1]**2)**1.5 , -u[1]/( u[0]**2 + u[1]**2)**1.5] )  #Froumula de F=[dot(rx), dot(ry), dot(dot(rx)), dot(dot(ry))] velocidad en x y en y, aceleración en x y en y

    K10 = dt * F1[0]                            # Calculo una función de Runge-Kutta para cada componente del vector F
    K11 = dt * F1[1]
    K12 = dt * F1[2]
    K13 = dt * F1[3]

    K20 = dt * (F1[0] + 1/2 * K12)
    K21 = dt * (F1[1] + 1/2 * K13)
    K22 = dt * F1[2]
    K23 = dt * F1[3]

    K30 = dt * (F1[0] + 1/2 * K22)
    K31 = dt * (F1[1] + 1/2 * K23)
    K32 = dt * F1[2]
    K33 = dt * F1[3]

    K40 = dt * (F1[0] + K32)
    K41 = dt * (F1[1] + K33)
    K42 = dt * F1[2]
    K43 = dt * F1[3]


    u = array ( [ u[0] + (K10 + 2*K20 + 2*K30 + K40)/6 ,
                  u[1] + (K11 + 2*K21 + 2*K31 + K41)/6 ,
                  u[2] + (K12 + 2*K22 + 2*K32 + K42)/6 ,
                    u[3] + (K13 + 2*K23 + 2*K33 + K43)/6 ] )    # Con las funciones de Runge- kutta calculo el siguiente paso temporal de u
    



    x[i] = u[0]           #Meto las nueva componente calculada de la coordenada x en la matrix de x
    y[i] = u[1]           #Meto la nuueva componente calculada de la coordenada y en la matrix de y

plt.axis('equal')
plt.plot(x,y)
plt.show()

del()