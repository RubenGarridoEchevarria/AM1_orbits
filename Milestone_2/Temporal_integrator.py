

def Euler(U, dt, t, F_Kepler):

    return U + dt * F_Kepler(U,t)