


import matplotlib.pyplot as plt
from numpy import array, vstack, arange, zeros
from Sistemas_Dinamicos.Temporal_integrator import Adams_Bashforth_4th_order
from Sistemas_Dinamicos.Dynamic_System import f





t0 = 0
h = 0.001
t_final = 20

# Inicialización de las listas de valores
t_values = arange(t0, t_final + h, h)
U = zeros((len(t_values), 2))

# Condiciones iniciales
t_values[0] = t0
U0 = array([0,1])

U1 = U0 + h*f(t_values[0],U0)
t_values[1] = t0 + h
U2= U1 + h*f(t_values[1],U1)
t_values[2] = t_values[1] + h
U3= U2 + h*f(t_values[2],U2)


U[0,:] = U0
U[1,:] = U1
U[2,:] = U2
U[3,:] = U3


Adams_Bashforth_4th_order(h, t_values, U, f)
print(U)

plt.plot( U[:,0] , U[:,1] )   
plt.show()




plt.show()
