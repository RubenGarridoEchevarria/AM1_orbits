
from numpy import zeros
from numpy import array

def Cauchy_problem(F,t, U0, Kepler_Euler):
    
    N = len(t)-1
    Nv = len(U0)
    U = zeros((N+1,Nv))
    U[0,:] = U0

    for i in range(N):

        U[i+1,:] = Euler( U[i, :], t[i+1] - t[i], t[i],  F)


    return U
    
