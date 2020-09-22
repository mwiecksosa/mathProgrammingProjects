import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d

domain = [0,1] # use the unit cube (in question 3)
fig=plt.figure()
#ax=fig.add_subplot(111,projection='3d')
ax = fig.gca(projection='3d')

#1
def perspectiveProjection(x, a, u, h, d):

    n = x.shape[1]
    m = u.shape[0]

    mOnes = np.ones((m,1)) #3 by 1
    nOnes = np.ones((n,1))
    nOnes = nOnes.T #1 by n

    p0 = a + d*u # origin in image plane
    c = float((p0.T).dot(u))

    #my compiler prefers .dot over @   :)
    num = (a.dot((u.T).dot(x)-c) + (c - (u.T).dot(a))*x)
    denom = mOnes.dot((u.T).dot(x - a.dot(nOnes)))
    px = num / denom

    print((x.T).dot(u))
    print("Check if our projected matrix dotted with u equals c")
    print((u.T).dot(px))
    print "c = %f" % (c)


    v = np.cross(u.T,h.T)
    v = v.reshape(3,1)

    xCoords = (h.T).dot(px - p0) #x Coord
    yCoords = (v.T).dot(px - p0) #y Coord

    s = np.linspace(-2,2,20)
    t = np.linspace(-2,2,20)
    s, t = np.meshgrid(s,t)
    X = p0[0] + s*h[0] + t*v[0] # 3D Coord
    Y = p0[1] + s*h[1] + t*v[1]
    Z = p0[2] + s*h[2] + t*v[2]

    ax.plot_surface(X,Y,Z,color = 'gray', alpha=0.5) # plot mesh grid
    ax.scatter(*a,color='green') # plot camera aperture
    #ax.quiver(*p0,*u,length=0.5) # plot camera direction vector
    #ax.quiver(*p0,*h,length=0.5) # horizontal basis
    #ax.quiver(*p0,*v,length=0.5) # vertical basis
    ax.scatter(*px)

    # Setting the length of the axes and labels
    ax.set_xlim(-1,4)
    ax.set_ylim(-1,4)
    ax.set_zlim(-1,4)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

    # Plot the points projected onto the plane
    plt.scatter(xCoords,yCoords)
    # Now we have to draw the lines connecting the vertices
    # so our 2D image has some character, not just dots.
    I1 = np.array([0, 1, 3, 2, 0])
    I2 = I1 + 4
    I3 = np.array([1, 3, 7, 5, 1])
    I4 = np.array([6, 4, 0, 2, 6])
    plt.plot(xCoords[0,I1],yCoords[0,I1],'k')
    plt.plot(xCoords[0,I2],yCoords[0,I2],'k')
    plt.plot(xCoords[0,I3],yCoords[0,I3],'k')
    plt.plot(xCoords[0,I4],yCoords[0,I4],'k')

    plt.show()

    return px


#2
print("Direct Proof:")
print("Suppose x lies in the image plane, that is, u@x = c")
print("Then we have...")
print("P(x) = ((u@x - c)*a + (c - u@a)*x) / (u * (x - a))")
print(" = (c - u@a)*x) / u@(x - a) since u@x = c and with simplification")
print(" = (c - u@a)*x) / (u@x - u@a) by distributive law")
print(" = (c - u@a)*x) / (c - u@a) since u@x = c")
print(" = x by cancellation law")
print("QED")

#3
print("Yes, perspective projection preserves lines.")
print("However, not necessarily parallel lines, angles, or distances")
print("Consider the line with endpoints (x1,y1,z1) and (x2,y2,z2)")
print("The x,y,z coordinates of the line may be (respectively) parametrized as:")
print("Lx(t) = (t*x1 + (1-t)*x2")
print("Ly(t) = (t*y1 + (1-t)*y2")
print("Lz(t) = (t*z1 + (1-t)*z2")
print("with some variable t = {x E R | x E [0,1]}")
print("Then the projection is given the multiplication of Lx(T),Ly(t), and Lz(t) by the constant (1 / (d(t*z1 + (1-t)*z2)))")
print("For the distance d = ((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)^(1/2)")
print("Stated previously, t = {x E R | x E [0,1]}, so the different values of t give different lines.")
print("QED")





#5 before #4 to compare

#5
points = np.array([[0,1,0,1,0,1,0,1],[0,0,1,1,0,0,1,1],[0,0,0,0,1,1,1,1]])
points = points.T
ax.scatter3D(points[:,0], points[:,1], points[:,2])

verts=[[points[0],points[1],points[3],points[2]],
 [points[0],points[1],points[5],points[4]],
 [points[2],points[3],points[7],points[6]],
 [points[1],points[3],points[7],points[5]],
 [points[4],points[5],points[7],points[6]],
 [points[6],points[4],points[0],points[2]]]

faces = art3d.Poly3DCollection(verts,
edgecolors='g', linewidths=1.5)
faces.set_facecolor((0.,1.,1.,0.1))  # make it cyan #00ffff
ax.add_collection3d(faces)
a = 0.5+np.array([1,1,1]).reshape(3,1)
u = np.array([-1.5,-0.5,-0.5]).reshape(3,1)
u = u/np.linalg.norm(u)

h = np.array([-u[1], u[0], u[2]]).reshape(3,1)
h = h/np.linalg.norm(h)
d = -0.5*-1
x = points.T
per = perspectiveProjection(x, a, u, h, d)
print("Yes, the perspective rendering in mplot3d matches the perspective projection")
plt.show()


#4
#parallel to the x axis
x = np.array([[0,1,0,1,0,1,0,1],[0,0,1,1,0,0,1,1],[0,0,0,0,1,1,1,1]])
a = np.array([[5],[0.5],[0.5]])
u = np.array([[-1],[0],[0]])
h = np.array([[0],[1],[0]])
d = 2
result = perspectiveProjection(x,a,u,h,d)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(result[0],result[1])
print("Parallel to the x axis")
plt.show()


#from the first octant
x = np.array([[0,1,0,1,0,1,0,1],[0,0,1,1,0,0,1,1],[0,0,0,0,1,1,1,1]])
a = np.array([[5],[5],[0.5]])
u = np.array([[-1],[-1],[-0.1]])
h = np.array([[-0.5],[0.5],[0]])
d = 2
result = perspectiveProjection(x,a,u,h,d)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(result[0],result[1])
print("From the first octant")
plt.show()

#from the origin
x = np.array([[0,1,0,1,0,1,0,1],[0,0,1,1,0,0,1,1],[0,0,0,0,1,1,1,1]])
a = np.array([[0],[0],[0]])
u = np.array([[1],[1],[1]])
h = np.array([[-1],[1],[0]])
d = 2
result = perspectiveProjection(x,a,u,h,d)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(result[0],result[1])
print("From the origin")
plt.show()

print("Done :D")
