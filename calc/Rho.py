from numpy import sqrt
from unit import WithUnit

class Rho(object):
    """docstring for Rho"""
    set = {'velocity':0,'density':0} 
    def __init__(self):
        self._rho      = 0
        self._v        = 0
        self.with_unit = 0
        
    def rho(self,h):#{{{
        '''#{{{
        [MKS] SI unit
        find air density by passing h[km]

        example:

            if we know the height as 18[km]
            we can get rho by

            rho = rho(18)  

        '''#}}}
        self._rho      = 1.2257 * ( (1-0.0226*h)**( 4.25713 ) )

        title = 'density' 
        self.set[title] = WithUnit( title,self._rho )

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
        den = rho * S * C_L 
        val = num/den 

        v   = sqrt( val )

        self._v = v 
        title = 'velocity' 
        self.set[title] = WithUnit( title,self._v )

        return self._v

        #}}}

r  = Rho()
ro = r.rho(0.0)
v0  = r.V_ss( r.rho(0) )
r.set['velocity'].convert()
r.set['velocity'].convert()
r.set['velocity'].convert()
r.set['velocity'].convert()
r.set['velocity'].convert()
print r.set['velocity'].prettyvalue_km
print r.set['density'].prettyvalue
r.set['density'].convert()
print r.set['density'].prettyvalue
