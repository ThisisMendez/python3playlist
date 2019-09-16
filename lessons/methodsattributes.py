class Planet: 

    shape = 'round' #this is attribute that is the same to the entire class
    
    def __init__(self, name, radius, gravity, system):
        self.name= name
        self.radius= radius
        self.gravity= gravity
        self.system= system

    def orbit(self): 
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod #common to all planets. Has access to class lvl attributes
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity' 

    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins and spins at {speed}'

Naboo = Planet('Naboo', 300000, 8, 'Naboo System')

print(Naboo.spin('a very high speed'))

