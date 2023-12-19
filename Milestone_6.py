
from Funciones_Auxiliares.RK_Embebido import Embedded_RK

from scipy.optimize import newton
from scipy.integrate import solve_ivp
from Funciones_Auxiliares.Temporal_integrator import RK4
from Funciones_Auxiliares.F_3_Cuerpos import F_3_Cuerpos

from Funciones_Auxiliares.Cauchy_Problem_Con_F import Cauchy_problem
from numpy import sqrt, array, hstack, cos, sin, abs, concatenate, linspace, pi, zeros_like, sum, square
import matplotlib.pyplot as plt
import matplotlib.path as mpath

## Código pora la resolucion del problema de los 3 cuerpos restirngidos.


def Problema_Tres_Cuerpos_Restirngidos():
    
    #Condiciones iniciales

    m_1 = 5.974E24 
    m_2 = 7.348E22 
    pi_2 = m_2/(m_1 + m_2)              # Relación de la segunda masa entre la masa total

    x_0 = 1 - pi_2                      
    y_0 = .0455
    z_0 = 0
    vx_0 = -0.5
    vy_0 = 0.5
    vz_0 = 0

    r_0 = array((x_0, y_0, z_0))
    v_0 = array((vx_0, vy_0, vz_0))
    U_0 = hstack((r_0, v_0))

    t_0 = 0  
    t_f = 20  
    t_points = linspace(t_0, t_f, 1000)
    
    
    
    # Resolución del problema de los 3 cuerpos resitringidos
    
    U = Cauchy_problem(t_points, U_0, RK4, F_3_Cuerpos)

    r = U[:, :3]    # Posicion
    v = U[:, 3:]    # Velocidad


    x_2 = (1 - pi_2) * cos(linspace(0, pi, 100))
    y_2 = (1 - pi_2) * sin(linspace(0, pi, 100))
    fig, ax = plt.subplots(figsize=(5,5), dpi=96)

    
    ax.plot(r[:, 0], r[:, 1], 'r', label="Trajectory")
    ax.axhline(0, color='k')
    ax.plot(hstack((x_2, x_2[::-1])), hstack((y_2, -y_2[::-1])))
    ax.plot(-pi_2, 0, 'bo', label="$m_1$")
    ax.plot(1 - pi_2, 0, 'go', label="$m_2$")
    ax.plot(x_0, y_0, 'ro')
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

    
    m_1 = 5.974E24  # kg
    m_2 = 7.348E22 # kg
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
    
    L_2 = newton(func=collinear_lagrange, x0=1, args=(pi_2,))
    L_1 = newton(func=collinear_lagrange, x0=0, args=(pi_2,))
    L_3 = newton(func=collinear_lagrange, x0=-1, args=(pi_2,))
    print(f"{L_1=}, {L_2=}, {L_3=}")
    fig, ax = plt.subplots(figsize=(5,5), dpi=96)
    ax.set_xlabel("$x^*$")
    ax.set_ylabel("$y^*$")

    # Plot the orbits
    ax.axhline(0, color='k')
    ax.plot(hstack((x_2, x_2[::-1])), hstack((y_2, -y_2[::-1])))
    ax.plot(hstack((x_1, x_1[::-1])), hstack((y_1, -y_1[::-1])))
    ax.plot([-pi_2, 0.5 - pi_2, 1 - pi_2, 0.5 - pi_2, -pi_2], [0, sqrt(3)/2, 0, -sqrt(3)/2, 0], 'k', ls="--", lw=1)

    # Plot the Lagrange Points and masses
    ax.plot(L_1, 0, 'rv', label="$L_1$")
    ax.plot(L_2, 0, 'r^', label="$L_2$")
    ax.plot(L_3, 0, 'rp', label="$L_3$")
    ax.plot(0.5 - pi_2, sqrt(3)/2, 'rX', label="$L_4$")
    ax.plot(0.5 - pi_2, -sqrt(3)/2, 'rs', label="$L_5$")
    ax.plot(0, 0, 'k', marker=center_of_mass, markersize=10)
    ax.plot(-pi_2, 0, 'bo', label="$m_1$")
    ax.plot(1 - pi_2, 0, 'go', label="$m_2$")
    ax.legend()
    ax.set_aspect("equal")
    plt.show()
        
Lagrange_Points()    