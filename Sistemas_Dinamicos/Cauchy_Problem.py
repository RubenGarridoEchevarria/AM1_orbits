
from numpy import zeros, arange





def Cauchy_problem(t, U0, Temporal_integrator, Diferntial_operator):  #Defino el problema de Cauchy Con la F, la condición inicial y se introducé el integrador temporal que se usa
    
    N = len(t)-1                #Creará la dimensión de la matriz donde se guradan cada paso de tiempo 
    Nv = len(U0)                #Creará la dimensión de la matriz donde se guarda cada componte del vector de Kepler para cualquier matriz
    U = zeros((N+1,Nv))         #El vector solución será una matriz en la que las filas son cada paso de tiempo y las columnas son cada componente del vector de Kepler en ese paso de tiempo
    U[0,:] = U0                 #Establezco que el primer paso de timpo para todas las compontes columna es la condición inicial

    for i in range(0,N):          #Crea el vector del problema de Cauchy para luego en cada paso del bucle resolverlo

    
            U[i+1,:] = Temporal_integrator(U[i, :] , t[i+1] - t[i], t[i],  Diferntial_operator) #Crea el vector problema de Cauchy en el siguiente paso de tiempo y llama al integrador temporal para que lo resulva


    return U    #Devuelve la imagen de lo calculado por el integrador temporal
    
def Cauchy_problem_Adams(t, U0, Temporal_integrator,Diferntial_operator,h):
        
        # t0 = t[0] 
        
        # t_values_0 = arange(t0,4 * h, h)
        # U1 = Cauchy_problem (t_values_0, U, RK4, Diferntial_operator)
    
        # U[0,:] = U1[0,:]
        # U[1,:] = U1[1,:]
        # U[2,:] = U1[2,:]
        # U[3,:] = U1[3,:]
        
        t0=0
        
        n = len(t)
  
        U = zeros((len(t),3))
        # Condiciones iniciales
        #t[0] =  0
        

        U1  = U0 + h*Diferntial_operator(U0,t[0])
        #t[1] = t0 + h
      
        U2 = U1 + h*Diferntial_operator(U1,t[1])
        
        #t[2] = t[1] + h
        
        U3 = U2 + h*Diferntial_operator(U2,t[2])


        U[0,:] = U0
        U[1,:] = U1
        U[2,:] = U2
        U[3,:] = U3

        
        for i in range(3, len(t)-1):
                
                U[i+1,:] = Temporal_integrator( U[i,:], U[i-1, :], U[i-2, :], U[i-3,:] ,t[i+1] - t[i], t[i],  Diferntial_operator)
        
    
        return U
        