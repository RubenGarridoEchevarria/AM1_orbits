
from Cauchy_Problem import Cauchy_problem
from numpy import array, zeros, log10, ones, vstack, linspace
from numpy.linalg import norm, lstsq
from Kepler_Orbits import F_Kepler
from Temporal_integrator import RK4, Euler, Crank_Nicolson
import matplotlib.pyplot as plt



def Error_Cauchy_Problem (Time_Domain, Diferential_operator, Scheme, order, U0):        #Esta función obtienen el error de un esquema numérico al calcula una solución usando dos mallas diferentes
                                                                                        # Diferntial operator es la F de la ecuación diferencial que resolvamos
    
    N = len(Time_Domain)-1
    Nv = len(U0)
   
    t1 = Time_Domain            # Espaciado temporal de la primera malla
    t2 = zeros(2*N+1)           # Espaciado temporal de la segunda malla. Tiene que ser el doble que la primera 
    Error = zeros(N+1, Nv)      # El error tendrá por filas los pasos de tiempo de la malla primera y por columnas las diferentes componenetes de la condición inicial U0
    
    for i in range(N):
        
        t2[2*i] = t1[i]          # Relleno la segunda malla un hueco si y otro no con la malla primera
        t2[2*i] = (t1[i] + t1[i+1])/2    #Relleno el resto de hecos con el la mitada de el paso en el que estoy más el paso siguiente entre 2
    
    
    t2[2*N] = t1[N]         # La última celda de tiempo de la segunda malla debe ser igual a la última de la primera malla
    
    U1 = Cauchy_problem ( t1, U0, Scheme, Diferential_operator)     # Obtengo las soluciones para la primera malla
    U2 = Cauchy_problem ( t2, U0, Scheme, Diferential_operator)      # Obtengo las soluciones para la segunda malla
    
    for i in range(N): 
        
        Error [i,:] = ( U2[2*i,:] - U1[i,:] )/(1-1/2**order)       #Para todas las columnas (Componentes de U) el error es la solución en la malla 2 menos la solución en la malla 1 entre 1-1/2 elevado al orden del esquema numérico
        
    Solucion = U1 +Error  # La solución exacta será la solución obteneida en cada paso de la malla 1 más el error en cada uno de los pasos
    
    return Solucion, Error



def Test_Error_Cauchy_Problem():        # Función que guarda los argumentos para ejecutar después la función que calcula el error del esquema numérico

 N = 5000                               # Pasos de tiempo
 t = linspace(0, 10, N)                 # Crea el vector de pasos de tiempo que después será el arugmento de Time domain 
 U0 = array([1, 0, 0, 1 ])            # Condición inicial para el problema de Kepler 
 order = 1                              # En este caso sabemos que el orden del esquema de Euler es 1

 
 U, Error = Error_Cauchy_Problem( Time_Domain=t, Diferential_operator=F_Kepler,  Scheme=Euler, order=order, U0 = U0  ) # La solución exacta y el error en cada paso se obtienen al llamar a la función anterior

 plt.plot(t, Error[:,0] )
 plt.axis('equal')
 plt.grid()
 plt.show()

Test_Error_Cauchy_Problem()


    
    
    


 