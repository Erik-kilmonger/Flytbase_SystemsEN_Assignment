#!/usr/bin/env python
import time
import argparse
from flyt_python import api
import math

drone = api.navigation(timeout=120000)  # instance of Flyt drone na$

# at least 3 seconds sleep time for the drone interface to initiali$
time.sleep(3)

# Parsing command line arguments
parser = argparse.ArgumentParser(description='Process a float value$
parser.add_argument('side', metavar='side_length', type=float, help$
args = parser.parse_args()

# Let's fly
side_length = args.side

print "Taking off!"
drone.take_off(5.0)

print 'Flying in a triangle with side length', side_length

# Calculate the height of the equilateral triangle
height = (math.sqrt(3) / 2) * side_length

# Move to the first point (relative to the starting point)
drone.position_set(side_length, 0, 0, relative=True)

# Move to the second point (relative to the current position)
drone.position_set(-side_length / 2, height, 0, relative=True)

# Move back to the starting point (relative to the current position)
drone.position_set(-side_length / 2, -height, 0, relative=True)

print "Landing"
drone.land(False)
