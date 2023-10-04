
from numpy import zeros

from Temporal_integrator import Euler

def Cauchy_problem(F,t, U0, Integrador_temporal):
    
    N = len(t)-1
    Nv = len(U0)
    U = zeros((N+1,Nv))
    U[0,:] = U0

    for i in range(N):

        U[i+1,:] = Integrador_temporal( U[i, :], t[i+1] - t[i], t[i],  F)


    return U
    
