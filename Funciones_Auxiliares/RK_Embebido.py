
## Código para el Runge Kuta embebido.

from numpy import zeros, array, float64, dot
from numpy.linalg import norm 

def Embedded_RK( U, dt, t, F, q, Tolerance): 
  
   
    N_stages = { 2:2, 3:4, 8:13  }                  # Dicionario. Al valor 2 le corresponde 2, al 3 el valor 4 y al 8 le corresponde el 13        
    Ns = N_stages[q]                                # q es el orden del esquema numérico. Cuando introduzca el orden, Ns (tamaño de los vectores y matrices de los coeficientes del Runge-Kutta) tomará el valor del valor dependiendo de que número tenga q (clave)
    a = zeros( (Ns, Ns), dtype=float64)             # a son la matriz de coeficientes que se usan para calcular cada dunción del Runge-Kutta
    b = zeros(Ns); bs = zeros(Ns); c = zeros(Ns)    # b serán los coeficientes que van con cada una de las funciones Rounge-Kutta al sumarlas todas en el cálculo del paso. Estas funciones son iguales en el Runge-Kutta normal y el embebido
                                                    # c es el coeficiente que acompaña a los delta de t para calcular cada función k en el Runge-Kutta
    if Ns==2:                                       # Si Ns = 2 el orden del esquema es 2 y por lo tanto se ha accedido en el diccionario al valor 2 
                                                    # Lo coeficientes a, b, c son dato y corresponden a los de un Runge-Kutta 2
     a[0,:] = [ 0, 0 ]                              # El valor de a para la primera fila y todas la columnas (dos) es 0, 0   a11 = 0 , a12 = 0 
     a[1,:] = [ 1, 0 ]                              # El valor de a para la segunda fila y todas la columanas (dos) es 1,0   a21 = 1 , a22 = 0
     b[:]  = [ 1/2, 1/2 ]                           # Al calcular el paso de tiempo las dos funciones k1 y k2 tienen el mismo peso
     bs[:] = [ 1, 0 ]                               
     c[:]  = [ 0, 1]                                # En la k1 no suma paso de tiempo. Delta t * c1 = 0 -> tn el en esa función. En k2 Delta t * c2 + tn     

    elif Ns==13:                                    # el orden del escquema es un Runge-Kutta 9 por lo que el tamaño de matrices y vectores de los coeficientes.
      
      # El valor de estos coeficientes depeonde del número de funciones Runge-Kutta.
        
       c[:] = [ 0., 2./27, 1./9, 1./6, 5./12, 1./2, 5./6, 1./6, 2./3 , 1./3,   1., 0., 1.]

       a[0,:]  = [ 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0] 
       a[1,:]  = [ 2./27, 0., 0., 0., 0., 0., 0.,  0., 0., 0., 0., 0., 0] 
       a[2,:]  = [ 1./36 , 1./12, 0., 0., 0., 0., 0.,  0.,0., 0., 0., 0., 0] 
       a[3,:]  = [ 1./24 , 0., 1./8 , 0., 0., 0., 0., 0., 0., 0., 0., 0., 0] 
       a[4,:]  = [ 5./12, 0., -25./16, 25./16., 0., 0., 0., 0., 0., 0., 0., 0., 0]
       a[5,:]  = [ 1./20, 0., 0., 1./4, 1./5, 0., 0.,0., 0., 0., 0., 0., 0] 
       a[6,:]  = [-25./108, 0., 0., 125./108, -65./27, 125./54, 0., 0., 0., 0., 0., 0., 0] 
       a[7,:]  = [ 31./300, 0., 0., 0., 61./225, -2./9, 13./900, 0., 0., 0., 0., 0., 0] 
       a[8,:]  = [ 2., 0., 0., -53./6, 704./45, -107./9, 67./90, 3., 0., 0., 0., 0., 0] 
       a[9,:]  = [-91./108, 0., 0., 23./108, -976./135, 311./54, -19./60, 17./6, -1./12, 0., 0., 0., 0] 
       a[10,:] = [ 2383./4100, 0., 0., -341./164, 4496./1025, -301./82, 2133./4100, 45./82, 45./164, 18./41, 0., 0., 0] 
       a[11,:] = [ 3./205, 0., 0., 0., 0., -6./41, -3./205, -3./41, 3./41, 6./41, 0., 0., 0]
       a[12,:] = [ -1777./4100, 0., 0., -341./164, 4496./1025, -289./82, 2193./4100, 51./82, 33./164, 19./41, 0.,  1., 0]
      
       b[:]  = [ 41./840, 0., 0., 0., 0., 34./105, 9./35, 9./35, 9./280, 9./280, 41./840, 0., 0.] 
       bs[:] = [ 0., 0., 0., 0., 0., 34./105, 9./35, 9./35, 9./280, 9./280, 0., 41./840, 41./840]     
     

    
    k = RK_stages( F, U, t, dt, a, c )                                  # Crea cada una de las funciones k 
    Error = dot( b-bs, k )                                              # El error local en cada paso                  

    dt_min = min( dt, dt * ( Tolerance / norm(Error) ) **(1/q) )        # Paso de tiempo mínimo es el paso de tiempo por la toleracncia partido por la norma del error todo elevado a la inversa del orden del esquema temporal
    N = int( dt/dt_min  ) + 1                           
    h = dt / N
    Uh = U.copy()

    for i in range(0, N): 

        k = RK_stages( F, Uh, t + h*i, h, a, c ) 
        Uh += h * dot( b, k )

    return Uh



def RK_stages( F, U, t, dt, a, c ):                     # Funcion que crea todas la funciones Runge-Kuta cogiendo los valores de los coefiente a y c

     k = zeros( (len(c), len(U)), dtype=float64 )       # El tamaño de la matriz que contiene todas las funciones k depende del número de funciones c y la dimensión de la condición inicial

     for i in range(len(c)):                            # Bucle para consturir las funciones k

        for  j in range(len(c)-1): 
          Up = U + dt * dot( a[i, :], k)                # Up será la solución U más el apso de timpo por la multiplicación de la matriz de coeficientes y la matriz k

        k[i, :] = F( Up, t + c[i] * dt )                # Ahora para construir k del todo añade a la matriz up la los coeficientes c con su paso de timpo correspoendiente.

     return k 
