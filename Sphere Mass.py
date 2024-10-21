import math

# Given values
radius = 125000  # in meters
density_rock = 2500  # in kg/m^3
density_iron = 7870  # in kg/m^3

# Step 1: Volume of the sphere
volume = (4/3) * math.pi * radius**3  # volume in cubic meters

# Step 2: Average density
average_density = (density_rock + density_iron) / 2  # in kg/m^3

# Step 3: Mass of the sphere
mass = volume * average_density  # mass in kg

# Output the mass
print(f"The mass of the sphere is approximately {mass:.2e} kg")