
import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace 
from Temporal_integrator import Euler, Crank_Nicolson, RK4
from Cauchy_Problem import Cauchy_problem




def Milestone_function(tf, N, U0):     #Defino la función que resolverá el problema de Cauchy con los argumentos de tiempo final, número de iteraciones y las condiciones iniciales
    
    t = linspace(0,tf,N)            #Creo el vector de tiempos
    temporal_scheme = RK4


    U = Cauchy_problem(t, U0, temporal_scheme)       #La solución la resulvo llamndo a problema de Cauchy metiendo en el primer argumento al F de Kepler

    plt.axis('equal')
    plt.plot( U[3000:N,0] , U[3000:N,1] )            #Grafico los resultados
    plt.grid()
    plt.show()
    plt.plot( t[3000:N],U[3000:N,0])
    plt.grid
    plt.show()



Milestone_function(tf=100,N=5000, U0=array([1,1]))  #Llamo a la función que va a resolver el problema de Cauchy introduciendo los parámetos










    
