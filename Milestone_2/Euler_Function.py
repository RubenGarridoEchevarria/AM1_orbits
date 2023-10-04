
import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace 
from Temporal_integrator import Euler
from Kepler_Orbits import F_Kepler
import Cauchy_Problem




def Euler_function(tf, N, U0):
    
    t = linspace(0,tf,N)

    temporal_integrator = Euler
    U = Cauchy_Problem(F_Kepler, t, U0, temporal_integrator=Euler)
    plt.plot( U[:,0] , U[:,1], "." )
    plt.show()



Euler_function(tf=100,N=100, U0=array([1,0,0,1]))










    
