
from numpy import array
from math import cos

def Duffin_Oscilator(U,t):
    
    return array([U[1], U[0]-U[0]**3])



def Duffin_Osciliator_2(U,t):
    k = 0.01
    B = 1 
    
    return array ( [U[1], -U[0]**3-k*U[1]+B*cos(t)] )


def Rayleigh_Osocilator(U,t):
    
    f0 = 0.8
    
    return array([ U[1] , U[0] - U[0]**3 - U[1] + f0*cos(t) ])

def Lorentz(U,t):
    
    b = 8/3
    r = 28
    s = 10
    
    return array([ - s*U[0] + s*U[1], r*U[0] - U[0]*U[2] - U[1], - b*U[2] + U[0]*U[1]])


def Rossler(U,t):
    
    a = 0.398
    b = 2
    c = 4
    
    return array([-U[1] - U[2], a*U[1] + U[0], b+U[2]*(U[0]-c)])