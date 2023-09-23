
##Milestone 1 Kepler usando Rounge-Kutta de cuarto orden


from numpy import array, zeros
import matplotlib.pyplot as plt

u = array( [1, 0, 0, 1] )  #Condición inicial de la ecuación diferncial
n=7500                    #Número de pasos de tiempo
dt=0.001                   #Paso de tiempo 

x = array( zeros(n) )     #Posición x del vector de posición   
y = array( zeros(n))      #Posición y del vector de posición

x[0] = u[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y[0] = u[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y





for i in range(0,n):

    F1 = array( [ u[2], u[3], -u[0]/(u[0]**2+u[1]**2)**1.5 , -u[1]/( u[0]**2 + u[1]**2)**1.5] )  #Froumula de F=[dot(rx), dot(ry), dot(dot(rx)), dot(dot(ry))] velocidad en x y en y, aceleración en x y en y

    K1 = dt * F1
    
    F2 = array( [ (u[2]+1/2*K1),  (u[3]+1/2*K1), -(u[0]+1/2*dt)/((u[0]+1/2*dt)**2+(u[1]+1/2*dt)**2)**1.5] )

    K2 = dt * F2

    F3 = array( [ (u[2]+1/2*K2),  (u[3]+1/2*K2), -(u[0]+1/2*dt)/((u[0]+1/2*dt)**2+(u[1]+1/2*dt)**2)**1.5] )

    K3 = dt * F3

    F4 = array( [ (u[2]+K3),  (u[3]+K3), -(u[0]+dt)/((u[0]+dt)**2+(u[1]+dt)**2)**1.5] )

    K4 = dt*F4

    print(K4)


    u = u + 1/6*(K1 + 2*K2 + 2*K3 + K4)
    print(u)

    #x[i] = u[0]           #Meto las nueva componente calculada de la coordenada x en la matrix de x
    #y[i] = u[1]           #Meto la nuueva componente calculada de la coordenada y en la matrix de y


#plt.plot(x,y)
#plt.show()

