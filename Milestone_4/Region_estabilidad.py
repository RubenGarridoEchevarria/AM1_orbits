from numpy import array, zeros, linspace ,abs,transpose, float64
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Temporal_integrator import Euler,RK4,Crank_Nicolson


def Stability_Region( Scheme , N , x0 , xf , y0 , yf):
    
    x, y = linspace( x0 , xf , N ), linspace( y0 , yf , N )

    rho = zeros((N , N), dtype=float64)

    for i in range( N ):
        for j in range( N ):


            w = complex(x[i],y[j])          # w es un número complejo con parte real x y parte compleja y        
            
            r = Scheme( 1., 1. , 0., lambda u,t : w*u)   # Primero llama a la función Scheme con esos atributos. Lueego lambda crea una función como def pero sin nombre que es la F que necesita el esquema numérico 
            rho[i,j]=abs(r)

    return rho, x, y  

def test_Stability_region():

    schemes = [RK4, Euler, Crank_Nicolson]

    for scheme in schemes:

        rho, x, y = Stability_Region (scheme,100,-4,2,-4,4)
       
        #plt.contour(x,y, transpose(rho), linspace(0,1,11))   # Al pintar las regiones de estabilidad rho representa las isolíneas de ganancia constante
        
    return rho, x, y
        
        
        
        


test_Stability_region()