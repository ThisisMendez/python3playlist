class Planet: 

    def __init__(self, name, radius, gravity, system):
        self.name= name
        self.radius= radius
        self.gravity= gravity
        self.system= system

    def orbit(self): 
        return f'{self.name} is orbiting in the {self.system}'

hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'the gravity is: {hoth.gravity}')
print(hoth.orbit())

Naboo = Planet('Naboo', 300000, 8, 'Naboo System')
print(f'Name:{Naboo.name}')
print(f'Radius:{Naboo.Radius}')
print(f'Gravity:{Naboo.gravity}')
print(Naboo.orbit())

#If we want to pass our own parameters we need to use the init function 
#Ex. If we wanted to create our own planet we do that using the init functions 
#If we dont create the init functions pyhton will do it for you 

#We are Creating multiple instances of this class passing unquie data for each planet
#Than we can access that data in the def__init__ function so it can be assign to those props
