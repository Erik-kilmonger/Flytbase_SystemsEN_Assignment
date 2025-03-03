#!/usr/bin/env python
import time
from flyt_python import api

# Initialize the drone navigation system with a timeout of 120 seconds.
drone = api.navigation(timeout=120000)

# Wait for at least 3 seconds to ensure the drone interface is fully initialized.
time.sleep(3)

# Indicate that the drone is about to take off.
print 'Taking off'
# Command the drone to take off to a height of 5 meters.
drone.take_off(5.0)

# Indicate that the drone will start moving along the setpoints.
print 'Going along the setpoints'
# Move the drone 6.5 meters forward from its current position.
drone.position_set(6.5, 0, 0, relative=True)
# Move the drone 6.5 meters to the right from its current position.
drone.position_set(0, 6.5, 0, relative=True)
# Move the drone 6.5 meters backward from its current position.
drone.position_set(-6.5, 0, 0, relative=True)
# Move the drone 6.5 meters to the left from its current position.
drone.position_set(0, -6.5, 0, relative=True)

# Indicate that the drone is about to land.
print 'Landing'
# Command the drone to land.
drone.land(async=False)

# Disconnect from the drone and shut down the navigation system.
drone.disconnect()





#arun.
