def rho(h):
    '''
    [MKS] SI unit
    find air density by passing h[km]

    example:

        if we know the height as 18[km]
        we can get rho by

        rho = rho(18)  

    '''
    return 1.2257 * (1- 0.0226*h) ** ( 4.25713 )
    # rho = 0.002378 * (1- 0.0226*h) ** ( 4.25713 )
    # return rho

# print rho(18)

from numpy import sqrt
def V_ss(rho,C_L=0.7,S=50,m=150):
    '''
    [MKS] SI unit
    find steady-state velocity of the aircraft 
    given the rho value which is of the height(in [km] unit)

    example:

        V_ss = V_ss(rho(18)) 
            
        that is, at the height of 18[km] sky
        the velocity which is required to maintain the steady-state
    '''
    g   = 9.8
    C_L = C_L
    S   = S
    m   = m
    rho = rho

    V = sqrt( ( 2*m*g )/( rho*S*C_L ) ) 
    V_unit = str(V) + '[m/s]'

    return V

