
from numpy import array


def Oscillator(U,t): 
    
    U = array ( [ U[1], -U[0] ] )
    return U