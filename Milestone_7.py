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
#print( "   ==                      Ruben Garrido Echevarria                        ==" )
#print( "   ==========================================================================" )
#print( "   ==========================================================================" )
#print( "" )
#print( "" )
#print( "" )
#print( "   ==========================================================================" )
#print( "   =========================    FINAL MILESTONE    ==========================" )
#print( "   ==========================================================================" )
#print( "" )



from Sistemas_Dinamicos.Temporal_integrator import  RK4, Adams_Bashforth_4th_order, Euler, Crank_Nicolson

from Sistemas_Dinamicos.Cauchy_Problem import Cauchy_problem
from Animaciones.Animacion import create_animation
from Animaciones.Graphics import Plot_2D, Plot_3D
from Animaciones.Histogram import Histogram_2D, Histogram_3D
from Sistemas_Dinamicos.Dynamic_System import VanDerPol_Libre, VanDerPol_ForzadoArmonico, VanDerPol_ForzadoEstocastico, VanDerPol_Libre2, VanDerPol_Libre3

import matplotlib.pyplot as plt
from numpy import array, zeros, linspace, abs, transpose, float64, histogram2d, meshgrid, ones_like, max, min, arange
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation


# #Inicialización de las listas de valores


t0 = 0
h = 0.01


t_final = 50
N =  t_final/h
t_values = arange(t0, t_final + h, h)
U0 = array([0,1,0])

print("Selecione el integrador temporal: 1 = Euler, 2 = RK4, 3 = Admas_Bashforth 4 Orden, 4 = Crank_Nicolson")
# Selector=input()  #Eligo que integrador temporal que va a usar para resolver el programa
Selector= input() 

try:
    Selector=float(Selector)

    if Selector == 1:
            
        U = Cauchy_problem(t_values, U0, Euler, VanDerPol_ForzadoEstocastico )
                  
    
    if Selector == 2:

        U = Cauchy_problem(t_values, U0, RK4, VanDerPol_ForzadoEstocastico)                        

    if Selector == 3:
        
       U  = Cauchy_problem(t_values, U0,Adams_Bashforth_4th_order, VanDerPol_ForzadoEstocastico)        
        
    if Selector == 4:
   
        U = Cauchy_problem(t_values, U0, Crank_Nicolson, VanDerPol_ForzadoEstocastico )
        

        

            
except ValueError:
          print("El valor introducido no es válido")   
          
          
#create_animation(U, 10, 25, 'Animaciones/Anim_VDPL_Muneg.gif',N)

Plot_2D(U[:,0], U[:,1], "x", "y")   

Plot_3D(U[:,0], U[:,1], U[:,2], "x", "y")      # Solo cuado se resuelva un problema de Cauchy con condiciones en tres dimensiones

Histogram_2D(U[:,0], U[:,1], "x", "y")   
Histogram_3D(U[:,0], U[:,1], "x", "y")




