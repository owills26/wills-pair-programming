#Olivia Wills - Polar to Cartesian Coordinates

import numpy as np
def polar_to_cartesian(radius, angle_radians):
    assert (type(radius)==float) or (type(radius)==int) or (type(radius)==np.array),\
    "The radius should be a float, np array or an integer"
    assert (type(angle_radians)==float) or (type(angle_radians)==int) or (type(angle_radians)==np.array),\
    "The angle should be a float, np array or an integer"
    #Defensive programming, makes sure that a string isn't being inputted
    x = radius * np.cos(angle_radians)
    #Calculates the x component
    y = radius * np.sin(angle_radians)
    #Calculates the y component
    return x, y

