
import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace 
from Temporal_integrator import Euler, Crank_Nicolson, RK4
from Cauchy_Problem import Cauchy_problem
from mpl_toolkits.mplot3d import Axes3D




def Milestone_function(tf, N, U0):     #Defino la función que resolverá el problema de Cauchy con los argumentos de tiempo final, número de iteraciones y las condiciones iniciales
    
    
    t = linspace(0,tf,N)  

    U = Cauchy_problem(t, U0, temporal_scheme)       #La solución la resulvo llamndo a problema de Cauchy metiendo en el primer argumento al F de Kepler
    return U

tf = 100 
N = 50000
t = linspace(0,tf,N)            #Creo el vector de tiempos
temporal_scheme = RK4
U0 = array([1,1,1])

U = Milestone_function(tf,N, U0)  #Llamo a la función que va a resolver el problema de Cauchy introduciendo los parámetos


plt.axis('equal')
plt.plot( U[0] , U[1] )            #Grafico los resultados
plt.grid()
plt.show()

#plt.plot( t[3000:N],U[3000:N,0])
#plt.show()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.plot(U[0],U[1],U[2])

plt.show()










    
