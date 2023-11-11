
from numpy import linspace, zeros, array
import matplotlib.pyplot as plt
from Temporal_integrator import Euler, RK4, Crank_Nicolson

from Cauchy_Problem import Cauchy_problem






def ejecutar(tf, N, U0):    
        t = linspace(0,tf,N)
        
        
        U=Cauchy_problem(t, U0, Crank_Nicolson )

        plt.axis('equal')
        plt.plot( U[:,0] , U[:,1], "." )            #Grafico los resultados
        plt.show()
        
        
        
ejecutar(tf=10,N=500, U0=array([1,1.]))