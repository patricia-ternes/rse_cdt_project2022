# Step 1: Receive Radius value:
radius = input("Enter radius (m)")
import numpy as np
import random
import pytest

# initialise variables and counters
inside_points = 0
outside_points = 0
error = 1
desired_error = 0.01
Real_Area = (radius ** 2) * np.pi
iteration_number = 0
# Need to make loop starting here
while error > desired_error:

    # Step 2: generate random x and y value inside a line of 2*radius size

    x_coord = (random.random() * 2) - 1
    y_coord = (random.random() * 2) - 1

    # Check if within or outside circle. Need to calculate distance from origin. If < radius, within.

    dist = np.sqrt(x_coord ** 2 + y_coord ** 2)

    if dist < radius:
        inside_points = inside_points + 1
    else:
        outside_points = outside_points + 1

    square_area = 4 * radius ** 2
    circle_area = inside_points / (inside_points + outside_points) * square_area

    error = circle_area - Real_Area
    iteration_number = iteration_number + 1
    if iteration_number > 1000:
        break
