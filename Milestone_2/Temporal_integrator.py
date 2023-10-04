


from scipy.optimize import newton


def Euler(U, dt, t, F_Kepler):

    return U + dt * F_Kepler(U,t)



def Crank_Nicolson(U, dt, t, F_Kepler):

    def residual(X):

        return X-a-dt/2*F_Kepler(X, t+dt)
    

    a = U + dt/2*F_Kepler(U, t)




    return newton(Crank_Nicolson, U)