
import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace 
from Temporal_integrator import Euler, Crank_Nicolson 
from Kepler_Orbits import F_Kepler
from Cauchy_Problem import Cauchy_problem




def Euler_function(tf, N, U0):
    
    t = linspace(0,tf,N)

    temporal_scheme = [(Euler), Crank_Nicolson]

    for (method) in temporal_scheme:


        U = Cauchy_problem(F_Kepler, t, U0, method)




    plt.plot( U[:,0] , U[:,1], "." )
    plt.show()



Euler_function(tf=100,N=100, U0=array([1,0,0,1]))










    
