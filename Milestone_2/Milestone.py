
import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace 
from Temporal_integrator import Euler, Crank_Nicolson 
from Kepler_Orbits import F_Kepler
from Cauchy_Problem import Cauchy_problem




def Milestone_function(tf, N, U0):
    
    t = linspace(0,tf,N)

    temporal_scheme = [(Euler), (Crank_Nicolson)]

    U = Cauchy_problem(F_Kepler, t, U0, temporal_scheme=Euler)




    plt.plot( U[:,0] , U[:,1], "." )
    plt.show()



Milestone_function(tf=100,N=100, U0=array([1,0,0,1]))










    
