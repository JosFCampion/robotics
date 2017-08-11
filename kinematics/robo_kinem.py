from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt

class KinoJoint:
    def __init__(self, start_pos, length, rot_axis):
        # FIXME: eventually add prismatic joints too
        self.x = start_pos
        self.L = length
        if not (rot_axis == 'x' or rot_axis == 'y'
                or rot_axis == 'z'):
            raise ValueError(
            "Invalid rotation axis (choose 'x' 'y' or 'z').")
        self.ax = rot_axis
        self.R = np.identity(3) # start unrotated
    
    def rotate(self, q):
        cq = cos(q)
        sq = sin(q)
        if self.ax == 'x':
            self.R = np.array([[1,0,0],[0,cq,-sq],[0,sq,cq]])
        elif self.ax == 'y'
            self.R = np.array([[cq,0,sq],[0,1,0],[-sq,0,cq]])
        else:
            self.R = np.array([[cq,-sq,0],[sq,cq,0],[0,0,1]])



