
from numpy import array,zeros, float64, real, imag
import scipy.linalg
import matplotlib.pyplot as plt
from Region_estabilidad import test_Stability_region


def System_matrix (F , U0 , t):

    eps = 1e-6  #Epsilon
    N=len(U0)     
    A=zeros( (N,N), dtype=float64 ) #La matriz a tendrá las dimensiones que tenga el vector de condicion inicial
    delta=zeros(N)      


    for j in range(N):
        
        delta[:]=0
        delta[j]=eps        #mete el épsilon soo en la diagonal
       
        A[:,j]=(F(U0+delta,t) - F(U0-delta,t))/(2*eps)  #Lla dos veces al oscilador con los argumentos de la condición inicial sumando o restando un paso de tiempo y el argumento del tiempo aunque en el caso del osicador no aplica


    return A 

def Oscillator(U,t): 

   return array( [ U[1], -U[0] ] )  

def test_system_matrix(): 

    U0 = array( [ 0., 0. ] ) 
    t = 0. 
    A = System_matrix(Oscillator,  U0, t)       #Construyo la matriz A (Jacobiana del sistema) con la condición inicial t, U0 y la F que toque en cada caso. Ahora está elegida la del oscilador
    print("A=", A)
    autovalores = scipy.linalg.eigvals(A)
    n = len(autovalores)
    print(autovalores)
    
    lambda_1 = complex(autovalores[0])
    lambda_2 = complex(autovalores[1])
    lamda = array( zeros(n))
    plt.figure()
    for i in range(n):
        
        x1=real(autovalores[i])
        y1=imag(autovalores[i])
        plt.plot(x1,y1, ".")
        
    
    test_Stability_region()
    plt.contour(x,y, transpose(rho), linspace(0,1,11))
    plt.show()
    
    
    
    
   
     
        
    
        
    


test_system_matrix()