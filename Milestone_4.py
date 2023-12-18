
from numpy import linspace, zeros, array
import matplotlib.pyplot as plt
from Funciones_Auxiliares.Temporal_integrator import Euler, RK4, Crank_Nicolson

from Funciones_Auxiliares.Cauchy_Problem_Con_F import Cauchy_problem
from Funciones_Auxiliares.Oscilador import Oscillator
from Funciones_Auxiliares.Region_estabilidad import test_Stability_region






def ejecutar(tf, N, U0):    
        t = linspace(0,tf,N)
        
        
        U=Cauchy_problem(t, U0, Crank_Nicolson, Oscillator )

        plt.axis('equal')
        plt.plot( U[:,0] , U[:,1], "." )            #Grafico los resultados
        plt.show()
        
        
        
ejecutar(tf=10,N=500, U0=array([1,1.]))

test_Stability_region()