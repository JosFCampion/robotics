from numpy import sin, cos
import numpy as np
# import scipy as sp
import matplotlib.pyplot as plt

class Joint:
    def __init__(self, mass, center_of_mass, inertia, length, joint_type, axis):
        self.m = mass
        self.COM = center_of_mass
        self.I = inertia
        self.L = length
        if not (joint_type == 'r' or joint_type == 'p'):
            raise ValueError(
            "Invalid joint type ('r' for revolute or 'p' for 'prismatic'.")
        self.jt = joint_type
        if not(axis == 'x' or axis == 'y' or axis == 'z'):
            raise ValueError("Invalid axis (choose x, y, or z).")
        self.ax = axis
        self.R = np.identity(3) # start unrotated

    def rotate(self, q):
        #if self.jt == 'p'
        #    print("Prismatic joint; rotation does not apply.")
        #    return
        if self.ax == 'x':
           self.R = np.array([[1,0,0],[0,cos(q),-sin(q)],[0,sin(q),cos(q)]])
        elif self.ax == 'y':
           self.R = np.array([[cos(q),0,sin(q)],[0,1,0],[-sin(q),0,cos(q)]])
        else: # self.ax == 'z'
           self.R = np.array([[cos(q),-sin(q),0],[sin(q),cos(q),0],[0,0,1]])
    
    def get_position(self):
        x = np.array([self.L,0,0])
        return np.dot(self.R,x)
            

class RoboticManip:
    def __init__(self, ndof, joints):
        self.joints = joints
        self.njoints = len(joints)
        self.X = np.array(3,self.njoints)
        self.V = np.zeros(3,self.njoints)

    def rotate_joint_i(self, q, i):
        self.joints[i].rotate(q)

    def get_position_i(self, i):
        x = np.array([self.joints[i].length,0,0])

# Testing functions so far
m1 = 1
com1 = [1,0,0]
I1 = np.identity(3)
l1 = 3.2
jt1 = 'r'
ax1 = 'y' 
j1 = Joint(m1, com1, I1, l1, jt1, ax1) 
theta = np.pi/4
j1.rotate(theta)
print(j1.get_position())
        



