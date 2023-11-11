from numpy import array, zeros, linspace ,abs,transpose, float64
import matplotlib.pyplot as plt
from Temporal_integrator import Euler,RK4,Crank_Nicolson


def Stability_Region( Scheme , N , x0 , xf , y0 , yf):
    
    x, y = linspace( x0 , xf , N ), linspace( y0 , yf , N )

    rho = zeros((N , N), dtype=float64)

    for i in range( N ):
        for j in range( N ):


            w = complex(x[i],y[j])
            r = Scheme( 1., 1. , 0., lambda u, t:w*u)   #Lambda crea una función como def pero sin nombre
            rho[i,j]=abs(r)

    return rho, x, y  

def test_Stability_region():

    schemes = [RK4, Euler, Crank_Nicolson]

    for scheme in schemes:

        rho, x, y = Stability_Region (scheme,100,-4,2,-4,4)
       
        plt.contour(x,y, transpose(rho), linspace(0,1,11))
        plt.axis("equal")
        plt.grid()
        plt.show()


test_Stability_region()