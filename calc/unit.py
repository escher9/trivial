UNIT = {'velocity' :  [ '[ft/s]'      , '[m/s]'    ],
         'density' :  [ '[slug/ft^3]' , '[kg/m^3]' ]
        } 
class WithUnit(object):
    """docstring for Unit"""
    def __init__(self,type,value,SI=1):
        self.SI    = SI
        self.value = value
        self.unit  = UNIT[type][SI]
        self.type  = type
        self.prettyvalue = str(self.value) + self.unit
        
        if self.SI and type is 'velocity':

            to_km =  self.value * (1/1000.)*(3600)
            self.prettyvalue_km = str(to_km) + '[km/h]' 

    def convert(self):
        if self.type is 'velocity':
            conversion_factor = 3280.8
        elif self.type is 'density':
            conversion_factor = 515.3787147

        self.value *= (conversion_factor)**( (-1)**(self.SI) )

        self.SI = int(not self.SI) 
        self.unit = UNIT[self.type][self.SI]

        self.prettyvalue = str(self.value) + self.unit

        

