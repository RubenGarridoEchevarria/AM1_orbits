
from numpy import zeros
from Kepler_Orbits import F_Kepler




def Cauchy_problem(F,t, U0, Temporal_integrator):  #Defino el problema de Cauchy Con la F, la condición inicial y se introducé el integrador temporal que se usa
    
    N = len(t)-1                #Creará la dimensión de la matriz donde se guradan cada paso de tiempo 
    Nv = len(U0)                #Creará la dimensión de la matriz donde se guarda cada componte del vector de Kepler para cualquier matriz
    U = zeros((N+1,Nv))         #El vector solución será una matriz en la que las filas son cada paso de tiempo y las columnas son cada componente del vector de Kepler en ese paso de tiempo
    U[0,:] = U0                 #Establezco que el primer paso de timpo para todas las compontes columna es la condición inicial

    for i in range(N):          #Crea el vector del problema de Cauchy para luego en cada paso del bucle resolverlo

    
            U[i+1,:] = Temporal_integrator( U[i, :], t[i+1] - t[i], t[i],  F_Kepler) #Crea el vector problema de Cauchy en el siguiente paso de tiempo y llama al integrador temporal para que lo resulva


    return U    #Devuelve la imagen de lo calculado por el integrador temporal
    
