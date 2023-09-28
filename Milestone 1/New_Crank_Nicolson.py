
from numpy import array, zeros
from scipy.optimize import newton
import matplotlib.pyplot as plt

n=6000  
dt=0.01  

U = array( [1, 0, 0, 1] )  #Condición inicial de la ecuación diferncial

def F_Kepler(U):            #Programa con el paradigma funcional 
   
   
   
   x, y, Vx, Vy = U[0], U[1], U[2], U[3]
   mr = (x**2 + y**2)**1.5
   
   
   return array( [Vx , Vy , -x/mr, -y/mr] )
     


def G(x):

    return x-U-dt/2*(F_Kepler(U)+F_Kepler(x))


for i in range(1,n):

    U=newton(G, U)

