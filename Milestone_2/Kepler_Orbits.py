
from numpy import array

def F_Kepler(U):           
   
   x = U[0]
   y = U[1]
   Vx = U[2]
   Vy = U[3]
   mr = (x**2 + y**2)**1.5
   
   
   return array( [Vx , Vy , -x/mr, -y/mr] )