
import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace 
import sys
sys.path.append('..')  

from ..Milestone_1.Kepler_Euler import F_Kepler
from ..Milestone_1.Kepler_Euler import Euler
import Cauchy_Problem



def Euler_function(tf, N, U0):
    
    t = linspace(0,tf,N)

    temporal_integrator = Euler
    U = Cauchy_Problem(F_Kepler, t, U0, temporal_integrator)
    plt.plot( U[:,0] , U[:,1], "." )
    plt.show()



Euler_function(100,100, array([1,0,0,1]))










    
