class WithUnit(object):
    """docstring for Unit"""
    def __init__(self,value,unit):
        self.value = value 
        self.unit = unit 
        self.prettyvalue = str(self.value) + self.unit
        
