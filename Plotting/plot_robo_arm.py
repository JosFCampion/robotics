import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
#theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
#z = np.linspace(-2, 2, 100)
#r = z**2 + 1
#x = r * np.sin(theta)
#y = r * np.cos(theta)
#ax.plot(x, y, z, label='parametric curve')
#ax.legend()

joint_types = ['r','r','r']
arm_lengths = [3,2,1]
l1 = arm_lengths[0]
l2 = arm_lengths[1]
l3 = arm_lengths[2]
arm_intertias = [10,5,2]
ax.plot([0,1],[0,0],[0,0],label='x')
ax.plot([0,0],[0,1],[0,0],label='y')
ax.plot([0,0],[0,0],[0,1],label='z')
q1 = np.pi/4
q2 = np.pi/3
q3 = -np.pi/6
x1 = l1*np.cos(q1)
y1 = l1*np.sin(q1)
z1 = 0
x2 = x1+l2*np.cos(q1)*np.cos(q2)
y2 = x2+l2*np.sin(q1)*np.cos(q2)
z2 = l2*np.sin(q2)
def Rx(q):
    return np.array([[np.cos(q),-np.sin(q),0],[np.sin(q),np.cos(q),0],[0,0,1]])
def Ry(q):
    return np.array([[np.cos(q),0,-np.sin(q)],[0,1,0],[np.sin(q),0,np.cos(q)]])
def Rz(q):
    return np.array([[1,0,0],[0,np.cos(q),-np.sin(q)],[0,np.sin(q),np.cos(q)]])
#plt.plot([0,x1],[0,y1],[0,z1],label='arm1')
#plt.plot([x1,x2],[y1,y2],[z1,z2],label='arm2')
X1 = np.dot(Rx(q1),[1,0,0])
# print("new x: ",X1rot)
plt.plot([0,X1[0]],[0,X1[1]],[0,X1[2]])
X2 = X1 + np.dot(np.dot(Rx(q1),Ry(q2)),[l2,0,0])
plt.plot([X1[0],X2[0]],[X1[1],X2[1]],[X1[2],X2[2]])
ax.legend()
plt.show()


