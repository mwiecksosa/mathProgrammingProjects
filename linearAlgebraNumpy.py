#Michael Wieck-Sosa Problem 4
import numpy as np
import matplotlib.pyplot as plt

#1
Q = np.random.random((4,4))

print("Printing random 4x4 matrix below...")
print(Q)

u = Q[:,0]
v = Q[:,1]
w = Q[:,2]
x = Q[:,3]

#Gram-Schmidt process
u /= np.linalg.norm(u)

v -= v.dot(u)*u
v /= np.linalg.norm(v)

w -= w.dot(u)*u + w.dot(v)*v
w /= np.linalg.norm(w)

x -= x.dot(u)*u + x.dot(v)*v + x.dot(w)*w
x /= np.linalg.norm(x)

#orthogonal matrix O
O = np.stack((u,v,w,x))

print("Printing orthogonal matrix below...")
print(O)
print("Printing result of matrix multiplication below...")
print(O.dot(O.T))
print("The resulting I.D. matrix implies that the orthogonality property holds")

#2
#problem 4 called "Using Numpy in Linear Algebra" so assuming numpy ok

A = np.zeros((100,100))

for i in range(100):
    for j in range(100):
        if i == j:
            A[i][j] = 2
        elif abs(i - j) == 1:
            A[i][j] = -1

eigVals, eigVecs = np.linalg.eig(A)

minEigVal = eigVals[0]

for i in range(eigVals.shape[0]): #quick way to implement because numpy eig is ordered
    if eigVals[i] < minEigVal:
        minEigVal = eigVals[i]
        minEigVec = eigVecs[i]

print("Smallest eigenvalue is %f:"%(minEigVal))
print("Plotting eigenvector corresponding to minimum eigenvalue...")
plt.plot(minEigVec)
plt.show()
