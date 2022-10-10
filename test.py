print()

# Velocity Calculator
"""
m = mass
g = gravity
t = time
c = inner_value (1/2 p A C)
p = fluid
A = area
C = constant

Formula = v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
"""

print("Welcome to the velocity calculator. Please enter the following: \n")

import math

# m
mass = float(input("Mass (in kg): "))

# g
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))

# t
time = float(input("Time (in seconds): "))

# p
fluid = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))

# A
area = float(input("Cross sectional area (in m^2): "))

# C
constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# c = 1/2 p A C
inner_value = (1/2) * fluid * area * constant
print(f"The inner value of c is: {inner_value:.3f}")

# Velocity
# Formula = v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
velocity_time = math.sqrt((mass * gravity) / inner_value) * (1 - math.exp((-math.sqrt(mass * gravity * inner_value) / mass) * time))

# Calculation
print(f"The velocity after {time} seconds is: {velocity_time:.3f} m/s \n")






