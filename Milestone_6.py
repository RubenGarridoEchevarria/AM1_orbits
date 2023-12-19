
from Funciones_Auxiliares.RK_Embebido import Embedded_RK

from scipy.optimize import newton
from scipy.integrate import solve_ivp
from Funciones_Auxiliares.Temporal_integrator import RK4, Crank_Nicolson
from Funciones_Auxiliares.F_3_Cuerpos import F_3_Cuerpos

from Funciones_Auxiliares.Cauchy_Problem_Con_F import Cauchy_problem
from numpy import sqrt, array, hstack, cos, sin, abs, concatenate, linspace, pi, zeros_like, sum, square, float64
import matplotlib.pyplot as plt
import matplotlib.path as mpath

## Código pora la resolucion del problema de los 3 cuerpos restirngidos.


def Problema_Tres_Cuerpos_Restirngidos():
    
    #Condiciones iniciales

    m_1 = 5.974E24                      # Masa de la tierra
    m_2 = 7.348E22                      # Masa de la luna
    pi_2 = m_2/(m_1 + m_2)              # Relación de la segunda masa entre la masa total
    
    
 ## Seleccionar la condición inicila de los diferentes puntos de Lagrange calculados con la última función
 # Todas las cordenadas están adimensionalizadas respecto a la distancia entre la tierra y la luna
 
   # Condiciones iniciales para el L1 ----->  Punto de Lagrange inestable: Si las condiciones iniciales varian ligeramente del punto de equilibrio, la solución divergerá de éste con el tiempo
    
    # x_0 =  0.8369154703220377
    # y_0 = 0
    # z_0 = 0
    # vx_0 = 0
    # vy_0 = 0
    # vz_0 = 0
    
    # Condiciones iniciales para el L2 ----->  Punto de Lagrange inestable: Si las condiciones iniciales varian ligeramente del punto de equilibrio, la solución divergerá de éste con el tiempo
    
    # x_0 = 1.1556818961291992      
    # y_0 = 0
    # z_0 = 0
    # vx_0 = 0
    # vy_0 = 0
    # vz_0 = 0
    
    # Condiciones iniciales para el L3  ----->  Punto de Lagrange inestable: Si las condiciones iniciales varian ligeramente del punto de equilibrio, la solución divergerá de éste con el tiempo
    
    x_0 = -1.0050626166357435          
    y_0 = 0
    z_0 = 0
    vx_0 = 0
    vy_0 = 0
    vz_0 = 0
    
    
    # # Condiciones iniciales para el L4 ----->  Punto de Lagrange estable: Si las condiciones iniciales varian ligeramente, la solución volverá al punto de equilibrio
    
    # x_0 = 0.5 - pi_2         
    # y_0 = sqrt(3)/2
    # z_0 = 0
    # vx_0 = 0
    # vy_0 = 0
    # vz_0 = 0
    
    #  # Condiciones iniciales para el L5  -----> Punto de Lagrange estable: Si las condiciones iniciales varian ligeramente, la solución volverá a la solución inicial
    
    # x_0 = 0.5 - pi_2         
    # y_0 = -sqrt(3)/2
    # z_0 = 0
    # vx_0 = 0
    # vy_0 = 0
    # vz_0 = 0
    
  
    
    

    r_0 = array((x_0, y_0, z_0))                # Posiciones iniciales
    v_0 = array((vx_0, vy_0, vz_0))             # Velocidades iniciales
    U_0 = hstack((r_0, v_0))                    # Matriz de posiciones y velocidades iniciales

    t_0 = 0                                     # Tiempo inicial 
    t_f = 25                                  # Tiempo final
    t_points = linspace(t_0, t_f, 1000)         
    
    
    
    # Resolución del problema de los 3 cuerpos resitringidos
    
    U = Cauchy_problem(t_points, U_0, RK4, F_3_Cuerpos)         # Resolución del porblema de los tres cuerpos llamando a la funcion Cauchy Porblem. Esta a su vez usará la función RK4 como integrador temporal

    r = U[:, :3]    # Vector de posicion
    v = U[:, 3:]    # Vector de velocidad
    x_2 = (1 - pi_2) * cos(linspace(0, pi, 100))
    y_2 = (1 - pi_2) * sin(linspace(0, pi, 100))


    fig, ax = plt.subplots(figsize=(5,5), dpi=96)

    ax.plot(r[:, 0], r[:, 1], 'k', label="Trajectory")
    ax.axhline(0, color='k')
    ax.plot(hstack((x_2, x_2[::-1])), hstack((y_2, -y_2[::-1])))
    ax.plot(-pi_2, 0, 'bo', label="$m_1$")              # Posición de la tierra
    ax.plot(1 - pi_2, 0, 'go', label="$m_2$")           # Posición de la luna
    ax.plot(x_0, y_0, 'ro')                             # Satélite
    ax.set_aspect("equal")

    plt.show()
    
Problema_Tres_Cuerpos_Restirngidos()


def Lagrange_Points():

    # Código para calcular los puntos de Lagrange

    circle = mpath.Path.unit_circle()
    wedge_1 = mpath.Path.wedge(90, 180)
    wedge_2 = mpath.Path.wedge(270, 0)

    verts = concatenate([circle.vertices, wedge_1.vertices[::-1, ...], wedge_2.vertices[::-1, ...]])
    codes = concatenate([circle.codes, wedge_1.codes, wedge_2.codes])
    center_of_mass = mpath.Path(verts, codes)

    
    m_1 = 5.974E24 
    m_2 = 7.348E22 
    pi_2 = m_2/(m_1 + m_2)


    x_2 = (1 - pi_2) * cos(linspace(0, pi, 100))
    y_2 = (1 - pi_2) * sin(linspace(0, pi, 100))
    x_1 = (-pi_2) * cos(linspace(0, pi, 100))
    y_1 = (-pi_2) * sin(linspace(0, pi, 100))
    
    def collinear_lagrange(xstar, pi_2):
      
        first_term = xstar
        second_term = (1 - pi_2) / abs(xstar + pi_2)**3 * (xstar + pi_2)
        third_term = pi_2 / abs(xstar - 1 + pi_2)**3 * (xstar - 1 + pi_2)
        return first_term - second_term - third_term
    
    L_2 = newton(func=collinear_lagrange, x0 = float64(1.0), args=(pi_2,))
    L_1 = newton(func=collinear_lagrange, x0=0.836915, args=(pi_2,))
    L_3 = newton(func=collinear_lagrange, x0=-1, args=(pi_2,))
    print(f"{L_1=}, {L_2=}, {L_3=}")
    
        
Lagrange_Points()    

