



from scipy.optimize import newton
from numpy import zeros, array, arange
from Sistemas_Dinamicos.Cauchy_Problem import Cauchy_problem



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
    history = []

 

    if len(history) < 4:

        
        if len(history) == 0:
            history.append(U)
        for _ in range(3 - len(history)):
            U_next = U + dt * F(U, t)
            history.append(U_next)
            U = U_next
            t += dt

 

        return U_next

 
    f0 = F(history[-1], t - 3 * dt)
    f1 = F(history[-2], t - 2 * dt)
    f2 = F(history[-3], t - dt)
    f3 = F(history[-4], t)

    U_next = U + (dt / 24) * (55 * f3 - 59 * f2 + 37 * f1 - 9 * f0)
    history.append(U_next)
    return U_next       