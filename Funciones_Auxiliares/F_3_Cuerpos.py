from numpy import sqrt, array, hstack, cos, sin, abs, concatenate, linspace, pi, zeros_like, sum, square

def F_3_Cuerpos(U,t):
  
        x, y, z = U[:3]
        xdot, ydot, zdot = U[3:]
        m_1 = 5.974E24 
        m_2 = 7.348E22 
        pi_2 = m_2/(m_1 + m_2)

        # Define the derivative vector
        Ydot = zeros_like(U)
        Ydot[:3] = U[3:]

        sigma = sqrt(sum(square([x + pi_2, y, z])))
        psi = sqrt(sum(square([x - 1 + pi_2, y, z])))
        Ydot[3] = 2 * ydot + x - (1 - pi_2) * (x + pi_2) / sigma**3 - pi_2 * (x - 1 + pi_2) / psi**3
        Ydot[4] = -2 * xdot + y - (1 - pi_2) * y / sigma**3 - pi_2 * y / psi**3
        Ydot[5] = -(1 - pi_2)/sigma**3 * z - pi_2/psi**3 * z
        return Ydot