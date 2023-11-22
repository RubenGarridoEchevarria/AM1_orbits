
from numpy import array
from math import cos

def Duffin_Oscilator(U,t):
    
    return array([U[1], U[0]-U[0]**3])



def Duffin_Osciliator_2(U,t):
    k = 0.01
    B = 1 
    
    return array ( [U[1], -U[0]**3-k*U[1]+B*cos(t)] )


def Rayleigh_Osocilator(U,t):
    
    f0 = 1
    
    return array([ U[1] , U[0] - U[0]**3 - U[1] + f0*cos(t) ])

