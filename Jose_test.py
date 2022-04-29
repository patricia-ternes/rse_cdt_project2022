# Step 1: Receive Radius value:
radius = input("Enter radius (m)")
inside_points = 0  # initialise counter
outside_points = 0  # initialise counter

# Need to make loop starting here

# Step 2: generate random x and y value inside a line of 2*radius size
import random

x_coord = (random.random() * 2) - 1
y_coord = (random.random() * 2) - 1

# Check if within or outside circle. Need to calculate distance from origin. If < radius, within.
import numpy as np

dist = np.sqrt(x_coord ** 2 + y_coord ** 2)

if dist < radius:
    inside_points = inside_points + 1
else:
    outside_points = outside_points + 1

# To Do:
# Calculate error, compare error to min error at which you can stop the loop
# Include a second way to stop in case of code error.
