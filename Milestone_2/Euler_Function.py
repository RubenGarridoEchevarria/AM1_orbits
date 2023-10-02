
import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace 
from Milestone_1.Kepler_Euler import Euler
from Milestone_1.Kepler_Euler import F_Kepler
import Cauchy_Problem



def Euler(tf, N, U0):
    
    t = linspace(0,tf,N)

    temporal_integrator = Euler
    U = Cauchy_Problem(F_Kepler, t, U0, Euler)










    
