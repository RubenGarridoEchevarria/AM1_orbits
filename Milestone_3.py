
from Funciones_Auxiliares.Cauchy_Problem_Con_F import Cauchy_problem
from numpy import array, zeros, log10, ones, vstack, linspace
from numpy.linalg import norm, lstsq
from Funciones_Auxiliares.Kepler_Orbits import F_Kepler
from Funciones_Auxiliares.Temporal_integrator import RK4, Euler, Crank_Nicolson
import matplotlib.pyplot as plt



def Error_Cauchy_Problem (Time_Domain, Diferential_operator, Scheme, order, U0):        #Esta función obtienen el error de un esquema numérico al calcula una solución usando dos mallas diferentes
                                                                                        # Diferntial operator es la F de la ecuación diferencial que resolvamos
    
    N = len(Time_Domain)-1
    Nv = len(U0)
    
    t1 = Time_Domain            # Espaciado temporal de la primera malla
    t2 = zeros(2*N+1)           # Espaciado temporal de la segunda malla. Tiene que ser el doble que la primera 
    Error = zeros ((N+1, Nv))      # El error tendrá por filas los pasos de tiempo de la malla primera y por columnas las diferentes componenetes de la condición inicial U0
    
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

 
 U, Error = Error_Cauchy_Problem( Time_Domain = t, Diferential_operator = F_Kepler,  Scheme = Euler, order = order, U0 = U0  ) # La solución exacta y el error en cada paso se obtienen al llamar a la función anterior

 plt.plot(t, Error[:,0] )
 plt.axis('equal')
 plt.grid()
 plt.show()

#Test_Error_Cauchy_Problem()

def Ratio_convergencia_temporal( Time_Domain, Diferential_operator, U0, Scheme, m):   # Este programa se usa para calcular el orden de un esquema numérico y las graficar como evoluciona el error logarítimico en función del paso logarítmico
    
    
    log_E = zeros(m)        #Los errores logarítmicos tienen la dimensión el número de iteraciones que voy a usar para calcularlos  
    log_N = zeros(m)
    
    N = len(Time_Domain)-1      # Número de pasos de la malla 1
    t1 = Time_Domain            # El paso de tiempo de la malla 1

    U1 = Cauchy_problem(t1, U0, Scheme, Diferential_operator)       # Calculo la solución al problema con la malla 1
    
    for i in range(m):                                  # Bucle que calcula el error logaritmico. Se repite las veces "m" que le he puesto
        
        N = 2*N                                         # Creo la segunda malla a partir de la primera
        t2 = array(zeros(N+1))                          
        t2[0:N+1:2] = t1                                #Relleno la primera parte de la malla con t1 como se ha hecho en la primera función para calcular el error. La sintaxis significa que desde 0 hasta N+1 con pasos de 2
        t2[1:N:2] = ( t1[1:int(N/2)+1] + t1[0:int(N/2)] )/2 #Relleno la segunda mitad de la malla. La sintaxis significa desde el paso 1 hasta N+1 con pasos de 2
        
        U2= Cauchy_problem(t2, U0, Scheme, Diferential_operator)    #Resulevo el problema con la segunda malla
    
        error = norm(U2[N,:] - U1[int(N/2),:]) # Calculo el error
        log_E[i] = log10( error )               # Hago el logarimo del error
        log_N[i] = log10 (N)
        t1 = t2                                 # Igualo en ese paso del bucle tanto las mallas como la solución en este paso de tiempo
        U1 = U2
        
        
    for j in range(m):
        if abs(log_E[j]) > 12: break
            
    j= min (j, m-1)
    x = log_N[0:j+1]
    y = log_E[0:j+1]
    A = vstack([x, ones(len(x))]).T
    m,c =lstsq(A,y, rcond=None)[0]
    order=abs(m)
    log_E = log_E -log10(1-1/2**order)
    
    return order, log_E, log_N


def Test_convergencia_temporal():

    N = 2000                    # Numero de pasos de tiempo que con el que calculo las solución es del problema
    t = linspace(0,10,N)        # Paso de tiempo para calcular la solución del problema
    U0 = array([1, 0, 0, 1 ])    #Condición inicial de Kepler
    m = 5                       #Cuantas veces itero para calcular el error logarítmico (Cuidado con poner un número alto)
    order, log_e, log_n = Ratio_convergencia_temporal(t, F_Kepler, U0, Crank_Nicolson, m)            # Llamo a la función que me calcula el orden del esquema y la evolución del error del esquema en escala logarítmica
    print("order =",order)
    plt.plot(log_n, log_e)
    plt.axis('equal')
    plt.grid()
    plt.show()
    
Test_convergencia_temporal()
   
