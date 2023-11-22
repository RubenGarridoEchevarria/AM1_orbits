
import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace 
from Temporal_integrator import Euler, Crank_Nicolson, RK4
from Cauchy_Problem import Cauchy_problem
from mpl_toolkits.mplot3d import Axes3D




def Milestone_function(tf, N, U0):     #Defino la función que resolverá el problema de Cauchy con los argumentos de tiempo final, número de iteraciones y las condiciones iniciales
    
    
    t = linspace(0,tf,N)  

    U = Cauchy_problem(t, temporal_scheme, U0)       #La solución la resulvo llamndo a problema de Cauchy metiendo en el primer argumento al F de Kepler
    return U



      
      
        
temporal_scheme = Euler


U = Milestone_function(tf=100 ,N=50000, U0=array([-1,-1,1]))  #Llamo a la función que va a resolver el problema de Cauchy introduciendo los parámetos

print(U)

plt.axis('equal')
plt.plot( U[2000:50000,0] , U[2000:50000,1] )            #Grafico los resultados
plt.grid()
plt.show()




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.plot(U[0],U[1],U[2])

plt.show()










    
