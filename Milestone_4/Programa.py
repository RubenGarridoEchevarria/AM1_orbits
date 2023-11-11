
from numpy import linspace, zeros, array
import matplotlib.pyplot as plt
from Temporal_integrator import Euler

from Cauchy_Problem import Cauchy_problem






def ejecutar(tf, N, U0):    
        t = linspace(0,tf,N)
        
        
        U=Cauchy_problem(t, U0, Euler )

        plt.axis('equal')
        plt.plot( U[:,0] , U[:,1], "." )            #Grafico los resultados
        plt.show()
        
        
        
ejecutar(tf=10,N=500, U0=array([0.,0.]))