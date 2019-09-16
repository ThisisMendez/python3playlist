from space.planet import Planet
from space.calc import planet_mass, planet_vol

Naboo = Planet('Naboo', 300000, 8, 'Naboo System')

naboo_mass = planet_mass(Naboo.gravity, Naboo.radius)
naboo_vol = planet_vol(Naboo.radius)
print(f'{Naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')
