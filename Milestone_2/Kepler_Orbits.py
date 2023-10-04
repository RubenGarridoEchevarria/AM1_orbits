
from numpy import array

def F_Kepler(U):           
   
   
   
   x, y, Vx, Vy = U[0], U[1], U[2], U[3]
   mr = (x**2 + y**2)**1.5
   
   
   return array( [Vx , Vy , -x/mr, -y/mr] )