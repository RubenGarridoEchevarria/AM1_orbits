



from scipy.optimize import newton
from numpy import zeros, array, arange




def Euler(U, dt, t, F):         #Resuelve el problema de Cauchy con el método de Euler

    return U + dt * F(U,t)     #La solución en el paso siguiente será la solución en el paso actual más el paso de tiempo por la F de kepler en ese instante de tiempo



def Crank_Nicolson(U, dt, t, F):  #Resuelve el problema de Cauchy con el método de Crank-Nicolson
    
   

        def residual(X):                        #Define la función residual que solo tiene como argumento X, todo lo demás le viene dado por los datod de las demás funciones

            return X - a - dt/2*F(X, t+dt)   #Devuleve la imagen que es un sistema de ecuaciones no linela
        

        a = U + dt/2 * F(U, t)
    
        return newton(residual, U, maxiter=600)    #Resuleve el sistema de ecuaciones no lineal por el método de Newton



def RK4(U, dt, t, F):

    K1=F(U,t)
    K2=F(U + dt * K1/2, t + dt/2)
    K3=F(U + dt * K2/2, t + dt/2)
    K4=F(U + dt * K3, t + dt)

    return U + dt * (K1 + 2*K2 + 2*K3 +K4)/6



def Adams_Bashforth_4th_order(U, dt, t, F):
    

    
    N = len(U)
    if t == 0:
        global previous_U 
        global previous_U_state
        previous_U = zeros([3,N])
        previous_U_state = zeros([3,1])
 
    # history = [None] * 4  # Lista para almacenar los últimos 4 resultados
 
    # Si hay resultados anteriores faltantes, utiliza Euler para calcularlos
    if any(previous_U_state == 0):
        for ii in range(3):
            if previous_U_state[ii] == 0:
                # Calcula los primeros pasos con el método de Euler
                previous_U[ii,:] = F(U, t)
                previous_U_state[ii] = 1
                return (U + dt * previous_U[ii,:])  # Devuelve el resultado final después de los primeros pasos
    
    # Almacena los valores de previous_U en unas variables auxiliares
    Un3 = previous_U[0,:]
    Un2 = previous_U[1,:]
    Un1 = previous_U[2,:]
 
    # Adams-Bashforth de cuarto orden
    f0 = Un3
    f1 = Un2
    f2 = Un1
    f3 = F(U, t)
 
    # Actualiza el historial eliminando el resultado más antiguo y agregando el nuevo
    previous_U[0,:] = Un2
    previous_U[1,:] = Un1
    previous_U[2,:] = f3
 
    return U + (dt / 24) * (55 * f3 - 59 * f2 + 37 * f1 - 9 * f0)    
    
    
    
    
    
