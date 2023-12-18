
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



      
      
        
temporal_scheme = RK4


U = Milestone_function(tf=10 ,N=10000, U0=array([1.5,1]))  #Llamo a la función que va a resolver el problema de Cauchy introduciendo los parámetos
#tf=1 
#N=100
#t = linspace(0,tf,N)  
print(U)


plt.axis('equal')
plt.plot( U[:,0] , U[:,1] )            #Grafico los resultados
plt.grid()
plt.show()




#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#plt.plot(U[2000:50000,0],U[2000:50000,1],U[2000:50000,2])

#plt.show()










    
