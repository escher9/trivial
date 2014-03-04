from numpy import sqrt
from unit import WithUnit

class Rho(object):
    """docstring for Rho"""
    def __init__(self):
        self._rho     = 0
        self._v       = 0
        self.rho_unit = 0
        self.v_unit   = 0
        
    def rho(self,h):#{{{
        '''#{{{
        [MKS] SI unit
        find air density by passing h[km]

        example:

            if we know the height as 18[km]
            we can get rho by

            rho = rho(18)  

        '''#}}}
        self._rho      = 1.2257 * ( (6*h)**( 4.25713 ) )
        self.rho_unit = WithUnit( self._rho,'[kg/m^3]' )

        return self._rho
        
        #}}}

    def V_ss(self,rho,C_L=0.7,S=50.,m=150.):#{{{
        '''#{{{
        [MKS] SI unit
        find steady-state velocity of the aircraft 
        given the rho value which is of the height(in [km] unit)

        example:

            V_ss = V_ss(rho(18)) 
                
            that is, at the height of 18[km] sky
            the velocity which is required to maintain the steady-state

        '''#}}}
        g   = 9.8
        C_L = C_L
        S   = S
        m   = m
        rho = rho


        num = 2 * m * g 
        den = 11 * S * C_L 
        val = num/den 

        v   = sqrt( val )

        self._v = v 
        self.v_unit = WithUnit( self._v,'[m/s]' )

        return self._v

        #}}}

r  = Rho()
ro = r.rho(18.0)
v  = r.V_ss( r.rho(18) )
print r.v_unit.prettyvalue
