





#=================================================================================
#=================================================================================
#                      MASTER UNIVERSITARIO EN SISTEMAS ESPACIALES
#                                 IDR - ETSIAE - UPM
#						     AMPLIACION DE MATEMATICAS 1
#                                Javier Pueyo Serrano
#                              Ruben Garrido Echevarría
#=================================================================================
#=================================================================================


#=================================================================================
#								FINAL MILESTONE
#=================================================================================


from Sistemas_Dinamicos.Temporal_integrator import  RK4, Adams_Bashforth_4th_order
#from Sistemas_Dinamicos.Cauchy_Problem import Cauchy_Problem
#from ODEs.Stability_Region import Region_Estabilidad
#from ODEs.Temporal_Error import Error_Cauchy_Problem, Temporal_Convergence_Rate

from Sistemas_Dinamicos.Dynamic_System import VanDerPol_Libre, VanDerPol_ForzadoArmonico, VanDerPol_ForzadoEstocastico, VanDerPol_Libre2, VanDerPol_Libre3

import matplotlib.pyplot as plt
from numpy import array, zeros, linspace, abs, transpose, float64, histogram2d, meshgrid, ones_like, max, min, arange
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

## Graficos con tipografia LaTeX
#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "serif",
#    "font.serif": ["Computer Modern Roman"],
#})

#print( "" )
#print( "   ==========================================================================" )
#print( "   ==========================================================================" )
#print( "   ==           MASTER UNIVERSITARIO EN SISTEMAS ESPACIALES                ==" )
#print( "   ==                         IDR - ETSIAE - UPM                           ==" )
#print( "   ==                    AMPLIACION DE MATEMATICAS 1                       ==" )
#print( "   ==                        Javier Pueyo Serrano                          ==" )
#print( "   ==========================================================================" )
#print( "   ==========================================================================" )
#print( "" )
#print( "" )
#print( "" )
#print( "   ==========================================================================" )
#print( "   =========================    FINAL MILESTONE    ==========================" )
#print( "   ==========================================================================" )
#print( "" )


#print( "   INTERVALO DE TIEMPO" )
#print( "" )
#print( "   Seleccione el tiempo de integracion que desea utilizar para la resolucion." )

#float(input( "        tf = " ))
#input()
#print( "   Seleccione el numero de pasos que desea utilizar para la resolucion." )

#int(input( "        N = " ))
#print( "" )
#input()
#t = linspace( start = 0, stop = tf, num = N)

t0 = 0
h = 0.01
t_final = 1000
N =  t_final/h
print(N)

# Inicialización de las listas de valores
t_values = arange(t0, t_final + h, h)
U = zeros((len(t_values), 3))

# Condiciones iniciales
t_values[0] = t0
U0 = array([0,1,0])

U1 = U0 + h*VanDerPol_ForzadoEstocastico(t_values[0],U0)
t_values[1] = t0 + h
U2= U1 + h*VanDerPol_ForzadoEstocastico(t_values[1],U1)
t_values[2] = t_values[1] + h
U3= U2 + h*VanDerPol_ForzadoEstocastico(t_values[2],U2)


U[0,:] = U0
U[1,:] = U1
U[2,:] = U2
U[3,:] = U3


Adams_Bashforth_4th_order(h, t_values, U, VanDerPol_ForzadoEstocastico)
print(U)

plt.plot( U[:,0] , U[:,1] )   
plt.show()

#U_01 = array([1,0,0])
#U1 =  Cauchy_Problem( VanDerPol_ForzadoEstocastico, t, U_01, RungeKutta_4 )

#U_02 = array([0.1,0])
#U2 =  Cauchy_Problem( VanDerPol_Libre2, t, U_02, RungeKutta_4 )

#U_03 = array([0.1,0])
#U3 =  Cauchy_Problem( VanDerPol_Libre3, t, U_03, RungeKutta_4 )



##plt.figure()
##plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
##plt.plot( t[:] , U1[:,0], color = 'r')
##plt.ylabel("$x$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.xlabel("$t$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.figure()
##plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
##plt.plot( t[:] , U1[:,1], color = 'g')
##plt.ylabel("$dx/dt$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.xlabel("$t$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.show()

##plt.figure()
##plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
##plt.plot( t[:] , U2[:,0], color = 'r')
##plt.ylabel("$x$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.xlabel("$t$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.figure()
##plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
##plt.plot( t[:] , U2[:,1], color = 'g')
##plt.ylabel("$dx/dt$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.xlabel("$t$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.show()

##plt.figure(figsize=(8, 8))
##plt.tick_params(labelsize=13)
##plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
##plt.plot( U1[:,0] , U1[:,1], color = 'b')
##plt.plot(0.1,0,marker='o', color='r')
##plt.ylabel("$dx/dt$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.xlabel("$x$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.axis("equal")
##plt.savefig('VDP_Libre_mu_negativo.png', format='png')
##plt.figure(figsize=(8, 8))
##plt.tick_params(labelsize=13)
##plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
##plt.plot( U2[:,0] , U2[:,1], color = 'b')
##plt.plot(0.1,0,marker='o', color='r')
##plt.ylabel("$dx/dt$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.xlabel("$x$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.axis("equal")
##plt.savefig('VDP_Libre_mu_positivo.png', format='png')
##plt.figure(figsize=(8, 8))
##plt.tick_params(labelsize=13)
##plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
##plt.plot( U3[:,0] , U3[:,1], color = 'b')
##plt.plot(0.1,0,marker='o', color='r')
##plt.ylabel("$dx/dt$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.xlabel("$x$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.axis("equal")
##plt.savefig('VDP_Libre_mu_nulo.png', format='png')
##plt.show()


#plt.figure(figsize=(8, 8))
#plt.tick_params(labelsize=13)
#plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
#plt.plot( U1[:,0] , U1[:,1], color = 'b')
#plt.plot( U2[:,0] , U2[:,1], color = 'r')
#plt.plot( U3[:,0] , U3[:,1], color = 'g')
#plt.plot(0.1,0,marker='o', color='k')
#plt.ylabel("$dx/dt$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
#plt.xlabel("$x$", fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
#plt.axis("equal")
#plt.savefig('VDP_Libre_mu_nulo.png', format='png')
#plt.show()



### Crear la figura usando plt.figure
##plt.figure(figsize=(8, 8))
##plt.tick_params(labelsize=13)
### Crear una linea vacia que se actualizara en la animacion
##line, = plt.plot([], [], '-',color='blue')
### Función de inicializacion: se llama para crear la trama base vacia
##def init():
##    line.set_data([], [])
##    return line,
### Funcion de actualizacion para cada cuadro de la animacion
##def update(frame):
##    x1 = U1[:frame, 0]  # Obtener datos hasta el cuadro actual
##    y1 = U1[:frame, 1]
##    line.set_data(x1, y1)

##    return line,
### Crear la animacion
##plt.xlim([-0.10,0.12])
##plt.ylim([-0.10,0.10])
##plt.xlabel('$x$', fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.ylabel('$dx/dt$', fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.plot(0.1,0,marker='o', color='b')
##ani = animation.FuncAnimation(plt.gcf(), update, frames=U1.shape[0], init_func=init, blit=True, interval=0.01)
##ani.save('Anim_VDPL_Muneg.gif', writer='pillow', fps=240)

##plt.show()

### Crear la figura usando plt.figure
##plt.figure(figsize=(8, 8))
##plt.tick_params(labelsize=13)
### Crear una linea vacia que se actualizara en la animacion
##line, = plt.plot([], [], '-',color='blue')
### Función de inicializacion: se llama para crear la trama base vacia
##def init():
##    line.set_data([], [])
##    return line,
### Funcion de actualizacion para cada cuadro de la animacion
##def update(frame):
##    x2 = U2[:frame, 0]  # Obtener datos hasta el cuadro actual
##    y2 = U2[:frame, 1]
##    line.set_data(x2, y2)

##    return line,
### Crear la animacion
##plt.xlim([-3,3])
##plt.ylim([-3,3])
##plt.xlabel('$x$', fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.ylabel('$dx/dt$', fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.plot(0.1,0,marker='o', color='b')
##ani = animation.FuncAnimation(plt.gcf(), update, frames=U2.shape[0], init_func=init, blit=True, interval=0.01)
##ani.save('Anim_VDPL_Mupos.gif', writer='pillow', fps=240)

##plt.show()

### Crear la figura usando plt.figure
##plt.figure(figsize=(8, 8))
##plt.tick_params(labelsize=13)
### Crear una linea vacia que se actualizara en la animacion
##line, = plt.plot([], [], '-',color='blue')
### Función de inicializacion: se llama para crear la trama base vacia
##def init():
##    line.set_data([], [])
##    return line,
### Funcion de actualizacion para cada cuadro de la animacion
##def update(frame):
##    x3 = U3[:frame, 0]  # Obtener datos hasta el cuadro actual
##    y3 = U3[:frame, 1]
##    line.set_data(x3, y3)

##    return line,
### Crear la animacion
##plt.xlim([-0.11,0.11])
##plt.ylim([-0.11,0.11])
##plt.xlabel('$x$', fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.ylabel('$dx/dt$', fontdict = {'fontsize':14, 'fontweight':'normal', 'color':'k'})
##plt.plot(0.1,0,marker='o', color='b')
##ani = animation.FuncAnimation(plt.gcf(), update, frames=U3.shape[0], init_func=init, blit=True, interval=0.01)
##ani.save('Anim_VDPL_Munulo.gif', writer='pillow', fps=240)



##plt.show()














##plt.show()

## with warnings.catch_warnings():
##     warnings.simplefilter("ignore", category=UserWarning)
##     hexbin_plot = plt.hexbin(U2[0,:], U2[1,:], gridsize=25, cmap='viridis', mincnt=1)
## counts = hexbin_plot.get_array()
## min_count = min(counts)
## max_count = max(counts)
## common_value = median(counts)
## uncommon_value = min(counts)
## # legend = plt.colorbar(hexbin_plot, label='Frecuencia')
## legend = plt.colorbar(hexbin_plot)
## legend.set_ticks([uncommon_value, common_value, max_count])
## # legend.set_ticklabels(['Menos comun', 'Mas comun', ''])
## legend.ax.set_yticklabels(['', 'Menos comun', 'Mas comun'])
## plt.title('Histograma 2D con leyenda de colores')
## plt.xlabel('X')
## plt.ylabel('Y')
## plt.axis('equal')
## plt.show()



#hist, xedges, yedges = histogram2d(U[:,0], U[:,1], bins=25)
#x_centers = (xedges[:-1] + xedges[1:]) / 2
#y_centers = (yedges[:-1] + yedges[1:]) / 2
#fig = plt.figure(figsize=(10, 8))
#ax = fig.add_subplot(111, projection='3d')
#x_mesh, y_mesh = meshgrid(x_centers, y_centers)
#ax.bar3d(x_mesh.flatten(), y_mesh.flatten(), 0, 1, 1, hist.flatten(), shade=True)
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Frecuencia')
#plt.title('Histograma 3D')
#plt.axis('equal')
#plt.show()





# Datos de ejemplo (sustituye estos con tus propios datos)
data_x = U[:,0]
data_y = U[:,1]

# Crear el histograma bidimensional
plt.figure(figsize=(8, 6))
plt.hist2d(data_x, data_y, bins=200, cmap='viridis')

# Agregar etiquetas y titulo
plt.colorbar(label='Frecuencia')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Histograma 2D de Datos')

## Mostrar el grafico
plt.show()


# Calcular el histograma tridimensional
hist, x_edges, y_edges = histogram2d(data_x, data_y, bins=100)

# Obtener las coordenadas para el grafico 3D
xpos, ypos = meshgrid(x_edges[:-1] + 0.25, y_edges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Tamanos de los cuadrados en el grafico
dx = dy = 0.5 * ones_like(zpos)
dz = hist.ravel()
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')


ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', cmap='viridis')


ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Frecuencia')
ax.set_title('Histograma 3D')

plt.show()

