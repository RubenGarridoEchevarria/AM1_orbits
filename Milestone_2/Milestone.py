
import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace 
from Temporal_integrator import Euler, Crank_Nicolson 
from Kepler_Orbits import F_Kepler
from Cauchy_Problem import Cauchy_problem




def Milestone_function(tf, N, U0):     #Defino la función que resolverá el problema de Cauchy con los argumentos de tiempo final, número de iteraciones y las condiciones iniciales
    
    t = linspace(0,tf,N)            #Creo el vector de tiempos

    temporal_scheme =  Euler        #Eligo que integrador temporal que va a usar para resolver el programa

    U = Cauchy_problem(F_Kepler, t, U0, temporal_scheme)       #La solución la resulvo llamndo a problema de Cauchy metiendo en el primer argumento al F de Kepler

    plt.plot( U[:,0] , U[:,1], "." )            #Grafico los resultados
    plt.show()
    print(U)



Milestone_function(tf=100,N=5000, U0=array([1,0,0,1]))  #Llamo a la función que va a resolver el problema de Cauchy introduciendo los parámetos










    
