# Import the necessary functions from sympy
from typing import Any
from sympy import symbols, factor

# Define the symbolic variable for the polynomial
x = symbols('x')  # Directly use symbols from sympy
x, y = symbols('x, y')

# Define the polynomial to be factored
polynomial: int | Any = 2*x**2 - y**2

# Factor the polynomial
factored_polynomial = factor(polynomial)

# Output the result
print(f"The factored form of the polynomial is: {factored_polynomial}"),

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# To calculate the slope-intercept form of a line (y = mx + b),
# we need two points (x1, y1) and (x2, y2). Using these points, we can compute the slope (m) and the intercept (b).

# Function to calculate slope (m) and intercept (b) given two points
def slope_intercept(x1, y1, x2, y2):
    # Calculate slope
    m = (y2 - y1) / (x2 - x1)

    # Calculate intercept
    b = y1 - m * x1

    return m, b


# Enter inputs below: t
x1, y1 = 3, 2
x2, y2 = 4, 2

slope, intercept = slope_intercept(x1, y1, x2, y2)
print(f"The slope and intercept is: {slope}, {intercept}")

