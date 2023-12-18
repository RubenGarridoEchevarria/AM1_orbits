
from Funciones_Auxiliares.RK_Embebido import Embedded_RK

from scipy.optimize import newton
from scipy.integrate import solve_ivp
from Funciones_Auxiliares.F_3_Cuerpos import F_3_Cuerpos

from numpy import sqrt, array, hstack, cos, sin, abs, concatenate, linspace, pi, zeros_like, sum, square
import matplotlib.pyplot as plt

## Código pora la resolucion del problema de los 3 cuerpos restirngidos.


def Problema_Tres_Cuerpos_Restirngidos():

    m_1 = 5.974E24 
    m_2 = 7.348E22 
    pi_2 = m_2/(m_1 + m_2)

    x_0 = 1 - pi_2
    y_0 = .0455
    z_0 = 0
    vx_0 = -0.5
    vy_0 = 0.5
    vz_0 = 0


    r_0 = array((x_0, y_0, z_0))
    v_0 = array((vx_0, vy_0, vz_0))
    Y_0 = hstack((r_0, v_0))



    t_0 = 0  
    t_f = 20  
    t_points = linspace(t_0, t_f, 1000)
    sol = solve_ivp(F_3_Cuerpos, [t_0, t_f], Y_0, t_eval=t_points)

    Y = sol.y.T
    r = Y[:, :3]  
    v = Y[:, 3:]  


    x_2 = (1 - pi_2) * cos(linspace(0, pi, 100))
    y_2 = (1 - pi_2) * sin(linspace(0, pi, 100))
    fig, ax = plt.subplots(figsize=(5,5), dpi=96)

    # Plot the orbits
    ax.plot(r[:, 0], r[:, 1], 'r', label="Trajectory")
    ax.axhline(0, color='k')
    ax.plot(hstack((x_2, x_2[::-1])), hstack((y_2, -y_2[::-1])))
    ax.plot(-pi_2, 0, 'bo', label="$m_1$")
    ax.plot(1 - pi_2, 0, 'go', label="$m_2$")
    ax.plot(x_0, y_0, 'ro')
    ax.set_aspect("equal")

    plt.show()
    
Problema_Tres_Cuerpos_Restirngidos()