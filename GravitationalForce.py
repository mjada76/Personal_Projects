# Given values for Moon and Earth
mass_earth = 5.972e24 # Mass of the Earth in Kg
mass_moon = 7.342e22  # Mass of the Moon in kg
distance_earth_moon = 384400000  # Distance between Earth and Moon in meters

# Gravitational force between Earth and Moon
G = 6.67430e-11 # gravitational  constant 'G' in m^3, kg^-1
g_force = (G * mass_earth * mass_moon)/    (distance_earth_moon ** 2)
#Gravitational force 
print(f"the gravitational force of 2 celestial objects {g_force:.2e} Newton(N)")