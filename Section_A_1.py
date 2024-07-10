#!/usr/bin/env python
import time
import argparse
from flyt_python import api

# Create an instance of the Flyt drone navigation class with a timeout of 120 seconds
drone = api.navigation(timeout=120000) 

# Wait for at least 3 seconds to ensure the drone interface is properly initialized
time.sleep(3)

# Parsing command line arguments
# Initialize the argument parser to process a float value from the command line
parser = argparse.ArgumentParser(description='Process a float value representing the side length of the square.')
parser.add_argument('side', metavar='side_length', type=float, help='Side length of the square')
args = parser.parse_args()

# Store the parsed side length value
side_length = args.side

# Take off to a height of 5 meters
print "Taking off!"
drone.take_off(5.0)

# Move the drone in a square path based on the provided side length
print 'Flying in square with side length', side_length
# Move forward by side_length meters
drone.position_set(side_length, 0, 0, relative=True)
# Move right by side_length meters
drone.position_set(0, side_length, 0, relative=True)
# Move backward by side_length meters
drone.position_set(-side_length, 0, 0, relative=True)
# Move left by side_length meters back to the starting point
drone.position_set(0, -side_length, 0, relative=True)

# Land the drone
print "Landing"
drone.land(False)

# Disconnect from the drone and shutdown the instance
drone.disconnect()

