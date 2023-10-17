
from numpy import array
from numpy import zeros
from numpy import linspace
import matplotlib.pyplot as plt

U_x=linspace(-5,1,5)
U_y=linspace(-5,1,5)






dt=0.01

n=2000


x = array( zeros(n) )     #Posición x del vector de posición   
y = array( zeros(n))      #Posición y del vector de posición

x[0] = U_x[0]                 #Asigno el primer valor de la x del vector de posición al primer valor de la condición inicial de u en x
y[0] = U_y[1]                 #Asigno el primer valor de la y del vector de posición al primer valor de la condición inicial de u en y

print(x)
for j in range(0,9):

        U = array([U_x[j],U_y[j]])
        print(U)
        for i in range(0,n):

    

            F=array([-3/2 * U[0] + U[1] , -1/4*U[0] - 1/2*U[1]])
            U = U + dt * F

            x[i] = U[0]
            y[i] = U[1]
        plt.plot(x,y)
        plt.show()      



