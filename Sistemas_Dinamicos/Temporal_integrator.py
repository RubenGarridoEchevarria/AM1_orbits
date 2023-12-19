



from scipy.optimize import newton
from numpy import zeros, array, arange
from Sistemas_Dinamicos.Cauchy_Problem import Cauchy_problem



def Euler(U, dt, t, F):         #Resuelve el problema de Cauchy con el método de Euler

    return U + dt * F(U,t)     #La solución en el paso siguiente será la solución en el paso actual más el paso de tiempo por la F de kepler en ese instante de tiempo



def Crank_Nicolson(U, dt, t, F):  #Resuelve el problema de Cauchy con el método de Crank-Nicolson

    def residual(X):                        #Define la función residual que solo tiene como argumento X, todo lo demás le viene dado por los datod de las demás funciones

        return X - a - dt/2*F(X, t+dt)   #Devuleve la imagen que es un sistema de ecuaciones no linela
    

    a = U + dt/2 * F(U, t)
    
    return newton(residual, U, maxiter=400)    #Resuleve el sistema de ecuaciones no lineal por el método de Newton



def RK4(U, dt, t, F):

    K1=F(U,t)
    K2=F(U + dt * K1/2, t + dt/2)
    K3=F(U + dt * K2/2, t + dt/2)
    K4=F(U + dt * K3, t + dt)

    return U + dt * (K1 + 2*K2 + 2*K3 +K4)/6


def Adams_Bashforth_4th_order(h, t_values, t0, U0, f):
    
    n = len(t_values)
  
    U = zeros((len(t_values),3))
    # Condiciones iniciales
    t_values[0] =  t0
   

    U1 = U0 + h*f(U0,t_values[0])
    t_values[1] = t0 + h
    U2= U1 + h*f(U1,t_values[1])
    t_values[2] = t_values[1] + h
    U3= U2 + h*f(U2,t_values[2])


    U[0,:] = U0
    U[1,:] = U1
    U[2,:] = U2
    U[3,:] = U3

    
    
    
    for i in range(3, n - 1):
        U[i+1,:] = U[i,:] + h / 24 * (55 * f(U[ i,:], t_values[i])
                                            - 59 * f( U[i - 1,:],t_values[i - 1])
                                            + 37 * f(U[i - 2, :], t_values[i - 2])
                                            - 9 * f(U[i - 3,:],t_values[i - 3]))
        
        
        
        t_values[i + 1] = t_values[i] + h
        

    return U , t_values





def Adams_Bashforth_4th_order_2(U, U1, U2 , U3, dt, t, F):
        

    return U + (dt /24) * ( 55 * F(U, t) - 59 * F(U1,t) + 37 * F(U2,t) -9 * F(U3,t))