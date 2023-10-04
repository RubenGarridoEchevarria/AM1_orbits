


from scipy.optimize import newton


def Euler(U, dt, t, F_Kepler):         #Resuelve el problema de Cauchy con el método de Euler

    return U + dt * F_Kepler(U,t)     #La solución en el paso siguiente será la solución en el paso actual más el paso de tiempo por la F de kepler en ese instante de tiempo



def Crank_Nicolson(U, dt, t, F_Kepler):  #Resuelve el problema de Cauchy con el método de Crank-Nicolson

    def residual(X):                        #Define la función residual que solo tiene como argumento X, todo lo demás le viene dado por los datod de las demás funciones

        return X-a-dt/2*F_Kepler(X, t+dt)   #Devuleve la imagen que es un sistema de ecuaciones no linela
    

    a = U + dt/2*F_Kepler(U, t)




    return newton(Crank_Nicolson, U)    #Resuleve el sistema de ecuaciones no lineal por el método de Newton