
from numpy import array
from math import cos
from numpy import sqrt, log, cos, pi, zeros
from random import random


def Vanderpol_Oscilator(U,t):
    
    return array([U[1], U[0]-U[0]**3])



def Duffin_Osciliator_2(U,t):
    k = 0.01
    B = 1 
    
    return array ( [U[1], -U[0]**3-k*U[1]+B*cos(t)] )


def Rayleigh_Osocilator(U,t):
    
    f0 = 1
    
    return array([ U[1] , U[0] - U[0]**3 - U[1] + f0*cos(t) ])


def pruebas(U,t):
    
    return -4 * t + U[0]


def pruebas_2(U,t):

    return array(U[1], -U[0])

def pruebas_3(U,t):

    return array([U[1], U[0] - U[0]**2])


def f(t, U):
    
    return array([U[1], U[0]-U[0]**3])


#=================================================================================
#								 MATH EQUATIONS
#=================================================================================


from numpy import array, cos, sin, arange, sqrt
from numpy.random import randn


def VanDerPol_Libre( U, t ):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.

	return array( [y , 1*(1 - x**2)*y - x  ] )

def VanDerPol_Libre2( U, t ):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.

	return array( [y , 1*(1 - x**2)*y - x  ] )

def VanDerPol_Libre3( U, t ):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.

	return array( [y , 3*(1 - x**2)*y - x  ] )

def VanDerPol_Libre4( U, t ):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.

	return array( [y , 0.5*(1 - x**2)*y - x  ] )


def VanDerPol_ForzadoArmonico( U, t ):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.

	return array( [y , -0.01 * (x**2-1) * y - 1 * x + 2*cos(t)  ] )


def VanDerPol_ForzadoEstocastico(U, t ):
    mu = 1.2
    w0 = 1
    tau = 0.1
    D = 1000000
    h = 0.01
    def Box_Muller_random_generator(a, b):
        # Genera un número aleatorio con distribución normal estándar utilizando el método de Box-Muller
        # Input: Dimensiones del output (hasta 2 dimensiones)
        # Output: Numero aleatorio con distribucion normal estandar
        Z1 = zeros((a, b))
        for ii in range(0, a):
            for jj in range(0, b):
                U1 = 1.0 - random()
                U2 = 1.0 - random()
                Z1[ii, jj] = sqrt(-2*log(U1)) * cos(2*pi*U2)
                
        return Z1
    Z1 = Box_Muller_random_generator(1,1)
 
    return array([U[1], -mu*(U[0]**2 - 1)*U[1] - (w0)*U[0] - U[2], -U[2]/tau + sqrt(D)*sqrt(h)*Z1[0,0]])
