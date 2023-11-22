
from numpy import reshape, zeros
from numpy.linalg import norm

def F_N_Cuerpos(U,t, Nb, Nc):
    
    Us = reshape(U, (Nb, Nc, 2))     # Se convierte U en un tensor que contendrá la información de posición y velocidad de todos los cuerpos y sus coordenadas
    F = zeros(len(U))                 
    dUs = reshape(F, (Nb, Nc,2))    # Convierto la derivada (La función F) en un tensor de la misma manera
    
    
    r = reshape(Us[:,:,0], (Nb, Nc))       # Posiciones de los cuerpos y sus coordenadas en una sola matriz
    v = reshape(Us[:,:,1], (Nb, Nc))       # Velocidades de los cuerpos y sus coodenadas
    
    
    drdt = reshape(dUs[:,:,0], (Nb,Nc))   # Lo mismo con las derivadas
    dvdt = reshape(dUs[:,:,1], (Nb,Nc)) 
    
    
    
    for i in range(Nb):  #Bucle para cada cuerpo
        
        drdt[i,:] = v[i,:] # Relleno la derivada de la posición con de cada cuerpo para todas la coordenadas con la velocidad
        
        for j in range(Nb):
            
            if j !=i:     # Si j no es ingual a i
                
                d = r[j,:] - r[i,:]  # Diferencia entre las posiciones de cada cuerpo dos a dos
                dvdt[i,:] = dvdt[i,:] + d[:]/norm(d)**3  # La aceleración de cada cuerpo viene dado por la diferencia entre la posición de cada cuerpo partido del módulo de esa distancia
                
                
    return F
            