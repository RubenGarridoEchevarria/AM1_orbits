
from Cauchy_Problem import Cauchy_problem
from numpy import array, zeros, linspace, reshape
from F_N_Cuerpos import F_N_Cuerpos
from Temporal_integrator import RK4
from Milestone_3.Temporal_integrator import Euler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def Condiciones_iniciales (Nc, Nb):
    
    U0 = zeros(2*Nc*Nb)     # Vector de condición inicial que contiene la información de posición y velocidad de cada para cada cuerpo y sus coordenadas
    U1 = reshape(U0, (Nb,Nc,2))  # Convierto el vector en un tensor
    r0 = reshape(U1[:,:,0],(Nb,Nc))  # Separo el tensor en posiciones y velocidades para cada cuerpo y sus cuerpos
    v0 = reshape(U1[:,:,1],(Nb,Nc))
    
    # Cada cuerpo tiene 6 grados de libertad, 3 en posición y otros 3 en velocidad
    
    r0[0,:] = [1, 0, 1] # Posición inicial del cuerpo 1 para todas la coordenadas tienen componentes en los tres ejes
    v0[0,:] = [0, 0.4,0]
    
    r0[1,:] = [-1, 0, 0] # Posición inicial del cuerpo 2 para todas la coordenadas tienen componentes en los tres ejes
    v0[1,:] = [2, -0.4,0]
    
    r0[2,:] = [0, 1, 0] # Posición inicial del cuerpo 3 para todas la coordenadas tienen componentes en los tres ejes
    v0[2,:] = [-0.4, 0,0]
    
    r0[3,:] = [0, -1, 0] # Posición inicial del cuerpo 4 para todas la coordenadas tienen componentes en los tres ejes
    v0[3,:] = [0.4, 0,1]
    
    r0[4,:] = [1, -1, 0] # Posición inicial del cuerpo 4 para todas la coordenadas tienen componentes en los tres ejes
    v0[4,:] = [0.6, 0,1]
    
    return U0


def Milestone_5():
    
    def F_a(U,t):
        
        return F_N_Cuerpos(U,t, Nb,Nc)
    
    N = 1000
    Nb = 5      # Número de cuerpos
    Nc = 3      # Componentes de las coordenadas
    t0 = 0
    tf = 4 
    t = linspace(t0,tf, N+1)  # Vector de tiempos
    
    U0 = Condiciones_iniciales(Nc, Nb)
    U = Cauchy_problem(t, U0, RK4,F_a )
    
    Us = reshape(U, (N+1, Nb, Nc, 2))
    r = reshape(Us[:,:,:,0], (N+1, Nb, Nc))
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(Nb):
        
        plt.plot (r[:,i, 0], r[:,i,1], r[:,i,2] ) # Pinto solo las coordenadas x e y
        
    plt.grid()
    plt.show()
    
    
Milestone_5()

