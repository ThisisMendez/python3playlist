class Planet: 

    def __init__(self):
        self.name='Hoth'
        self.radius= 200000
        self.gravity= 5.5
        self.system= 'Hoth System'

    def orbit(self): 
        return f'{self.name} is orbiting in the {self.system}'

hoth = Planet()
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'the gravity is: {hoth.gravity}')
print(hoth.orbit())

planetX = Planet()

# Created first class (Planet) than created a new object 
# base on that class which had different props. But if we created
# a new instance of this class it will have the same prop values


